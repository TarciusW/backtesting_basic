from Ticker import Ticker


class Trader:
    def __init__(self, ticker, portfolio_value, start_date, end_date):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.ticker = Ticker(ticker, start_date, end_date)
        self.price_data = self.ticker.get_price_data()
        self.portfolio_value = portfolio_value
        self.passive_outcome = self.get_passive_investing_outcome(self.price_data,self.portfolio_value)


    @staticmethod
    def get_passive_investing_outcome(price_data,portfolio_value):
        initial_price = price_data['Price'].iloc[0]
        num_of_shares = portfolio_value/ initial_price
        leftover = portfolio_value - (num_of_shares * initial_price)
        final_price = price_data['Price'].iloc[-1]
        return num_of_shares * final_price + leftover
