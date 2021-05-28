import unittest
import leap_year

class classTestLeapYear(unittest.TestCase):
    def test_leap_year_1(self):
        self.assertEqual(leap_year.check_year(40), "40 is a leap year")
