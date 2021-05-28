import unittest
import leap_year

class classTestLeapYear(unittest.TestCase):
    def test_leap_year_1(self):
        self.assertEqual(leap_year.check_year(4000), "40 is a leap year")

    def test_leap_year_2(self):
        self.assertEqual(leap_year.check_year(4500), "4500 is not a leap year")
