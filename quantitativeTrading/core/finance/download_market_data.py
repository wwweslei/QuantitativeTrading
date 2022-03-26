from re import S
import yfinance as yf
import sqlite3
from django.conf import settings
import os
import pandas as pd
import investpy as inv

os.environ[
    "DJANGO_SETTINGS_MODULE"
] = "quantitativeTrading.quantitativeTrading.settings"


def get_stocks_br():
    stocks_br = inv.get_stocks("brazil")
    stocks_br = stocks_br[["symbol", "name", "full_name", "isin"]]
    stocks_br.to_sql("stocks_br", conn, if_exists="replace", index=False)


def get_stocks_ibov():
    url = "http://bvmf.bmfbovespa.com.br/indices/ResumoCarteiraTeorica.aspx?Indice=IBOV&amp;idioma=pt-br"
    html = pd.read_html(url, decimal=",", thousands=".")[0][:-1]
    df = html.copy()[["Código", "Ação", "Tipo", "Qtde. Teórica", "Part. (%)"]]
    df.rename(
        columns={
            "Código": "symbol",
            "Ação": "name",
            "Tipo": "type",
            "Qtde. Teórica": "quantity",
            "Part. (%)": "percentage",
        },
        inplace=True,
    )
    df.to_sql("stocks_ibov", conn, if_exists="replace", index=False)


conn = sqlite3.connect(settings.DATABASES["default"]["NAME"])
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
    df.to_sql(name, conn, if_exists="replace")


def save():
    for name in tickers:
        update(name)
        print("updated", name)


if __name__ == "__main__":
    # save()
    # get_ibovespa_composition()
    # print(get_stocks_list_ibov())
    get_stocks_br()
