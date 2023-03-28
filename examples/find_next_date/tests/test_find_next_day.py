import pytest
from src.findNextDate import findNextDate, isLeapYear, getMonthLength, isValidDate
from unittest.mock import patch


@pytest.fixture
def mockIsLeapYear(mocker, isLeapYear):
    mocker.patch("src.findNextDate.isLeapYear", return_value=isLeapYear)


@pytest.fixture
def mockGetMonthLength(mocker, monthLength):
    mocker.patch("src.findNextDate.getMonthLength", return_value=monthLength)


@pytest.mark.parametrize(
    "year, output",
    [(2021, False), (2020, True), (2000, True), (2100, False)],
)
def test_is_leap_year(year, output):
    assert isLeapYear(year) == output


@pytest.mark.parametrize(
    "month, year, isLeapYear, monthLength",
    [
        (2, 2023, False, 28),
        # (4, 2023, False, 30),
        # (2, 2024, True, 29),
        # (3, 2023, False, 31),
    ],
)
@pytest.mark.usefixtures("mockIsLeapYear")
def test_get_month_length(month, year, isLeapYear, monthLength):
    assert getMonthLength(month, year) == monthLength


@pytest.mark.parametrize(
    "day, month, year, monthLength, isValid",
    [(1, 2, 2023, 28, True), (30, 2, 2024, 29, False), (20, 0, 2023, 0, False)],
)
@pytest.mark.usefixtures("mockGetMonthLength")
def test_is_valid_date(day, month, year, monthLength, isValid):
    assert isValidDate(day, month, year) == isValid


@pytest.mark.parametrize(
    "input,output",
    [
        ((28, 2, 2023), (1, 3, 2023)),
        ((1, 2, 2023), (2, 2, 2023)),
        ((31, 12, 2023), (1, 1, 2024)),
    ],
)
def test_find_next_day(input, output):
    with patch("src.findNextDate.isValidDate", return_value=True):
        assert findNextDate(*input) == output


@pytest.mark.parametrize(
    "day, month, year",
    [
        (29, 2, 2023),
        (31, 4, 2023),
        (30, 2, 2024),
    ],
)
def test_find_next_day_with_invalid_date(day, month, year):
    with pytest.raises(ValueError):
        with patch("src.findNextDate.isValidDate", return_value=False):
            findNextDate(day, month, year)
