import pandas as pd

from finance.research.tools import get_connection


def save():
    """get all the assets contained in the IFIX index and save it in the
    database."""
    url = (
        "https://www2.bmfbovespa.com.br/Fundos-Listados/"
        "FundosListados.aspx?tipoFundo=imobiliario&Idioma=pt-br"
    )
    df = pd.read_html(url, decimal=",", thousands=".")[0]
    df = df[["Código", "Fundo", "Razão Social"]]
    df.columns = ["symbol", "name", "full_name"]
    df["symbol"] = df["symbol"] + "11"
    df.to_sql("FII_LIST", get_connection(), if_exists="replace", index=False)
    print("updated: FII_LIST")
