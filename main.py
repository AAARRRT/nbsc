import math
from tests.test_annual_and_monthly_inflation import infl_annual, annual_from_monthly

assert math.isclose(infl_annual, annual_from_monthly, rel_tol=0.1)



