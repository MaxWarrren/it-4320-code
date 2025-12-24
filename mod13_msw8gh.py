import unittest
import re
from datetime import datetime

def validate_symbol(symbol):
    """
    Symbol must be capitalized and 1–7 alphabetic characters.
    """
    return bool(re.fullmatch(r"[A-Z]{1,7}", symbol))


def validate_chart_type(chart_type):
    """
    Chart type must be a single numeric character: 1 or 2.
    """
    return chart_type in ["1", "2"]


def validate_time_series(time_series):
    """
    Time series must be a single numeric character: 1–4.
    """
    return time_series in ["1", "2", "3", "4"]


def validate_date(date_string):
    """
    Date must be in YYYY-MM-DD format.
    """
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False

class TestProject3Inputs(unittest.TestCase):

    # SYMBOL TESTS
    def test_valid_symbol(self):
        self.assertTrue(validate_symbol("AAPL"))
        self.assertTrue(validate_symbol("GOOG"))
        self.assertTrue(validate_symbol("TSLA"))

    def test_invalid_symbol(self):
        self.assertFalse(validate_symbol("aapl"))      # lowercase
        self.assertFalse(validate_symbol("AAPLL12"))   # numbers included
        self.assertFalse(validate_symbol("ABCDEFGH"))  # >7 characters
        self.assertFalse(validate_symbol(""))          # empty string

    # CHART TYPE TESTS
    def test_valid_chart_type(self):
        self.assertTrue(validate_chart_type("1"))
        self.assertTrue(validate_chart_type("2"))

    def test_invalid_chart_type(self):
        self.assertFalse(validate_chart_type("3"))
        self.assertFalse(validate_chart_type("A"))
        self.assertFalse(validate_chart_type(""))

    # TIME SERIES TESTS
    def test_valid_time_series(self):
        for value in ["1", "2", "3", "4"]:
            self.assertTrue(validate_time_series(value))

    def test_invalid_time_series(self):
        self.assertFalse(validate_time_series("0"))
        self.assertFalse(validate_time_series("5"))
        self.assertFalse(validate_time_series("X"))

    # DATE TESTS
    def test_valid_date(self):
        self.assertTrue(validate_date("2023-01-01"))
        self.assertTrue(validate_date("2022-12-31"))

    def test_invalid_date(self):
        self.assertFalse(validate_date("01-01-2023"))
        self.assertFalse(validate_date("2023/01/01"))
        self.assertFalse(validate_date("2023-13-01"))
        self.assertFalse(validate_date("abcd-ef-gh"))


if __name__ == "__main__":
    unittest.main()
