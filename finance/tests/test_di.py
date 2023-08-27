from datetime import date

import pytest

from finance.research import di

sample_date_working_day = [
    (date(2023, 8, 18), date(2023, 8, 18)),
    (date(2023, 8, 19), date(2023, 8, 18)),
    (date(2023, 8, 20), date(2023, 8, 18)),
    (date(2023, 8, 21), date(2023, 8, 21)),
]


@pytest.mark.parametrize("date_test, expected", sample_date_working_day)
def test_working_day(date_test, expected):
    assert di.working_day(date_test) == expected


sample_date_last_day = [
    (date(2023, 8, 18), date(2023, 8, 17)),
    (date(2023, 8, 19), date(2023, 8, 17)),
    (date(2023, 8, 20), date(2023, 8, 17)),
    (date(2023, 8, 21), date(2023, 8, 18)),
]


@pytest.mark.parametrize("date_test, expected", sample_date_last_day)
def test_last_day_working(date_test, expected):
    assert di.last_day_working(date_test) == expected


sample_date_first_day_of_week = [
    (date(2023, 8, 18), date(2023, 8, 14)),
    (date(2023, 8, 19), date(2023, 8, 14)),
    (date(2023, 8, 20), date(2023, 8, 14)),
    (date(2023, 8, 21), date(2023, 8, 21)),
]


@pytest.mark.parametrize("date_test, expected", sample_date_first_day_of_week)
def test_first_day_of_week(date_test, expected):
    assert di.first_day_of_week(date_test) == expected


sample_date_first_day_of_month = [
    (date(2023, 1, 18), date(2022, 12, 30)),
    (date(2023, 7, 17), date(2023, 6, 30)),
    (date(2023, 8, 20), date(2023, 8, 1)),
    (date(2023, 9, 21), date(2023, 9, 1)),
]


@pytest.mark.parametrize("date_test, expected", sample_date_first_day_of_month)
def test_first_day_of_month(date_test, expected):
    assert di.fist_day_of_month(date_test) == expected
