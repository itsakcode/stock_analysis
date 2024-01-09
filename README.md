# STOCK ANALYSIS

### What is it?

Stock dataset is not a complex dataset with respect to content and amount, actually it is just 2 things that is needed datetime and price, but analyzing the price is the critical part and helps to put our money on risk free and profitable stocks. It is not an overnight trick, it takes lot and lots of analysis to understand the trends, markets, and other factors. But there is always an unexpected factors which can impact adversely. We just need to understand we can analyze and invest our money on the historical data under known normal factors. 

With this in mind, let us analyze the top tech stocks that have been ruling investment portfolios for many. Previously known as FAANG, these are the top stocks from decades. With many rebranding and name changes, here are six stocks that has been analyzed in this project, 

META - Meta Companies  
AAPL - Apple  
AMZN - Amazon  
NFLX - Netflix  
GOOG and GOOGL - Alphabet Inc.,  

### Data Source

Data used in this project is from [Alphavantage](https://www.alphavantage.co/). We do have functions to download data in realtime and store them as CSV to further use it. Since there is a 25 requests limit on API Calls. Below are some of the Endpoints used in this project, you can refer to [documentation](https://www.alphavantage.co/documentation/) on how this Endpoints are used. 

```
TIME_SERIES_DAILY  
SYMBOL_SEARCH  
DIGITAL_CURRENCY_DAILY  
EARNINGS  
EARNINGS_CALENDAR  
```

### Analysis

#### Time Series

Important analysis for a stock is time series, analyzing historical data, trends and any major changes. Reasons for any major changes or frequuent changes. All these helps to predict or at least undetstand the stock over a period of time. 

#### Moving Averages

Moving average is the another frequent and widely used analysis to see the stock price trend. 50 days moving average is one of the most used data. 
It is the average of closing price for a certain number of days from current day. Check the analysis in project to understand more. 

#### Statistical Analysis

Statistical analysis is to understand what are the mean, median and standard deviation of closing price. 

Correlation

The stocks we are analyzing in this project are all technology based. So have attempted to see relation between these and see if each have any inter-dependency or correlation.

### Installations

You can use the project package to execute the stock_market jupiter notebook for your analysis. 

Pre-requisite: Need to make sure you have Matplotlib and MPLFinance modules installed for timeseries/other and candlestick charts. 

From Conda Environment run below commands, 

```conda install mplfinance```  
```conda install matplotlib```  

If you want to extract realtime data from an API, we do have option for that and you need to update your API key in environment file under Resources. Replace demo with your API Key.

```alphavantage_api_key="demo"```  

### Future Enhancements



From Python use below commands, 

```pip install mplfinance```  
```pip install -U matplotlib```  
