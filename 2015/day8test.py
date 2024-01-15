import unittest
from day8 import parse_line  # assuming the function is in day8.py

class TestParseLine(unittest.TestCase):
    def test_parse_line_with_no_escapes(self):
        line = '""'
        result = parse_line(line)
        self.assertEqual(result, (2, 6))

    def test_parse_line_with_double_backslashes(self):
        line = '"abc"'
        result = parse_line(line)
        self.assertEqual(result, (5, 9))

    def test_parse_line_with_double_quotes(self):
        line = r'"aaa\"aaa"'
        result = parse_line(line)
        self.assertEqual(result, (10, 16))

    def test_parse_line_with_hexadecimal(self):
        line = '"\\x27"'
        result = parse_line(line)
        self.assertEqual(result, (6, 11))

if __name__ == '__main__':
    unittest.main()