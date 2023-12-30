import pandas as pd
import requests
import os.path

# dictionary to story function names
function_names = {
    "TIME_SERIES_DAILY": "TIME_SERIES_DAILY",
    "SYMBOL_SEARCH": "SYMBOL_SEARCH"
}

# function to get full URL
def getURL(fname, parameters):
    base_url = "https://www.alphavantage.co/query?"
    func_parameter = f"function={fname}"

    return f'{base_url}{func_parameter}{parameters}&apikey=685BEOWCXWU9D3ZI'

# function get ticker from user
def get_ticker(ticker_list):
    ticker_select = ""

    if not ticker_list:
        user_input = input("Enter your search")
        search_params = f"&keywords={user_input}"

        try:
            search_url = getURL(function_names['SYMBOL_SEARCH'], search_params)

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

        ticker_data_df.rename(columns={
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