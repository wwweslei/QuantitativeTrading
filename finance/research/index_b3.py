import os
import shutil
from multiprocessing import Pool

import pandas as pd
from selenium.webdriver.common.by import By

from finance.research.tools import DOWNLOAD_DIR, get_conn, get_webdriver, save_ticker

indexes = [
    "IBOV",  # indice ibovespa",
    "IBXX",  # indice iBrX 100",
    "IBXL",  # indice iBrX 50",
    "IBRA",  # indice brasil amplo",
    "IFNC",  # indice financeiro",
    "ICON",  # indice de consumo",
    "IEEX",  # indice de energia eletrica",
    "IFIX",  # indice de fundos imobiliarios",
    "IFIL",  # indice de fundos imobiliarios de alta liquidez",
    "IMAT",  # indice de materiais basicos",
    "IDIV",  # indice de dividendos",
    "INDX",  # indice do setor industrial",
    "IMOB",  # indice imobiliario",
    "MLCX",  # indice mid-large cap",
    "SMLL",  # indice small cap",
    "UTIL",  # indice de utilidade publica",
    "IVBX",  # indice valor",
    "ICO2",  # indice carbono eficiente",
    "IGCT",  # indice governanca corporativa trade",
    "IGCX",  # indice governanca corporativa",
    "IGNM",  # indice de governanca corporativa novo mercado",
    "ITAG",  # indice de governanca corporativa tag along diferenciado",
]
tickers = {
    "BVSP": "^BVSP",
    "SP500": "^GSPC",
    "NASDAQ": "^IXIC",
    "USD": "USDBRL=X",
    "BTC": "BTC-USD",
    "SMAL11": "SMAL11.SA",
    "XFIX11": "XFIX11.SA",
}


def get_index(index: str) -> pd.DataFrame:
    """open browser and download index.

    Args:
        index (pd.dataframe): dataframe with index name.
    """
    URL = f"https://sistemaswebb3-listados.b3.com.br/indexPage/day/{index}?language=pt-br"
    driver = get_webdriver()
    driver.get(URL)
    driver.find_element(By.ID, "segment").send_keys("Setor de Atuação")
    driver.implicitly_wait(1)
    driver.find_element(By.LINK_TEXT, "Download").click()
    driver.quit()
    print(f"Downloading {index} index")


def download_index():
    """Download all indexes in parallel."""
    with Pool(10) as p:
        p.map(get_index, indexes)


def csv_to_database(file: str) -> None:
    """Save csv to database.
    Args:
        file (str): read csv and save to database.
    """
    CONN = get_conn()
    df = pd.read_csv(
        f"{DOWNLOAD_DIR}/{file}",
        sep=";",
        encoding="iso-8859-1",
        skipfooter=2,
        engine="python",
        thousands=".",
        decimal=",",
        header=1,
        index_col=False,
    )
    df.to_sql(file[:4], CONN, if_exists="replace", index=False)


def save_tickers():
    """Save tickers to database."""
    for ticker in tickers:
        save_ticker(tickers[ticker], ticker)


def save():
    save_tickers()
    download_index()
    """Save all csv to database in parallel."""
    with Pool(10) as p:
        p.map(csv_to_database, os.listdir(DOWNLOAD_DIR))
        shutil.rmtree(f"{DOWNLOAD_DIR}/")


if __name__ == "__main__":
    save()
