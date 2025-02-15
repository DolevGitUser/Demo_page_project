import pytest
from conftest import demo_main_page

@pytest.mark.parametrize(
    "month, day, year",
    [
        # Valid dates
        (1, 1, 2025),  # January 1st, 2025
        (1, 17, 2025),  # January 1st, 2025
        (2, 29, 2024),  # February 29th, 2024 (Leap year)
        # Invalid dates
        (2, 30, 2025),  # Invalid February 30th, 2025 (not a valid day in February)
        (4, 31, 2025),  # Invalid April 31st, 2025 (April has only 30 days)
        (12, 32, 2025),  # Invalid December 32nd, 2025 (December has only 31 days)
        # Invalid month
        (13, 1, 2025),  # Invalid month 13 (months should be 1-12)
        # Invalid day
        (10, 100, 2025),  # Invalid day  (day should be 1-100)
        # Invalid years
        (2, 28, 999),  # Invalid year (too small)
        (2, 28, 10000),  # Invalid year (too large)
    ]
)
def test_one_date(demo_main_page, month, year, day):
    demo_main_page.logger.info(f"Starting test for date: {month}/{day}/{year}")
    demo_main_page.is_valid_date(day, month, year)
    demo_main_page.is_in_year_range(day, month, year)
    demo_main_page.logger.info(f"Date {day}/{month}/{year} is within the valid year range.")
    demo_main_page.navigate_to_date_picker()
    demo_main_page.goto_date_in_datepicker()
    date_in_datepicker = demo_main_page.get_datepicker_values()
    assert str(month) == date_in_datepicker["month"], f"Expected month {month}, but got {date_in_datepicker['month']}"
    assert str(year) == date_in_datepicker["year"], f"Expected year {year}, but got {date_in_datepicker['year']}"

    demo_main_page.logger.info(f"Test passed for date: {month}/{day}/{year}")
