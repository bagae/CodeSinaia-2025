import unittest
from TODO_number_to_words import number_to_words


class TestNumberToWords(unittest.TestCase):
   def test_interval(self):
       self.assertEqual(number_to_words(0), None)
       self.assertEqual(number_to_words(4000), None)

   def test_basic_numbers(self):
        self.assertEqual(number_to_words(1), "one")
        self.assertEqual(number_to_words(15), "fifteen")
        self.assertEqual(number_to_words(100), "one hundred")
        self.assertEqual(number_to_words(123), "one hundred twenty three")
        self.assertEqual(number_to_words(999), "nine hundred ninety nine")
        self.assertEqual(number_to_words(1919), "one thousand nine hundred nineteen")
        self.assertEqual(number_to_words(2121), "two thousand one hundred twenty one")
        self.assertEqual(number_to_words(3999), "three thousand nine hundred ninety nine")
        self.assertEqual(number_to_words(1000), "one thousand")

