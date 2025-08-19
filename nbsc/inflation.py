import pandas as pd

from nbsc import request_data

today_year = pd.Timestamp.today().strftime("%Y")


def get_inflation_from_2001() -> pd.Series:
    """
    Request long term monthly inflation time series from 2001 to recent year.
    """
    s_2016 = request_data.load_nbs_web(
        series="A01030101", periods="2016-2020", freq="month"
    )
    s_2001 = request_data.load_nbs_web(
        series="A01030201", periods="2001-2015", freq="month"
    )
    s = pd.concat([s_2016, s_2001], axis=0, join="outer", copy="false")
    s = check_for_zero(s)
    s = (s - 100.0) / 100
    s.index = s.index.to_period("M")
    return s.sort_index(ascending=False)


def get_recent_inflation(first_year: str = "2016") -> pd.Series:
    """
    Request monthly inflation time series (2016+).
    """
    s_2021 = request_data.load_nbs_web( 
        series="A01030G01", periods=f"{first_year}-{today_year}", freq="month"
    )    
    
    s_2021.index = s_2021.index.to_period("M")
    s_2021.sort_index(ascending=False, inplace=True)
    s_2021 = check_for_zero(s_2021)
    return (s_2021 - 100.0) / 100


def get_annual_inflation(first_year: str = "1987") -> pd.Series:
    """
    Request annual inflation monthly time series.

    Inflation is calculated from CPI.
    'A01010201' code - from 1987 to 2015 same month of last year=100)
    'A01010101' code - from 2016 same month of last year=100).

    NBSC official data has zeroes in the CPI history:
    2002-02    0.0
    2001-02    0.0
    2000-10    0.0
    2000-09    0.0
    """
    s_new = request_data.load_nbs_web(
        series="A01010101", periods=f"2016-{today_year}", freq="month"
    )
    if int(first_year) <= 2015:
        s_old = request_data.load_nbs_web(
            series="A01010201", periods=f"{first_year}-2015", freq="month"
        )
    else:
        s_old = pd.Series()
    s = pd.concat([s_old, s_new], axis=0, join="outer", copy="false")
    s.index = s.index.to_period("M")
    s.sort_index(ascending=False, inplace=True)
    s = check_for_zero(s)
    return (s - 100.0) / 100.0


def calculate_monthly_from_annual(last_date: str = "2000-12") -> pd.Series:
    """
    Calculate monthly inflation (1987+) given annual and monthly data.

    This function is used for periods where no official monthly CPI data is available.
    `last_date` should be 2000-12 or later.
    """
    s_annual = get_annual_inflation()
    s_monthly = get_inflation_from_2001()
    if pd.to_datetime(last_date, format="%Y-%m") < pd.to_datetime(
        "2000-12", format="%Y-%m"
    ):
        raise ValueError("last_date should be 2000-12 or later.")
    new_index = pd.period_range("1987-01", last_date, freq="M").sort_values(
        ascending=False
    )
    for date in new_index:
        prod_monthly = (s_monthly[: date + 1].tail(11) + 1.0).prod()
        s_monthly[date] = (s_annual.shift(11)[date] + 1.0) / prod_monthly - 1.0
    return s_monthly.sort_index(ascending=True)[:last_date]


def check_for_zero(s: pd.Series) -> pd.Series:
    """
    If the last CPI value is zero, skip it.

    NBSC shows zero value always for the last month statistics if the official data is not published yet.
    """
    if s[0] == 0:
        s = s[1:]
    return s
