from multiprocessing import Pool

import investpy as inv

from finance.research.tools import get_connection, save_ticker

CONN = get_connection()


def save_list() -> None:
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
    print("updated: stocks_overview")


def save() -> None:
    """get Dataframe containing all Ibovespa assets and save in database."""
    tickets = inv.get_stocks("brazil")[["symbol"]]["symbol"]
    args = list(zip(tickets + ".sa", tickets))
    with Pool(3) as p:
        p.starmap(save_ticker, args, chunksize=10)
