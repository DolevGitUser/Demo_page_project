from datetime import datetime, timedelta
from playwright.sync_api import Page, expect
from logger import get_logger
from date_validator import DateValidator

class DemoMainPage:
    def __init__(self, page: Page):
        self.date_validator = DateValidator()
        self.page = page
        self.logger = get_logger()
        self.DEMO_PAGE_UEL = "https://demo.automationtesting.in/Index.html"
        self.date = None
        self.logger.info("DemoMainPage initialized with provided page object")

    def is_valid_date(self, day, month, year):
        self.logger.info(f"Validating date with day: {day}, month: {month}, year: {year}")
        is_valid = self.date_validator.is_valid_date(day, month, year)
        self.date = self._us_format_date(day, month, year)
        return is_valid

    def _us_format_date(self, day, month, year):
        """Formats the date in MM/DD/YYYY and returns a datetime.date object."""
        try:
            date_obj = datetime(year, month, day).date()
            formatted_date = date_obj.strftime("%m/%d/%Y")
            return formatted_date
        except ValueError as e:
            self.logger.error(f"Invalid date| {e}")
            raise

    def _get_year_range(self):
        current_date = datetime.now().date()
        min_valid_date = current_date - timedelta(days=365)
        max_valid_date = current_date + timedelta(days=365)
        self.logger.info(f"Valid year range: {min_valid_date} to {max_valid_date}")
        return (min_valid_date, max_valid_date)

    def is_in_year_range(self, day, month, year):
        """Check if the date is within the valid 1-year range."""
        self.logger.info(f"Checking if date is within the valid 1-year")
        self.date = self._us_format_date(day, month, year)
        date_obj = datetime.strptime(self.date, "%m/%d/%Y").date()
        year_range = self._get_year_range()
        if year_range[0] <= date_obj <= year_range[1]:
            return True
        else:
            self.logger.error(f"Target date {self.date} is out of the valid range.")
            raise ValueError(f"Target date {self.date} is out of the valid range. "
                             f"Must be within 1 year of the current date.")

    def navigate_to_date_picker(self):
        self.page.goto(self.DEMO_PAGE_UEL)
        self.page.locator("#logo").is_visible()
        self.page.get_by_role(role="button", name="Skip Sign In").click()
        self.page.get_by_role("heading", name="Automation Demo Site")
        self.page.get_by_role("link", name="Widgets").click()
        self.page.get_by_role("link", name="Datepicker").click()
        self.page.get_by_text("DatePicker Enabled")
        self.logger.info("Successfully navigated to date picker page")

    def goto_date_in_datepicker(self):
        """Select a specific date in the datepicker input."""
        self.logger.info(f"Selecting the date: {self.date} in the datepicker")
        self.page.locator("#datepicker2").click()
        self.page.locator("#datepicker2").type(self.date)
        self.logger.info(f"Date {self.date} selected in the datepicker")

    def get_datepicker_values(self):
        combobox_value = self.page.get_by_role("combobox").nth(1).input_value()
        month, year = combobox_value.split("/")
        expect(self.page.locator("table")).to_contain_text(self.date.split("/")[1])
        self.logger.info(f"Retrieved datepicker values: month={month}, year={year}")
        return {"month": month, "year": year}
