import shutil

import pandas as pd
from selenium.webdriver.common.by import By

from finance.research.tools import DOWNLOAD_DIR, get_connection, get_webdriver


def get_index() -> pd.DataFrame:
    """open browser and download index.

    Args:
        index (pd.dataframe): dataframe with index name.
    """
    driver = get_webdriver()
    driver.get("https://sistemaswebb3-listados.b3.com.br/fundsPage/20")
    driver.implicitly_wait(1)
    driver.find_element(
        By.LINK_TEXT, "Exportar lista completa de Fundos em CSV"
    ).click()
    driver.quit()
    print("Downloading etfs list")


def save() -> None:
    """Save csv to database.

    Args:
        file (str): read csv and save to database.
    """
    get_index()
    CONN = get_connection()
    df = pd.read_csv(
        f"{DOWNLOAD_DIR}/fundosListados.csv",
        sep=";",
        encoding="iso-8859-1",
        engine="python",
        index_col=False,
    )
    df["Código"] = df["Código"] + "11"
    df.to_sql("ETF_LIST", CONN, if_exists="replace", index=False)
    print("Update ETF_LIST")
    shutil.rmtree(f"{DOWNLOAD_DIR}/")


if __name__ == "__main__":
    get_index()
    # save()
