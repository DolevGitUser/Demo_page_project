from logger import get_logger

class DateValidator:
    def __init__(self ):
        self.logger = get_logger()

    def _date_validation_pattern(self, minimum, maximum, given, type):
        """Validate if a value falls within the given range."""
        if minimum <= given <= maximum:
            return True
        else:
            raise ValueError(self.logger.error(f"Invalid {type} | {type} should be between {minimum} and {maximum}."))

    def _validate_day(self, day):
        """Validate the day. It should be between 1 and 31."""
        self._date_validation_pattern(minimum=1, maximum=31, type="day", given=day)

    def _validate_month(self, month):
        """Validate the month. It should be between 1 and 12."""
        self._date_validation_pattern(minimum=1, maximum=12, type="month", given=month)

    def _validate_year(self, year):
        """Validate the year. It should be a positive 4-digit integer."""
        self._date_validation_pattern(minimum=1000, maximum=9999, type="year", given=year)

    def is_valid_date(self, day, month, year):
        """Validate the month, day, and year."""
        try:
            self._validate_month(month)
            self._validate_day(day)
            self._validate_year(year)
            return True
        except ValueError:
            raise
