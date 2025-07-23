import unittest
from roman_converter import roman_converter

class TestInvalidInput(unittest.TestCase):
    # ======== Step 1 ======== no input, return None
    def test_no_input(self):
        self.assertEqual(roman_converter(None), None)
    def test_num_str(self):
        self.assertEqual(roman_converter(""), None)
    def test_interval(self):
        self.assertEqual(roman_converter(0),None)
        self.assertEqual(roman_converter(4000),None)
    def test_float(self):
         self.assertEqual(roman_converter(3.14), None)
class TestOnes(unittest.TestCase):
    def test_base_1(self):
        self.assertEqual(roman_converter(1), 'I')
    def test_base_5(self):
        self.assertEqual(roman_converter(4),'IV')
    def test_base_500(self):
        self.assertEqual(roman_converter(593), 'DXCIII')
class TestTens(unittest.TestCase):
    def test_base_10(self):
        self.assertEqual(roman_converter(10), 'X')
    def test_base_50(self):
        self.assertEqual(roman_converter(50), 'L')
    def test_base_90(self):
        self.assertEqual(roman_converter(90), 'XC')
    def test_base_100(self):
        self.assertTrue(roman_converter(114)=='CXIV')
    
    