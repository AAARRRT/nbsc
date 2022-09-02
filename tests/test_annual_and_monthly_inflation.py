from pytest import approx

from nbsc import inflation as infl


def test_annual_and_monthly_inflation():
    infl_annual = infl.get_annual_inflation()["2015-12-01"] / 100
    monthly = infl.get_inflation_from_2001()["2015"]
    annual_from_monthly = (monthly / 100 + 1.0).prod() - 1.0
    assert annual_from_monthly == approx(infl_annual, rel=1e-2)
