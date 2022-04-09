import yfinance as yf
import pandas as pd
import investpy as inv
from sqlalchemy import create_engine
from decouple import config


ENVIRONMENT = config("ENVIRONMENT")

if ENVIRONMENT == "development":
    url = config("DATABASE_URL").replace("postgres://", "postgresql://")
else:
    url = config("DATABASE_URL_HEROKU").replace("postgres://", "postgresql://")
conn = create_engine(url)


def get_stocks_br():
    stocks_br = inv.get_stocks("brazil")
    stocks_br = stocks_br[["symbol", "name", "full_name", "isin"]]
    stocks_br.to_sql("stocks_br", conn, if_exists="replace", index=False)
    print("updated: get_stocks_br")


def get_stocks_ibov():
    url = "http://bvmf.bmfbovespa.com.br/indices/ResumoCarteiraTeorica.aspx?Indice=IBOV&amp;idioma=pt-br"
    html = pd.read_html(url, decimal=",", thousands=".")[0][:-1]
    df = html.copy()[["Código", "Ação", "Tipo", "Qtde. Teórica", "Part. (%)"]]
    df.columns = ["symbol", "name", "type", "quantity", "percentage"]
    df.to_sql("stocks_ibov", conn, if_exists="replace", index=False)
    print("updated: get_stocks_ibov")


def get_fiis():
    url = "https://www2.bmfbovespa.com.br/Fundos-Listados/FundosListados.aspx?tipoFundo=imobiliario&Idioma=pt-br"
    df = pd.read_html(url, decimal=",", thousands=".")[0][:-1]
    df = df[["Código", "Fundo", "Razão Social"]]
    df.columns = ["symbol", "name", "full_name"]
    df["symbol"] = df["symbol"] + "11"
    df.to_sql("fiis", conn, if_exists="replace", index=False)
    print("updated: get_fiis")


def get_stocks_fii():
    url = "https://sistemaswebb3-listados.b3.com.br/indexPage/day/IFIX?language=pt-br"
    html = pd.read_html(url)
    print(html)
    # df.to_sql("stocks_ibov", conn, if_exists="replace",flavor='postgresql',  index=False)
    print("updated: get_stocks_fii")


tickers = {
    "dollar": "USDBRL=X",
    "ibovespa": "^BVSP",
    "bitcoin": "BTC-USD",
    "smal": "SMAL11.SA",
    "sp_500": "^GSPC",
    "xfix": "XFIX11.SA",
    "nasdaq": "^IXIC",
}


def update(name):
    data = yf.Ticker(tickers[name])
    df = data.history(period="max")
    df.columns = df.columns.str.lower()
    df.index.rename("date", inplace=True)
    df = df.iloc[::-1]
    if ENVIRONMENT == "development":
        df.to_sql(name, conn, if_exists="replace")
    else:
        df = df.tail(10)
        df.to_sql(name, conn, if_exists="replace")


def save():
    print(f"saving in environment: {ENVIRONMENT}")
    for name in tickers:
        update(name)
        print("updated:", name)


def run_all():
    save()
    get_stocks_br()
    get_stocks_ibov()
    # get_stocks_fii()
    get_fiis()


if __name__ == "__main__":
    # get_stocks_ibov()
    # save()
    # get_stocks_br()
    # get_fiis()
    # get_stocks_fii()
    run_all()
