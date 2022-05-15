from datetime import date

import investpy
import pandas as pd

from finance.account.stock import Stock


class StockPortfolio(object):
    """StockPortfolio is the main class which is going to manage all the introduced stocks.

    Args:
        object (list): this list contains all the introduced stocks,
        which will later be used to generate the portfolio.

    Raises:
        ValueError: custom error message

    Returns:
        obj (pandas.DataFrame): it is the generated portfolio, once the addition of every stock is validated.
    """

    def __init__(self):
        """This is the init method of StockPortfolio class which is launched every time the user instances it."""
        self._stocks = list()
        self._stock_objs = list()
        self.data = None

    def add_stock(self, stock_symbol, stock_country, purchase_date,
                  num_of_shares, cost_per_share):
        """Method to add a stock to the portfolio.
        Args:
            stock_symbol (str): symbol of the Stock that is going to be added to the StockPortfolio.
            stock_country (str): country from where the specified stock_symbol is, so to validate it.
            purchase_date (str): date when the shares of the introduced stock were bought, formatted as dd/mm/yyyy.
            num_of_shares (int): amount of shares bought of the specified Stock in the specified date.
            cost_per_share (float): price of every share of the Stock in the specified date.

        Raises:
            ValueError: custom error message."""
        stock = Stock(stock_symbol, stock_country, purchase_date,
                      num_of_shares, cost_per_share)
        stock.validate()

        if stock.valid is True:
            self._stock_objs.append(stock)

            info = self.__get_stock_info(stock=stock)

            self._stocks.append(info)
            self.data = pd.DataFrame(self._stocks)
        else:
            raise ValueError(
                "ERROR [0001]: The introduced Stock is not valid.")

    def __get_stock_info(self, stock):
        """Method to get the stock information once it is validated.

        Args:
            stock (obj.Stock): Stock object with all its information after validated.

        Returns:
            obj.dict:which contains all the values from the introduced Stock in order to create its
                portfolio row.
        """
        stocks = investpy.get_stocks(country=stock.stock_country)

        stock_name = stocks.loc[(stocks["symbol"].str.lower() ==
                                 stock.stock_symbol.lower()).idxmax(),
                                "name", ]

        data = investpy.get_stock_historical_data(
            stock=stock.stock_symbol,
            country=stock.stock_country,
            from_date=stock.purchase_date,
            to_date=date.today().strftime("%d/%m/%Y"),
        )

        currency = data["Currency"][0]

        purchase_cost = self.calculate_purchase_cost(
            cost_per_share=stock.cost_per_share,
            num_of_shares=stock.num_of_shares)

        current_price = self.get_current_price(data=data)

        gross_current_value = self.calculate_gross_current_value(
            current_price=current_price, num_of_shares=stock.num_of_shares)

        dividends = investpy.get_stock_dividends(stock=stock.stock_symbol,
                                                 country=stock.stock_country)

        dividends = dividends.loc[dividends["Date"] > pd.to_datetime(
            stock.purchase_date, dayfirst=True)].reset_index(drop=True)

        if len(dividends) > 0:
            total_dividends = self.calculate_total_dividends(
                dividends=dividends, num_of_shares=stock.num_of_shares)
        else:
            total_dividends = 0

        net_current_value = self.calculate_net_current_value(
            gross_current_value=gross_current_value,
            total_dividends=total_dividends)

        total_gain_loss = self.calculate_total_gain_loss(
            net_current_value=net_current_value, purchase_cost=purchase_cost)

        total_gain_loss_percentage = self.calculate_total_gain_loss_percentage(
            total_gain_loss=total_gain_loss, purchase_cost=purchase_cost)

        info = {
            "stock_symbol": stock.stock_symbol,
            "stock_name": stock_name,
            "stock_country": stock.stock_country,
            "stock_currency": currency,
            "purchase_date": stock.purchase_date,
            "num_of_shares": stock.num_of_shares,
            "cost_per_share": stock.cost_per_share,
            "purchase_cost": purchase_cost,
            "current_price": current_price,
            "gross_current_value": gross_current_value,
            "total_dividends": total_dividends,
            "net_current_value": net_current_value,
            "total_gain_loss": total_gain_loss,
            "total_gain_loss_percentage": total_gain_loss_percentage,
        }

        return info

    def refresh(self):
        """Method to refresh/reload the StockPortfolio information."""
        if len(self._stock_objs) > 0:
            self._stocks = list()
            for stock_obj in self._stock_objs:
                info = self.__get_stock_info(stock=stock_obj)
                self._stocks.append(info)
            self.data = pd.DataFrame(self._stocks)

    @staticmethod
    def calculate_purchase_cost(cost_per_share, num_of_shares):
        """This method calculates the purchase cost, which is the paid value for every stock share hold by the user at
        the time that stock shares were bought.
        Returns:
            float: purchase cost
        """
        return float(cost_per_share * num_of_shares)

    @staticmethod
    def get_current_price(data):
        """This method gets the current price value of the introduced stock
        Returns:
            obj.pandas.DataFrame: stock historical data
        """

        return data.iloc[-1]["Close"]

    @staticmethod
    def calculate_gross_current_value(current_price, num_of_shares):
        """This method calculates the gross current value which is the total current value of the shares bought.

        Returns:
            float: result of the multiplication of the current price with the number of bought shares.
        """

        return float(current_price * num_of_shares)

    @staticmethod
    def calculate_total_dividends(dividends, num_of_shares):
        """This method calculates the total dividend's value which is the sum of all the dividends paid in the time
        range that the user owned/owns the stock shares.

        Args:
            dividends (_type_): _description_
            num_of_shares (_type_): _description_

        Returns:
            _type_: total dividend
        """
        total_dividends = 0
        for _, dividend in dividends.iterrows():
            total_dividends += dividend["Dividend"] * num_of_shares
        return total_dividends

    @staticmethod
    def calculate_net_current_value(gross_current_value, total_dividends):
        """ This method calculates the net current value which is the total of the gross current value and the value of
        the dividends, i.e., the total of returns from both capital gains and dividends._summary_

        Args:
            gross_current_value (method): gross current value()
            total_dividends (method): total dividend()

        Returns:
            float: net current value
        """

        return gross_current_value + total_dividends

    @staticmethod
    def calculate_total_gain_loss(net_current_value, purchase_cost):
        """This method calculates the difference between the current value of the stock shares, including the dividends
        received, with the value that the user paid of them.

        Args:
            net_current_value (method): net current value()
            purchase_cost (method): purchase cost()

        Returns:
            float: total difference between the current value of the stock shares         
        """
        return net_current_value - purchase_cost

    @staticmethod
    def calculate_total_gain_loss_percentage(total_gain_loss, purchase_cost):
        """ This method compares the stock total gain loss to what the user paid for the stock shares owned
        Args:
            total_gain_loss (method): calculate_total_gain_loss()
            purchase_cost (method): purchase_cost()

        Returns:
            str: percentage that can show the total stock performance.
        """

        return str(total_gain_loss / purchase_cost) + "%"

    def __len__(self):
        """Method to return the number of stocks in the portfolio."""
        return len(self._stock_objs)

if __name__ == "__main__":
    portfolio = StockPortfolio()
    portfolio.add_stock(stock_symbol='brcr11',
                        stock_country='brazil',
                        purchase_date='04/01/2018',
                        num_of_shares=100,
                        cost_per_share=90.51)
    print(portfolio.data)
