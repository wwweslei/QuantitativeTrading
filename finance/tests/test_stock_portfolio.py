import pytest

from finance.account.stockPortfolio import StockPortfolio


@pytest.fixture(scope='module')
def setUp():
    """
    This function is executed before each test.
    """
    portfolio = StockPortfolio()
    portfolio.add_stock(stock_symbol='petr4',
                        stock_country='brazil',
                        purchase_date='03/01/2022',
                        num_of_shares=100,
                        cost_per_share=28.53)
    return portfolio.data
    
    
def test_size_portfolio(setUp):
    """
    This function tests portfolio list size
    """
    assert len(setUp) == 1

def test_symbol_is_correct_in_portfolio(setUp):
    """
    This function tests if the symbol is in the portfolio.
    """
    assert 'petr4' in setUp['stock_symbol'].values


def test_stock_name_is_correct_in_portfolio(setUp):
    """
    This function tests if the symbol is in the portfolio.
    """
    assert 'PETROBRAS PN' in setUp['stock_name'].values


def test_country_is_correct_in_portfolio(setUp):
    """
    This function tests if the country is in the portfolio.
    """
    assert 'brazil' in setUp['stock_country'].values


def test_stock_currency_is_correct_in_portfolio(setUp):
    """
    This function tests if the stock currency is in the portfolio.
    """
    assert 'BRL' in setUp['stock_currency'].values


def test_purchase_date_is_correct_in_portfolio(setUp):
    """
    This function tests if the purchase date is in the portfolio.
    """
    assert '03/01/2022' in setUp['purchase_date'].values




def test_total_dividends_is_correct_in_portfolio(setUp):
    """
    This function tests if the total dividends is in the portfolio.
    """
    assert  setUp['total_dividends'].values > 660.0




