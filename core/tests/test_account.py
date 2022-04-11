import numpy
import pandas as pd
import sys

from core.finance import account
from django.test import TestCase


class AccounTest(TestCase):
    def setUp(self):
        pass

    def test_python_version(self):
        self.assertTupleEqual(
            sys.version_info[0:3], (3, 10, 2), "Python version is not 3.10.2"
        )

    def test_read_excel_return_is_dataFrame(self):
        file = account._read_excel(account.EXCEL_FILE_NAME)
        self.assertEqual(type(file), pd.DataFrame, "The file is not a dataframe")

    def test_read_excel_not_empty_file(self):
        file = account._read_excel(account.EXCEL_FILE_NAME)
        self.assertFalse(file.empty, "The file is empty")

    def test_clear_dataFrame_not_empty_file(self):
        file = account._read_excel(account.EXCEL_FILE_NAME)
        file = account._clear_dataFrame(file)
        self.assertFalse(file.empty, "The file is empty")

    def test_clear_dataFrame_return_is_dataFrame(self):
        file = account._read_excel(account.EXCEL_FILE_NAME)
        file = account._clear_dataFrame(file)
        self.assertEqual(type(file), pd.DataFrame, "The file is not a dataframe")

    def test_clear_dataFrame_return_is_dataFrame_with_correct_columns(self):
        file = account._read_excel(account.EXCEL_FILE_NAME)
        file = account._clear_dataFrame(file)
        self.assertEqual(
            set(file.columns),
            set(
                [
                    "Ticket",
                    "Price",
                    "Buy",
                    "Sell",
                    "Financial Buy",
                    "Financial Sell",
                    "Qtd",
                ]
            ),
            "The columns are not correct",
        )

    def test_clear_dataFrame_return_is_dataFrame_with_correct_index(self):
        file = account._read_excel(account.EXCEL_FILE_NAME)
        file = account._clear_dataFrame(file)
        self.assertEqual(
            set(file.index.names), set(["Data"]), "The index is not correct"
        )

    def test_full_business_not_empty_file(self):
        file = account.get_full_business()
        self.assertFalse(file.empty, "The file is empty")

    def test_full_business_return_is_dataFrame(self):
        file = account.get_full_business()
        self.assertEqual(type(file), pd.DataFrame, "The file is not a dataframe")

    def test_full_business_return_is_dataFrame_with_correct_columns(self):
        file = account.get_full_business()
        self.assertEqual(
            set(file.columns),
            set(
                [
                    "Ticket",
                    "Price",
                    "Buy",
                    "Sell",
                    "Financial Buy",
                    "Financial Sell",
                    "Qtd",
                ]
            ),
            "The columns are not correct",
        )

    def test_full_business_return_is_dataFrame_with_correct_index(self):
        file = account.get_full_business()
        self.assertEqual(
            set(file.index.names), set(["Data"]), "The index is not correct"
        )

    def test_get_simple_portfolio_not_empty_file(self):
        file = account.get_simple_portfolio()
        self.assertFalse(file.empty, "The file is empty")

    def test_get_simple_portfolio_return_is_Series(self):
        file = account.get_simple_portfolio()
        self.assertEqual(type(file), pd.Series, "The file is not a Series")

    def test_get_simple_portfolio_return_type_is_int(self):
        file = account.get_simple_portfolio()
        self.assertEqual(
            type(file.iloc[0]), numpy.int64, "The file is not a numpy.int64"
        )

    def test_individual_information_return_is_DataFrame(self):
        file = account.get_individual_information("PETR4")
        self.assertEqual(type(file), pd.DataFrame, "The file is not a DataFrame")

    def test_individual_information_return_is_DataFrame_with_correct_index(self):
        file = account.get_individual_information("PETR4")
        self.assertEqual(
            set(file.index.names), set(["Data"]), "The index is not correct"
        )

    def test_get_full_portfolio_not_empty_file(self):
        file = account.get_portfolio()
        assert not file.empty, "The file is empty"

    def test_get_full_portfolio_return_is_DataFrame(self):
        file = account.get_portfolio()
        self.assertEqual(type(file), pd.DataFrame, "The file is not a DataFrame")

    def test_get_full_portfolio_return_is_DataFrame_with_correct_columns(self):
        file = account.get_portfolio()
        self.assertEqual(
            set(file.columns),
            set(["Ticket", "Average Value", "Financial Buy", "Qtd"]),
            "The columns are not correct",
        )

    def test_get_full_portfolio_return_is_DataFrame_with_correct_index(self):
        file = account.get_portfolio()
        self.assertEqual(
            set(file.index.names), set(["Data"]), "The index is not correct"
        )