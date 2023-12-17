import pytest

from statement_crunch.aggregators import monthly_sum_aggregator
from statement_crunch.credit_statement import Entry


@pytest.mark.parametrize("entries, result", [
    ([], dict()),
    ([Entry(day=1, month=1, year=2000, credit=1000)], {(1,2000): 1000}),
    ([Entry(day=1, month=1, year=2000, credit=1000), Entry(day=1, month=1, year=2000, credit=500),], {(1,2000): 1500}),
    ])
def test_sum_aggregator(entries, result):
    assert monthly_sum_aggregator(entries) == result