import unittest
from day10 import increment, is_valid  # assuming the function is in day10.py

class TestIncrement(unittest.TestCase):
    def test_increment_single_character(self):
        password = "a"
        result = increment(password)
        self.assertEqual(result, "b")

    def test_increment_multiple_characters(self):
        password = "abc"
        result = increment(password)
        self.assertEqual(result, "abd")

    def test_increment_with_z(self):
        password = "abz"
        result = increment(password)
        self.assertEqual(result, "aca")

    def test_increment_with_all_z(self):
        password = "zzz"
        result = increment(password)
        self.assertEqual(result, "aaa")
        
    def test_is_valid_with_invalid_characters(self):
        password = "hijklmmn"
        self.assertFalse(is_valid(password))

    def test_is_valid_without_pairs(self):
        password = "abbceffg"
        self.assertFalse(is_valid(password))

    def test_is_valid_with_one_pair(self):
        password = "abbcegjk"
        self.assertFalse(is_valid(password))

    def test_is_valid_with_two_pairs(self):
        password = "aabcdeeg"
        self.assertFalse(is_valid(password))

    def test_is_valid_with_two_pairs(self):
        password = "abczz"
        self.assertTrue(is_valid(password))

if __name__ == '__main__':
    unittest.main()