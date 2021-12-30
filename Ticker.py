import numpy as np
import pandas as pd
from pandas_datareader.data import DataReader
import requests_cache

class Ticker:
    def __init__(self,ticker,start_date,end_date):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.data = self.get_stocks_data(ticker,start_date,end_date)
        self.price = self.data['Adj Close'].reset_index()

    def get_price_data(self):
        df = self.price
        df['Percentage Change'] = ((df['Adj Close'] / df['Adj Close'].shift(1))-1)*100
        return self.price.rename(columns = {"Adj Close" : "Price"})

    @staticmethod
    def get_stocks_data(ticker, start_date, end_date):
        session = requests_cache.CachedSession(cache_name='cache', backend='sqlite')

        # just add headers to your session and provide it to the reader
        session.headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',
                           'Accept': 'application/json;charset=utf-8'}
        '''
        Function that uses Pandas DataReader to download data directly from Yahoo Finance,
        computes the Log Returns series for each ticker, and returns a DataFrame
        containing the Log Returns of all specified tickers.

        Parameters:
        - tickers (list): List of Stock Tickers.
        - start_date, end_date (str): Start and end dates in the format 'YYYY-MM-DD'.

        Returns:
        - returns_df (pd.DataFrame): A DataFrame with dates as indexes, and columns corresponding
                                     to the log returns series of each ticker.
        '''

        # initialise output dataframe
        returns_df = pd.DataFrame()

        # retrieve stock data (includes Date, OHLC, Volume, Adjusted Close)
        s = DataReader(ticker, 'yahoo', start_date, end_date, session=session)
        # calculate log returns
        s['Log Returns'] = np.log(s['Adj Close'] / s['Adj Close'].shift(1))

        """
        # append to returns_df
        returns_df[ticker] = s['Log Returns']

        # skip the first row (that will be NA)
        # and fill other NA values by 0 in case there are trading halts on specific days
        returns_df = returns_df.iloc[1:].fillna(0)
        """

        return s
