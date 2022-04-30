from threading import Thread

import investpy as inv
import pandas as pd
import yfinance as yf
from decouple import config
from sqlalchemy import create_engine

ENVIRONMENT = config("ENVIRONMENT")
DATABASE_URL = config("DATABASE_URL").replace("postgres://", "postgresql://")  # type: ignore
CONN = create_engine(DATABASE_URL)


def get_stocks_br() -> None:
    """get Dataframe containing all Ibovespa assets and save in database."""
    stocks_br = inv.get_stocks("brazil")
    stocks_br = stocks_br[["symbol", "name", "full_name", "isin"]]
    stocks_br.to_sql("stocks_br", CONN, if_exists="replace", index=False)
    print("updated: get_stocks_br")


def get_stocks_ibov() -> None:
    """get all the assets contained in the ibovespa index and save it in the database."""
    url = (
        "http://bvmf.bmfbovespa.com.br/indices/"
        "ResumoCarteiraTeorica.aspx?Indice=IBOV&amp;idioma=pt-br"
    )
    html = pd.read_html(url, decimal=",", thousands=".")[0][:-1]
    df = html.copy()[["Código", "Ação", "Tipo", "Qtde. Teórica", "Part. (%)"]]
    df.columns = ["symbol", "name", "type", "quantity", "percentage"]
    df.to_sql("stocks_ibov", CONN, if_exists="replace", index=False)
    print("updated: get_stocks_ibov")


def get_fiis() -> None:
    """get all the assets contained in the IFIX index and save it in the database."""
    url = (
        "https://www2.bmfbovespa.com.br/Fundos-Listados/"
        "FundosListados.aspx?tipoFundo=imobiliario&Idioma=pt-br"
    )
    df = pd.read_html(url, decimal=",", thousands=".")[0][:-1]
    df = df[["Código", "Fundo", "Razão Social"]]
    df.columns = ["symbol", "name", "full_name"]
    df["symbol"] = df["symbol"] + "11"
    df.to_sql("fiis", CONN, if_exists="replace", index=False)
    print("updated: get_fiis")


def get_stocks_overview() -> None:
    """get Dataframe containing overview all Ibovespa assets and save in database."""
    df = inv.get_stocks_overview("brazil", n_results=400)
    df["change_percentage"] = df["change_percentage"].str.replace("%", "").astype(float)
    df.to_sql("stocks_overview", CONN, if_exists="replace", index=False)


tickers = {
    "dollar": "USDBRL=X",
    "ibovespa": "^BVSP",
    "bitcoin": "BTC-USD",
    "smal": "SMAL11.SA",
    "sp_500": "^GSPC",
    "xfix": "XFIX11.SA",
    "nasdaq": "^IXIC",
}


def update(name: str) -> None:
    """Update the data of the ticker in the database.

    Args:
        name (str): name of the ticker.
    """

    data = yf.Ticker(tickers[name])
    df = data.history(period="1mo")
    df.columns = df.columns.str.lower()
    df.index.rename("date", inplace=True)
    df = df.iloc[::-1]
    if ENVIRONMENT == "development":
        df.to_sql(name, CONN, if_exists="replace")
    else:
        df = df.head(2)
        df.to_sql(name, CONN, if_exists="replace")


def save() -> None:
    """save the data the dictionary in the database."""
    print(f"saving in environment: {ENVIRONMENT}")
    for name in tickers:
        Thread(target=update, args=(name,)).start()
        print("updated:", name)


def run_all() -> None:
    """Run all the functions."""
    Thread(target=get_stocks_br).start()
    Thread(target=get_stocks_ibov).start()
    Thread(target=get_fiis).start()
    Thread(target=get_stocks_overview).start()
    Thread(target=save).start()


if __name__ == "__main__":
    run_all()
