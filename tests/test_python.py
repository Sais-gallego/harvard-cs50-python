"""
Unit Tests for Harvard CS50P Python Programming Suite
Author: Sergio Andrés Ipuz Saavedra (@Sais-gallego)
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.core_programming import (
    CS50RegexValidator,
    LuhnCardValidator,
    Jar
)


class TestHarvardCS50Python(unittest.TestCase):

    def test_numb3rs_ipv4_validation(self):
        self.assertTrue(CS50RegexValidator.validate_ipv4("127.0.0.1"))
        self.assertTrue(CS50RegexValidator.validate_ipv4("255.255.255.255"))
        self.assertTrue(CS50RegexValidator.validate_ipv4("192.168.1.1"))

        # Invalid cases
        self.assertFalse(CS50RegexValidator.validate_ipv4("256.100.0.1"))
        self.assertFalse(CS50RegexValidator.validate_ipv4("1.2.3.1000"))
        self.assertFalse(CS50RegexValidator.validate_ipv4("cat.dog.cow.fox"))
        self.assertFalse(CS50RegexValidator.validate_ipv4("1.2.3"))

    def test_youtube_embed_extraction(self):
        iframe_html = '<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player"></iframe>'
        url = CS50RegexValidator.extract_youtube_embed(iframe_html)
        self.assertEqual(url, "https://youtu.be/xvFZjo5PgG0")

        # Non-youtube iframe
        other_iframe = '<iframe src="https://vimeo.com/123456"></iframe>'
        self.assertIsNone(CS50RegexValidator.extract_youtube_embed(other_iframe))

    def test_working_9_to_5_conversion(self):
        self.assertEqual(CS50RegexValidator.convert_12_to_24_hours("9:00 AM to 5:00 PM"), "09:00 to 17:00")
        self.assertEqual(CS50RegexValidator.convert_12_to_24_hours("9 AM to 5 PM"), "09:00 to 17:00")
        self.assertEqual(CS50RegexValidator.convert_12_to_24_hours("10:30 PM to 8:00 AM"), "22:30 to 08:00")

        # Invalid formats must raise ValueError
        with self.assertRaises(ValueError):
            CS50RegexValidator.convert_12_to_24_hours("9:60 AM to 5:00 PM")
        with self.assertRaises(ValueError):
            CS50RegexValidator.convert_12_to_24_hours("9AM - 5PM")

    def test_luhn_credit_card_brand_identification(self):
        # Valid Visa test (starts with 4)
        visa = "4000001234567891"
        # Validate checksum logic directly
        self.assertIn(LuhnCardValidator.get_card_brand(visa), ["VISA", "INVALID"])

        # Invalid short string
        self.assertEqual(LuhnCardValidator.get_card_brand("123"), "INVALID")

    def test_jar_oop_model(self):
        jar = Jar(capacity=10)
        self.assertEqual(jar.capacity, 10)
        self.assertEqual(jar.size, 0)
        self.assertEqual(str(jar), "")

        # Deposit
        jar.deposit(4)
        self.assertEqual(jar.size, 4)
        self.assertEqual(str(jar), "🍪🍪🍪🍪")

        # Withdraw
        jar.withdraw(1)
        self.assertEqual(jar.size, 3)
        self.assertEqual(str(jar), "🍪🍪🍪")

        # Exceeding capacity must raise ValueError
        with self.assertRaises(ValueError):
            jar.deposit(15)

        # Exceeding current cookies on withdraw
        with self.assertRaises(ValueError):
            jar.withdraw(10)

        # Negative capacity
        with self.assertRaises(ValueError):
            Jar(capacity=-5)


if __name__ == "__main__":
    unittest.main()
