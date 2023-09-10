from datetime import date
from multiprocessing import Pool

import pyettj.ettj as ettj
from dateutil.relativedelta import relativedelta

from finance.research.tools import get_connection

today = date.today()


def working_day(date):
    """Return the working day of the date passed as argument."""
    if date.weekday() == 5:
        date += relativedelta(days=-1)
        return date
    elif date.weekday() == 6:
        date += relativedelta(days=-2)
        return date
    else:
        return date


def last_day_working(_date):
    """Return the last working day of the month of the date passed as
    argument."""
    _date = working_day(_date)
    _date += relativedelta(days=-1)
    return working_day(_date)


# FIX: This function is not working properly.
# day is out of range for month in day 1


def first_day_of_week(_date):
    """Return the first day of the week of the date passed as argument."""
    _date = _date - relativedelta(day=_date.day - _date.weekday())
    return _date


def fist_day_of_month(_date):
    """Return the first day of the month of the date passed as argument."""
    _date = _date + relativedelta(day=1)
    return working_day(_date)


def get_ettj(_date, name):
    """Return ettj dataframe."""
    _date = _date.strftime("%d-%m-%Y")
    df = ettj.get_ettj(_date)[["DI x pré 252", "DI x pré 360", "Dias Corridos", "Data"]]
    df.columns = ["pre_252", "pre_360", "days", "date"]
    df.to_sql(name, get_connection(), if_exists="replace", index=True)


def save():
    args = [
        (working_day(today), "ettj_day"),
        (last_day_working(today), "last_ettj"),
        (first_day_of_week(today), "ettj_week"),
        (fist_day_of_month(today), "ettj_month"),
    ]
    with Pool(4) as p:
        p.starmap(get_ettj, args)
