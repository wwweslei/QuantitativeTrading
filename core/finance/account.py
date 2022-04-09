import os
import pandas as pd
import numpy as np
from django.conf import settings
from sqlalchemy import create_engine
from decouple import config

url = config("DATABASE_URL").replace("postgres://", "postgresql://")

conn = create_engine(url)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quantitativeTrading.settings")
EXCEL_FILE_NAME = "negociosNUinvest.xlsx"

EXCEL_FOLDER = os.path.join(settings.BASE_DIR, "documents")


def _read_excel(excel_file_name: str) -> pd.DataFrame:
    """
        Read excel file and return a dataframe

    Args:
        excel_file_name (str): name of the excel file
    Returns:
        pd.DataFrame: dataframe with the data from the excel file
    """
    excel_file_path = os.path.join(EXCEL_FOLDER, excel_file_name)
    return pd.read_excel(excel_file_path, index_col=0)


def _clear_dataFrame(dataFrame: pd.DataFrame) -> pd.DataFrame:
    """
        Clear dataframe from unnecessary columns

    Args:
        dataFrame (pd.DataFrame):
        dataframe with the data from the excel file

    Returns:
        pd.DataFrame:
        set index and change names the columns, delete unnecessary columns
        and add a column with Qtd value of the transactions
        and Ticket.
    """
    dataFrame.index.names = ["Data"]
    dataFrame.rename(
        columns={
            "Ativo": "Ticket",
            "Preço": "Price",
            "Quantidade Compra": "Buy",
            "Quantidade Venda": "Sell",
            "Financeiro Compra": "Financial Buy",
            "Financeiro Venda": "Financial Sell",
        },
        inplace=True,
    )
    dataFrame.drop(columns=["Conta"], inplace=True)
    dataFrame["Qtd"] = [
        y * -1 if y != 0 else x * 1 for x, y in zip(dataFrame["Buy"], dataFrame["Sell"])
    ]
    dataFrame["Ticket"] = [x[:-1] if x[-1] == "F" else x for x in dataFrame["Ticket"]]
    return dataFrame


def get_full_business() -> pd.DataFrame:
    """
        Get all the business from the excel file

    Returns:
        pd.DataFrame:
        dataframe with all the business from the excel file
    """
    dataFrame = _read_excel(EXCEL_FILE_NAME)
    return _clear_dataFrame(dataFrame)


def get_simple_portfolio() -> pd.Series:
    """
        Get user portfolio
    Returns:
        pd.Series:
        portfolio containing the names and quantity
        ["Ativo", "Qtd"]
    """
    dataFrame = get_full_business()
    series = dataFrame.groupby("Ticket").sum()
    return series[series["Qtd"] != 0]["Qtd"]


def get_individual_information(ticket: str) -> pd.DataFrame:
    """
        Get information about a specific ticket

    Args:
        ticket (str):
        ticket to get information about

    Returns:
        pd.DataFrame:
        dataframe with the information about the ticket
    """
    dataframe = get_full_business()
    dataframe = dataframe[dataframe["Ticket"] == ticket]
    dataframe["Cumulative_return"] = dataframe["Qtd"].cumsum()
    try:
        f = np.where(dataframe["Cumulative_return"] == 0)[0][-1]
        return dataframe.iloc[f + 1 :]
    except:
        return dataframe


def _clear_individual_information(individual_information: pd.DataFrame) -> pd.DataFrame:
    """
    Clear dataframe from unnecessary columns
    and change the columns

    Args:
        individual_information (pd.DataFrame):
        return from get_individual_information function

    Returns:
        pd.DataFrame:
        dataframe with the information about the ticket
        columns: ["Data", "Ticket", "Average Value", "Financial Value", "Qtd"]
    """
    ativo = {
        "Data": individual_information.index[0],
        "Ticket": individual_information["Ticket"].iloc[0],
        "Average Value": (
            (
                individual_information["Financial Buy"].sum()
                - individual_information["Financial Sell"].sum()
            )
            / individual_information["Qtd"].sum()
        ).round(2),
        "Financial Buy": individual_information["Financial Buy"].sum()
        - individual_information["Financial Sell"].sum(),
        "Qtd": individual_information["Qtd"].sum(),
    }
    return pd.DataFrame(ativo, index=[0]).set_index("Data")


def get_portfolio() -> pd.DataFrame:
    """
        Get complete user portfolio

    Returns:
        pd.DataFrame: complete portfolio
    """
    portfolio = get_simple_portfolio()
    full_portfolio = pd.DataFrame()
    for ticket in portfolio.index:
        full_portfolio = pd.concat(
            [
                full_portfolio,
                _clear_individual_information(get_individual_information(ticket)),
            ]
        )
    return full_portfolio

def save_portfolio(portfolio: pd.DataFrame):
    """
    Save portfolio in database

    Args:
        portfolio (pd.DataFrame):
        portfolio to save
    """
    portfolio["user"] = "1"
    portfolio.columns = ["symbol", "value", "total_value", "qtd", "user_id"]
    portfolio.index.rename("date", inplace=True)
    portfolio.to_sql("portfolio", conn, if_exists="replace")
    
    
if __name__ == "__main__":
    print(save_portfolio(get_portfolio()))
