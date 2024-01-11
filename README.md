# STOCK ANALYSIS

### Project Details

Stock dataset is not a complex dataset with respect to content and amount, actually it is just 2 things that is needed datetime and price, but analyzing the price is the critical part and helps to put our money on risk free and profitable stocks. It is not an overnight trick, it takes lot and lots of analysis to understand the trends, markets, and other factors. But there is always an unexpected factors which can impact adversely. We just need to understand we can analyze and invest our money on the historical data under known normal factors. 

With this in mind, let us analyze the top tech stocks that have been ruling investment portfolios for many. Previously known as FAANG, these are the top stocks from decades. With many rebranding and name changes, here are six stocks that has been analyzed in this project, 

META - Meta Companies  
AAPL - Apple  
AMZN - Amazon  
NFLX - Netflix  
GOOG and GOOGL - Alphabet Inc.,  

### Presentation

You can find a presentation explaining our project [here](https://docs.google.com/presentation/d/1U0djHwwD6WavXWna53xNfx54ahi5zLCSaJJjr2dhFJ0/edit?usp=sharing)

### Data Source

Data used in this project is from [Alphavantage](https://www.alphavantage.co/). We do have functions to download data in realtime and store them as CSV to further use it. Since there is a 25 requests limit on API Calls. Below are some of the Endpoints used in this project, you can refer to [documentation](https://www.alphavantage.co/documentation/) on how this Endpoints are used. 

```
TIME_SERIES_DAILY  
SYMBOL_SEARCH  
DIGITAL_CURRENCY_DAILY  
EARNINGS  
EARNINGS_CALENDAR
OVERVIEW  
```

### Data Analysis

#### Time Series

Important analysis for a stock is time series, analyzing historical data, trends and any major changes. Reasons for any major changes or frequent changes. All these helps to predict or at least undetstand the stock over a period of time. 

Time series of price and volume since IPO: 

![AAPL volume since IPO](https://github.com/itsakcode/stock_analysis/assets/93089647/ee37c836-374a-4f76-bab2-e2c880b50d8d)
![AAPL price since IPO](https://github.com/itsakcode/stock_analysis/assets/93089647/43e2624a-2cab-427a-8083-5cc99faf34d2)
![META volume since IPO](https://github.com/itsakcode/stock_analysis/assets/93089647/e38509e8-933a-40ad-976f-8085eddb2d3a)
![META price since IPO](https://github.com/itsakcode/stock_analysis/assets/93089647/738e33b0-5820-43ee-a041-6f016b3ea898)

Time series of price and volume by hour: 

![Avg  Stock Price   Volume at Diff  Time of Day (All Stocks)](https://github.com/itsakcode/stock_analysis/assets/93089647/5509b96f-c7ff-4b60-adbc-d96db85bea10)
![Avg  Price Variation at Diff  Time of Day (All Stocks)](https://github.com/itsakcode/stock_analysis/assets/93089647/79013267-9b12-4187-9079-fe1559c77807)


#### Moving Averages

Moving average is the another frequent and widely used analysis to see the stock price trend. 50 days moving average is one of the most used data analysis. 
It is the average of closing price for a certain number of days from current day. This helps to see the trend of the stock if it is bullish or bearish and also support and resistance level of the price. More details in the project. 

![MA_All](https://github.com/itsakcode/stock_analysis/assets/93089647/9067f16d-c22c-47c2-8474-e87260ec7979)


#### Statistical Analysis

Statistical analysis is to understand what are the mean, median and standard deviation of closing price. 

![Stats](https://github.com/itsakcode/stock_analysis/assets/93089647/2ebe5c40-2e41-4127-a857-bde3f60be79f)


Correlation

The stocks we are analyzing in this project are all technology based. So have attempted to see relation between these and see if each have any inter-dependency or correlation.

![Corr_heatmap](https://github.com/itsakcode/stock_analysis/assets/93089647/75c5a32e-ac54-46e4-aa6e-dc593e30056b)

#### Earnings

Analyzing earnings another key factor, which determines how the companies are performing and how they are providing dividend per share. This helps to determine how strong the companies business is and strong growth. 

![image](https://github.com/itsakcode/stock_analysis/assets/93089647/a072637a-a3de-492a-aea1-14d692c71040)


#### Company Overview

Company overview has more details on finance, performance and so on. Mostly focused on Market Cap and Number of Outstanding shares to analyze how much money and volume is shared between these companies. 


![image](https://github.com/itsakcode/stock_analysis/assets/93089647/4d5ee853-8e1d-479f-baf8-f34ede2b7a56)
![image](https://github.com/itsakcode/stock_analysis/assets/93089647/52498583-e8c4-43c8-8ba8-b2d1b213aa16)


Details of all analysis is in the notebook. 

### Execution and Installations

You can use the project package to execute the stock_market jupiter notebook for your analysis. 

Pre-requisite: Need to make sure you have Matplotlib and MPLFinance modules installed for timeseries/other and candlestick charts. 

From Conda Environment run below commands, 

```conda install mplfinance```  
```conda install matplotlib```  

From Python use below commands, 

```pip install mplfinance```  
```pip install -U matplotlib```  

If you want to extract realtime data from an API, we do have option for that and you need to update your API key in environment file under Resources. Replace demo with your API Key.

```alphavantage_api_key="demo"```  

### Future Enhancements

This data analysis project can be enhanced as an application and make it more user interactive and analyze and create visuals and charts based on user selection. This helps users to analyze their desired stock and make a decision on how to proceed with their trade. Also, can investigate on more visuals with data that can impact stock market like interest rate, economy, inflation and so on.
