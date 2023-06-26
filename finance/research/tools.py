from pathlib import Path

import yfinance as yf
from decouple import config
from selenium import webdriver
from sqlalchemy import create_engine
from selenium.webdriver.firefox.options import Options

DOWNLOAD_DIR = str(Path(__file__).resolve().parent.joinpath("data"))


def get_webdriver() -> webdriver:
    """Configure webdriver to download files.

    Returns:
        webdrive: drive selenium firefox.
    """
    options = Options()
    options.set_preference("browser.download.folderList", 2)
    options.set_preference("browser.download.manager.showWhenStarting", False)
    options.set_preference("browser.download.dir", DOWNLOAD_DIR)
    options.set_preference(
        "browser.helperApps.neverAsk.saveToDisk", "application/x-gzip"
    )
    options.add_argument("--headless")
    return webdriver.Firefox(options=options)


def get_connection():
    database_url = config("DATABASE_URL")
    CONN = create_engine(database_url)
    return CONN


def save_ticker(ticket: str, name: str) -> None:
    """Update the data of the ticker in the database.

    Args:
        name (str): name of the ticker.
    """

    data = yf.Ticker(ticket)
    df = data.history(period="5y")
    df.columns = df.columns.str.lower()
    df.index.rename("date", inplace=True)
    df = df.iloc[::-1]
    df.to_sql(name, get_connection(), if_exists="replace")
    print(f"Downloading {name} ticker")
