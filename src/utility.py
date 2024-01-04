import pandas as pd
import requests
from dotenv import load_dotenv
import os
import os.path
import re
from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta

line_len = 70

operations = [
    "Slice to specific timeframe",
    "Calculate Moving Average for 2023",
    "Future predictions (Forecast)",
    "Exit and select new stock"
]

timeframes = [
    "Today (D)",
    "Five Days (5D)",
    "One Month (1M)",
    "Six Months (6M)",
    "Year to date (YTD)",
    "One Year (1Y)",
    "Five Years (5Y)"
]

# dictionary to story function names
function_names = {
    "TIME_SERIES_DAILY": "TIME_SERIES_DAILY",
    "SYMBOL_SEARCH": "SYMBOL_SEARCH",
    "DIGITAL_CURRENCY_DAILY": "DIGITAL_CURRENCY_DAILY",
    "EARNINGS": "EARNINGS",
    "EARNINGS_CALENDAR": "EARNINGS_CALENDAR"
}

# function to get full URL
def getURL(fname, parameters):
    base_url = "https://www.alphavantage.co/query?"
    func_parameter = f"function={fname}"

    try:
        #get API key
        load_dotenv("../Resources/api_key.env")
        api_key = os.getenv("alphavantage_api_key")

        if api_key is None:
            raise Exception("No Environment Configurations.")
        
    except Exception as ex:
        print(f"Environment configurations not defined: {ex}")
        return ""
    
    return f'{base_url}{func_parameter}{parameters}&apikey={api_key}'

# function get ticker from user
def get_ticker(ticker_list):
    ticker_select = ""

    print("-" * line_len)
    print(f"{'***** Stock Analysis *****':^70}")
    print("-" * line_len)

    live_search = False
    if not ticker_list:
        user_input = input("\nWhat stock do you like to search: ")
        search_params = f"&keywords={user_input}"

        try:
            search_url = getURL(function_names['SYMBOL_SEARCH'], search_params)

            if not search_url:
                return ("Issue with URL.")
            
            ticker_results = requests.get(search_url).json()

            ticker_df = pd.DataFrame(ticker_results['bestMatches'])
            ticker_df.drop(ticker_df[ticker_df['4. region'] != "United States"].index, inplace=True)
            ticker_df.reset_index(inplace=True)

            ticker_list = ticker_df['1. symbol'].iloc[:5]
            live_search = True
        except:
            print(f"Not able to find {user_input}")

    if len(ticker_list) > 0:
        if live_search:
            print(f"\nHere are top stocks from your search\n")
        else:
            print(f"\nHere is list of stocks\n")

        for index, value in enumerate(ticker_list):
            print(f"{index+1} - {value}")
        
        user_selection = getIntInput("\nWhich stock do you like to explore: "\
                                        , 1, len(ticker_list))
        ticker_select = ticker_list[user_selection-1]

    return ticker_select

# prepare data from passed ticker and write to csv
def prepare_ticker_data(ticker, fname="TIME_SERIES_DAILY", interval=60):
    file_name = ""
    url_params = ""
    match fname: 
        case 'TIME_SERIES_INTRADAY':
            file_name = f"intraday_{interval}_{ticker.upper()}.csv"
            url_params = F"&symbol={ticker}&interval={interval}min&outputsize=full"
        case _:
            file_name = "daily_"+ticker.upper()+".csv"
            url_params = f"&symbol={ticker}&outputsize=full"

    if os.path.isfile("../Datasets/" + file_name):
        return True
    
    data_ready = False
    try:
        ticker_results = requests.get(getURL(fname, url_params)).json()

        result_node = "Time Series (Daily)"

        if(fname == "TIME_SERIES_INTRADAY"):
            result_node = f"Time Series ({interval}min)"

        ticker_data_df = pd.DataFrame(ticker_results[result_node]).T
        ticker_data_df.reset_index(inplace=True)

        ticker_data_df.rename(columns={
            'index': 'timestamp',
            '1. open': 'open',
            '2. high': 'high',
            '3. low': 'low',
            '4. close': 'close',
            '5. volume': 'volume' 
        }, inplace=True)
        ticker_data_df

        ticker_data_df.to_csv("../Datasets/" + file_name)
        data_ready = True
    except Exception as ex:
        print(f"No data found for {ticker}, error {ex}")
    
    return data_ready

# function to get crypto data
def prepare_crypto_data(symbol):
    if os.path.isfile("../Datasets/daily_"+symbol.upper()+".csv"):
        return True

    crypto_search_params = f"&symbol={symbol}&market=USD"
    data_ready = False
    try:
        crypto_results = requests.get(getURL('DIGITAL_CURRENCY_DAILY', crypto_search_params)).json()
        
        crypto_data_df = pd.DataFrame(crypto_results['Time Series (Digital Currency Daily)']).T
        crypto_data_df.reset_index(inplace=True)
        crypto_data_df.columns

        crypto_data_df.drop(['1b. open (USD)', '2b. high (USD)','3b. low (USD)', '4b. close (USD)'], axis=1, inplace=True)

        crypto_data_df.rename(columns={
                    'index': 'timestamp',
                    '1a. open (USD)': 'open',
                    '2a. high (USD)': 'high',
                    '3a. low (USD)': 'low',
                    '4a. close (USD)': 'close',
                    '5. volume': 'volume',
                    '6. market cap (USD)': 'marketCap'
                }, inplace=True)

        crypto_data_df.to_csv("../Datasets/daily_"+symbol.upper()+".csv")
        data_ready = True
    except Exception as ex:
        print(f"No data found for {symbol}, error {ex}")
    
    return data_ready

def getIntInput(inputStatment, min_value=None, max_value=None):
    """ helper method to get integer value from user
    
        Args:
            inputStatement str: input string to print for user
            min_value, max_value int: min and max value that user can enter
        
        Return:
            int: returns the integer value of user input
        
        Raises:
            Errors: if user enters any value other digit error will be 
                displayed and ask user to re-enter the value
    """
    while True:
        m_str_value = input(inputStatment)
        try:
            int_value = int(m_str_value)
            if min_value is not None and int_value < min_value:
                print(f"\nPlease enter an integer greater than or equal to {min_value}.\n")
            elif max_value is not None and int_value > max_value:
                print(f"\nPlease enter an integer less than or equal to {max_value}.\n")
            else:
                return int_value
        except ValueError:
            print("\nInvalid input. Please enter an integer.\n")

def getYNInput(inputStatment):
    """ helper method to get Y/N value from user
    
        Args:
            inputStatement str: input string to print for user
        
        Return:
            str: returns the value of user input
        
        Raises:
            Errors: if user enters any value other than Y/N (in any case)
                error will be displayed and ask user to re-enter the value
    """
    while True:
        m_str_value = input(inputStatment)
        try:
            if m_str_value.upper() in ['Y','N']:
                return m_str_value.upper()
        except ValueError:
            print("\nInvalid input. Please enter an Y or N.\n")

def get_operation():  
    print("-" * line_len)
    print(f"{'***** Analysis *****':^70}")
    print("-" * line_len)

    for index,value in enumerate(operations):
        print(f" {index+1}. {value}.")
    print("\n")

    tf_input = getIntInput("Select your option: ", 1, len(operations))

    return  tf_input

def get_timeframe():
    print("-" * line_len)
    print(f"{'***** Timeframes *****':^70}")
    print("-" * line_len)

    for index,value in enumerate(timeframes):
        print(f" {index+1}. {value}.")
    print("\n")

    tf_input = getIntInput("Select timeframe: ", 1, len(timeframes))
    pattern = r"\((.*?)\)"

    return  re.search(pattern, timeframes[tf_input-1]).group(1)

def get_moving_average():
    print("-" * line_len)
    print(f"{'***** Moving Average *****':^70}")
    print("-" * line_len)

    print("\n You will see 50 Day Moving Average by default.")
    ma_input = getYNInput("\n Do you like to add an additional Moving Average [Y/N]: ")

    if ma_input == 'Y':
        second_ma = \
            getIntInput("Enter number of days for additional Moving Average: ", 1, 300)
        return second_ma

def get_future_prediction():
    print("-" * line_len)
    print(f"{'***** Future Predictions *****':^70}")
    print("-" * line_len)

    print("\nYou can predict in (D)ays, (W)eeks, (M)onths, (Y)ears.\n")
    print("Sample formats: ")
    print("45D, 30D, 2W, 10W, 3M, 1Y\n")

    while True:
        future_pred = input("How far do you like to predict: ")

        # Regular expression pattern for validation
        pattern = r"^\d+[DWMY]$"

        if re.match(pattern, future_pred):
            return future_pred
        else:
            print("\nInvalid input format.\n")
            print("Please enter a valid format (e.g., 45D, 2W, 3M, 1Y).\n")

def get_timeslice(timeframe):
    current_date = datetime.now().date()

    match timeframe:
        case '5D':
            return current_date - relativedelta(days=5)
        case '1M':
            return current_date - relativedelta(months=1)
        case '6M':
            return current_date - relativedelta(months=6)
        case 'YTD':
            return datetime(current_date.year, 1, 1)
        case '1Y':
            return current_date - relativedelta(years=1)
        case '5Y':
            return current_date - relativedelta(years=5)
        case _:
            return current_date