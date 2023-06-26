import pandas as pd

from finance.research.tools import get_connection


def treasury():
    """get Dataframe containing all Ibovespa."""
    url = "https://www.tesourotransparente.gov.br/ckan/dataset/df56aa42-484a-4a59-8184-7676580c81e3/resource/796d2059-14e9-44e3-80c9-2d9e30b405c1/download/PrecoTaxaTesouroDireto.csv"
    df = pd.read_csv(url, sep=";", decimal=",")
    df["Data Vencimento"] = pd.to_datetime(df["Data Vencimento"], dayfirst=True)
    df["Data Base"] = pd.to_datetime(df["Data Base"], dayfirst=True)
    multi_indice = pd.MultiIndex.from_frame(df.iloc[:, :3])
    df = df.set_index(multi_indice).iloc[:, 3:]
    df.sort_index(inplace=True)
    return df


def treasure_sales_search():
    url = "https://www.tesourotransparente.gov.br/ckan/dataset/f0468ecc-ae97-4287-89c2-6d8139fb4343/resource/e5f90e3a-8f8d-4895-9c56-4bb2f7877920/download/VendasTesouroDireto.csv"
    df = pd.read_csv(url, sep=";", decimal=",")
    df["Vencimento do Titulo"] = pd.to_datetime(
        df["Vencimento do Titulo"], dayfirst=True
    )
    df["Data Venda"] = pd.to_datetime(df["Data Venda"], dayfirst=True)
    multi_indice = pd.MultiIndex.from_frame(df.iloc[:, :3])
    df = df.set_index(multi_indice).iloc[:, 3:]
    return df


def treasure_repurchase_search():
    url = "https://www.tesourotransparente.gov.br/ckan/dataset/f30db6e4-6123-416c-b094-be8dfc823601/resource/30c2b3f5-6edd-499a-8514-062bfda0f61a/download/RecomprasTesouroDireto.csv"
    df = pd.read_csv(url, sep=";", decimal=",")
    df["Vencimento do Titulo"] = pd.to_datetime(
        df["Vencimento do Titulo"], dayfirst=True
    )
    df["Data Resgate"] = pd.to_datetime(df["Data Resgate"], dayfirst=True)
    multi_indice = pd.MultiIndex.from_frame(df.iloc[:, :3])
    df = df.set_index(multi_indice).iloc[:, 3:]
    return df


def save():
    all_treasury = treasury()
    treasury_types = (
        all_treasury.index.droplevel(level=1)
        .droplevel(level=1)
        .drop_duplicates()
        .to_list()
    )
    for treasury_type in treasury_types:
        unique_treasury = all_treasury.loc[(treasury_type)].reset_index()
        unique_treasury["Data Base"] = unique_treasury["Data Base"].dt.date
        unique_treasury["Data Vencimento"] = unique_treasury["Data Vencimento"].dt.date
        unique_treasury.to_sql(
            treasury_type, get_connection(), if_exists="replace", index=False
        )


if __name__ == "__main__":
    save()  # save all csv to database in parallel.
