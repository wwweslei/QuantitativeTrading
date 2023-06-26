import os
from pathlib import Path

from sqlalchemy import inspect

from finance.research import index_b3
from finance.research.tools import DOWNLOAD_DIR, get_connection


def setup_module():
    """setup for module."""
    index_b3.get_index("IBOV")


def test_if_file_env_exists():
    assert os.path.isfile(".env")


def test_connection():
    assert get_connection()


def test_webdriver_firefox_and_config():
    assert index_b3.get_webdriver()


def test_get_index_create_download_dir():
    assert Path(DOWNLOAD_DIR).is_dir()


def test_get_index_have_csv_file():
    csv = os.listdir(DOWNLOAD_DIR)[0]
    assert csv.endswith(".csv")


def test_db_table_exists():
    assert "IBOV" in inspect(get_connection()).get_table_names()
