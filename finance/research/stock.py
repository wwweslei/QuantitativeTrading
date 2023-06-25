import investpy as inv

from finance.research.tools import get_conn

CONN = get_conn()


def save() -> None:
    """get Dataframe containing all Ibovespa assets and save in database."""
    stocks_br = inv.get_stocks("brazil")
    stocks_br = stocks_br[["symbol", "name", "full_name", "isin"]]
    stocks_br.to_sql("STOCK_LIST", CONN, if_exists="replace", index=False)
    print("updated: STOCK_LIST")


def get_stocks_overview() -> None:
    """get Dataframe containing overview all Ibovespa assets and save in
    database."""
    df = inv.get_stocks_overview("brazil", n_results=400)
    df["change_percentage"] = df["change_percentage"].str.replace("%", "").astype(float)
    df.to_sql("stocks_overview", CONN, if_exists="replace", index=False)
