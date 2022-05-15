import pytest

from finance.account.stockPortfolio import StockPortfolio


def test_stock_portfolio_error_stock_symbol():
    """test is True introduced stock_symbol is mandatory and should be a str. 
    """
    portfolio = StockPortfolio()
    with pytest.raises(ValueError):
            portfolio.add_stock(stock_symbol=['error'],
                        stock_country='brazil',
                        purchase_date='03/01/2022',
                        num_of_shares=100,
                        cost_per_share=28.53)


def test_stock_portfolio_error_stock_country():
    """test is True introduced stock_country is mandatory and should be a str. 
    """
    portfolio = StockPortfolio()
    with pytest.raises(ValueError):
            portfolio.add_stock(stock_symbol='petr4',
                        stock_country=['error'],
                        purchase_date='03/01/2022',
                        num_of_shares=100,
                        cost_per_share=28.53)


def test_stock_portfolio_error_formatted_purchase_date():
    """test the introduced purchase_date is not properly formatted
    """
    portfolio = StockPortfolio()
    with pytest.raises(ValueError):
            portfolio.add_stock(stock_symbol='petr4',
                        stock_country='brazil',
                        purchase_date='error',
                        num_of_shares=100,
                        cost_per_share=28.53)


def test_stock_portfolio_error_purchase_date_earlier_or_Equal_today():
    """test introduced purchase_date is not valid since it should be earlier than "
                "the current date"""
    portfolio = StockPortfolio()
    with pytest.raises(ValueError):
            portfolio.add_stock(stock_symbol='petr4',
                        stock_country='brazil',
                        purchase_date='04/01/2050',
                        num_of_shares=100,
                        cost_per_share=28.53)


def test_stock_portfolio_error_num_of_shares_is_int():
    """The introduced num_of_shares is mandatory and should be an int
    """
    portfolio = StockPortfolio()
    with pytest.raises(ValueError):
            portfolio.add_stock(stock_symbol='petr4',
                        stock_country='brazil',
                        purchase_date='03/01/2022',
                        num_of_shares='error',
                        cost_per_share=28.53)

                        
def test_stock_portfolio_error_num_of_shares_is_higher_0():
    """test introduced num_of_shares is mandatory and should be an int higher "
                "than 0. 
    """
    portfolio = StockPortfolio()
    with pytest.raises(ValueError):
            portfolio.add_stock(stock_symbol='petr4',
                        stock_country='brazil',
                        purchase_date='03/01/2022',
                        num_of_shares=-7,
                        cost_per_share=28.53)


def test_stock_portfolio_error_cost_per_share_is_float():
    """test introduced cost_per_share is mandatory and should be a float 
    """
    portfolio = StockPortfolio()
    with pytest.raises(ValueError):
            portfolio.add_stock(stock_symbol='petr4',
                        stock_country='brazil',
                        purchase_date='03/01/2022',
                        num_of_shares=100,
                        cost_per_share='error')




def test_stock_portfolio_error_cost_per_share_is_higher_0():
    """test introduced cost_per_share is mandatory and should be a float higher "
                "than 0." 
    """
    portfolio = StockPortfolio()
    with pytest.raises(ValueError):
            portfolio.add_stock(stock_symbol='petr4',
                        stock_country='brazil',
                        purchase_date='03/01/2022',
                        num_of_shares=100,
                        cost_per_share=-7)


def test_stock_portfolio_error_purchase_date_is_not_valid():
    """test introduced purchase_date is not valid since the market was "
                        "closed." 
    """
    portfolio = StockPortfolio()
    with pytest.raises(KeyError):
            portfolio.add_stock(stock_symbol='petr4',
                        stock_country='brazil',
                        purchase_date='01/01/2022',
                        num_of_shares=100,
                        cost_per_share=28.53)



def test_stock_portfolio_error_value_is_not_possible():
    """The introduced value is not possible, 
    """
    portfolio = StockPortfolio()
    with pytest.raises(KeyError):
            portfolio.add_stock(stock_symbol='petr4',
                        stock_country='brazil',
                        purchase_date='01/01/2022',
                        num_of_shares=100,
                        cost_per_share=98.53)


def test_stock_portfolio_error_stock_symbol_no_the_specified_stock_country():
    """test No results were found for the introduced stock_symbol in the specified "
                    "stock_country." 
    """
    portfolio = StockPortfolio()
    with pytest.raises(ValueError):
            portfolio.add_stock(stock_symbol='petr4',
                        stock_country='russia',
                        purchase_date='01/01/2022',
                        num_of_shares=100,
                        cost_per_share=98.53)


def test_stock_portfolio_error_stock_country_no_indexed():
    """introduced stock_country is not valid or does not have any indexed. 
    """
    portfolio = StockPortfolio()
    with pytest.raises(ValueError):
            portfolio.add_stock(stock_symbol='pppp4',
                        stock_country='brazil',
                        purchase_date='01/01/2022',
                        num_of_shares=100,
                        cost_per_share=98.53)