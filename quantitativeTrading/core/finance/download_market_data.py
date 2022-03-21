from socket import if_nameindex
from black import main
import yfinance as yf
import sqlite3
from django.conf import settings
import os


os.environ[
    "DJANGO_SETTINGS_MODULE"
] = "quantitativeTrading.quantitativeTrading.settings"

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
    save()
