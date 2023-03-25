import pytest
from index import findNextDate, isLeafYear


@pytest.mark.parametrize(
    "input,output",
    [
        ((28, 2, 2023), (1, 3, 2023)),
        ((1, 2, 2023), (2, 2, 2023)),
        ((27, 2, 2023), (28, 2, 2023)),
    ],
)
def test_find_next_day(input, output):
    assert findNextDate(*input) == output


@pytest.mark.parametrize(
    "year, output",
    [(2021, False), (2020, True), (2000, True), (2100, False)],
)
def test_is_leaf_year(year, output):
    assert isLeafYear(year) == output
