import pandas as pd
import requests
from dotenv import load_dotenv
import os
import os.path

# dictionary to story function names
function_names = {
    "TIME_SERIES_DAILY": "TIME_SERIES_DAILY",
    "SYMBOL_SEARCH": "SYMBOL_SEARCH",
    "DIGITAL_CURRENCY_DAILY" : "DIGITAL_CURRENCY_DAILY"
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

    if not ticker_list:
        user_input = input("Enter your search")
        search_params = f"&keywords={user_input}"

        try:
            search_url = getURL(function_names['SYMBOL_SEARCH'], search_params)

            if not search_url:
                return ("Issue with URL.")
            
            ticker_results = requests.get(search_url).json()

            ticker_df = pd.DataFrame(ticker_results['bestMatches'])
            ticker_list = ticker_df['1. symbol'].iloc[:5]
        except:
            print(f"Not able to find {user_input}")

    if len(ticker_list):
        while(True): 
            print(f"Select a ticker to analyze")
            for index, value in enumerate(ticker_list):
                print(f"{index+1} - {value}")
            
            print(f"{'-' * 40}")
            user_selection = input("Enter your selection: ")
            ticker_select = ticker_list[int(user_selection)-1]

            break

        print(ticker_select)
    return ticker_select

# prepare data from passed ticker and write to csv
def prepare_ticker_data(ticker):
    if os.path.isfile("../Datasets/daily_"+ticker.upper()+".csv"):
        return True

    ticker_search_params = f"&symbol={ticker}&outputsize=full"
    data_ready = False
    try:
        ticker_results = requests.get(getURL(function_names['TIME_SERIES_DAILY'], ticker_search_params)).json()

        ticker_data_df = pd.DataFrame(ticker_results['Time Series (Daily)']).T
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

        ticker_data_df.to_csv("../Datasets/daily_"+ticker.upper()+".csv")
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