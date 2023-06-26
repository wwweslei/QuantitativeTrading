from multiprocessing import Pool

import pandas as pd

from finance.research.tools import get_connection

# source https://www.bcb.gov.br/estatisticas/indecoreestruturacao
tickers = {
    # Índices de preços
    "INPC": 188,
    "IPCA": 433,
    "IPCA_15": 7478,
    "IGPM": 189,
    # Força de trabalho e população em idade ativa
    "OCUPADAS": 24379,
    "DESOCUPADA": 24380,
    "FORCA_DE_TRABALHO": 24378,
    "POPULACAO_EM_IDADE_ATIVA": 24370,
    "TAXA_DE_DESOCUPACAO": 24369,
    # Rendimento médio real efetivo de todos os trabalhos
    "REMUNERACAO_MEDIA_NOMINAL": 24382,
    "MASSA_SARAIAL": 28544,
    # Produto Interno Bruto e taxas médias de crescimento
    "PIP": 22099,
    "EXPORTACOES": 22103,
    "IMPORTACOES": 22104,
    "AGRONEGOCIO": 22083,
    "INDUSTRIA": 22084,
    "SERVICOS": 22089,
    # Taxas de juros efetivas
    "SELIC": 4189,
    "SELIC_META": 432,
    "CDI": 4392,
    "CDI_OVER": 12,
    "POUPANCA": 196,
    # Reservas internacionais
    "RESEVAS_INTERNACIONAIS": 13621,
    # Taxa de câmbio
    "DOLAR_VENDA": 1,
    "DOLAR_COMPRA": 10813,
    "EURO_VENDA": 21619,
    "EURO_COMPRA": 21620,
    "OURO_VENDA": 4,
    "OURO_COMPRA": 21627,
    # Taxa de câmbio - média
    "DOLAR_VENDA_MEDIA": 21628,
    "DOLAR_COMPRA_MEDIA": 21629,
}


def consulta_bc(codigo_bcb, name):
    url = (
        f"http://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo_bcb}/dados?formato=json"
    )
    df = pd.read_json(url)
    df["data"] = pd.to_datetime(df["data"], dayfirst=True).dt.date
    df.set_index("data", inplace=True)
    df.to_sql(name, get_connection(), if_exists="replace")
    print(f"updated: {name}")


def save() -> None:
    """get Dataframe containing all Ibovespa assets and save in database."""
    args = list(zip(tickers.values(), tickers.keys()))
    with Pool(10) as p:
        p.starmap(consulta_bc, args)
