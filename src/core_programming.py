"""
CS50P - Core Implementations: Functions, Regex, OOP, and Validation
Author: Sergio Andrés Ipuz Saavedra (@Sais-gallego)
Harvard University CS50's Introduction to Programming with Python (Prof. David J. Malan)
"""

import re
import csv
from typing import Dict, List, Optional, Tuple


class CS50RegexValidator:
    """Implements Week 7 Regular Expressions challenges (NUMB3RS, Watch, Working, Regular)."""

    @staticmethod
    def validate_ipv4(ip: str) -> bool:
        """
        CS50P Week 7: NUMB3RS
        Validates whether string is an IPv4 address in #.#.#.# format (0-255 for each octet).
        """
        pattern = r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$"
        match = re.search(pattern, ip.strip())
        if not match:
            return False
        return all(0 <= int(octet) <= 255 for octet in match.groups())

    @staticmethod
    def extract_youtube_embed(html_snippet: str) -> Optional[str]:
        """
        CS50P Week 7: Watch on YouTube
        Extracts YouTube URL from an <iframe> and converts to shareable https://youtu.be/<id> format.
        """
        pattern = r'<iframe[^>]*\bsrc=["\']https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)["\']'
        match = re.search(pattern, html_snippet)
        if match:
            video_id = match.group(1)
            return f"https://youtu.be/{video_id}"
        return None

    @staticmethod
    def convert_12_to_24_hours(time_str: str) -> str:
        """
        CS50P Week 7: Working 9 to 5
        Converts 12-hour format string (e.g., '9:00 AM to 5:00 PM' or '9 AM to 5 PM')
        to 24-hour format (e.g., '09:00 to 17:00').
        """
        pattern = r"^(\d{1,2})(?::(\d{2}))?\s+(AM|PM)\s+to\s+(\d{1,2})(?::(\d{2}))?\s+(AM|PM)$"
        match = re.search(pattern, time_str.strip())
        if not match:
            raise ValueError(f"Invalid time format: {time_str}")

        h1, m1, p1, h2, m2, p2 = match.groups()
        h1, h2 = int(h1), int(h2)
        m1 = int(m1) if m1 else 0
        m2 = int(m2) if m2 else 0

        if not (1 <= h1 <= 12 and 0 <= m1 < 60 and 1 <= h2 <= 12 and 0 <= m2 < 60):
            raise ValueError("Time values out of valid range")

        def to_24(h, m, p):
            if p == "AM":
                h24 = 0 if h == 12 else h
            else:
                h24 = 12 if h == 12 else h + 12
            return f"{h24:02d}:{m:02d}"

        return f"{to_24(h1, m1, p1)} to {to_24(h2, m2, p2)}"


class LuhnCardValidator:
    """Implements CS50 Credit: Luhn's Algorithm checksum for credit card validation."""

    @staticmethod
    def is_valid(card_number: str) -> bool:
        """Verify credit card number validity via Luhn's algorithm."""
        digits = [int(c) for c in card_number if c.isdigit()]
        if len(digits) < 13:
            return False

        # Multiply every other digit by 2 starting from second-to-last
        checksum = 0
        reverse_digits = digits[::-1]
        for idx, digit in enumerate(reverse_digits):
            if idx % 2 == 1:
                doubled = digit * 2
                checksum += (doubled // 10) + (doubled % 10)
            else:
                checksum += digit

        return (checksum % 10) == 0

    @classmethod
    def get_card_brand(cls, card_number: str) -> str:
        """Identify card issuer (AMEX, MASTERCARD, VISA, or INVALID)."""
        clean = "".join(c for c in card_number if c.isdigit())
        if not cls.is_valid(clean):
            return "INVALID"

        length = len(clean)
        if length == 15 and (clean.startswith("34") or clean.startswith("37")):
            return "AMEX"
        elif length == 16 and (51 <= int(clean[:2]) <= 55):
            return "MASTERCARD"
        elif (length == 13 or length == 16) and clean.startswith("4"):
            return "VISA"
        return "UNKNOWN"


class Jar:
    """
    CS50P Week 8: Object-Oriented Programming (OOP) - Jar Class
    Simulates a cookie jar with capacity, deposits, withdrawals, and string representation.
    """

    def __init__(self, capacity: int = 12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity
        self._size = 0

    def __str__(self) -> str:
        return "🍪" * self._size

    def deposit(self, n: int):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Deposit amount must be non-negative")
        if self._size + n > self._capacity:
            raise ValueError("Deposit exceeds jar capacity")
        self._size += n

    def withdraw(self, n: int):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Withdraw amount must be non-negative")
        if self._size - n < 0:
            raise ValueError("Withdraw exceeds cookies in jar")
        self._size -= n

    @property
    def capacity(self) -> int:
        return self._capacity

    @property
    def size(self) -> int:
        return self._size
