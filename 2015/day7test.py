import unittest
from day7 import find_rule, get_value  # assuming the function is in day7.py

# class TestFindRule(unittest.TestCase):
#     def test_find_rule_with_not(self):
#         line = "NOT lf -> ls"
#         result = find_rule(line)
#         self.assertEqual(result, ('', 'NOT', 'lf', 'ls'))

#     def test_find_rule_without_not(self):
#         line = "lf AND lq -> ls"
#         result = find_rule(line)
#         self.assertEqual(result, ('lf', 'AND', 'lq', 'ls'))

#     def test_find_rule_with_empty_string(self):
#         line = "gj RSHIFT 1 -> hc"
#         result = find_rule(line)
#         self.assertEqual(result, ('gj', 'RSHIFT', '1', 'hc'))

#     def test_find_rule_with_no_output(self):
#         line = "ko AND kq -> kr"
#         result = find_rule(line)
#         self.assertEqual(result, ('ko', 'AND', 'kq', 'kr'))

#     def test_find_rule_with_no_input(self):
#         line = "fj LSHIFT 15 -> fn"
#         result = find_rule(line)
#         self.assertEqual(result, ('fj', 'LSHIFT', '15', 'fn'))

#     def test_find_rule_with_no_input(self):
#         line = "fj -> fn"
#         result = find_rule(line)
#         self.assertEqual(result, ('fj', 'SET', '', 'fn'))

#     def test_find_rule_with_no_input(self):
#         line = "15 -> fn"
#         result = find_rule(line)
#         self.assertEqual(result, (15, 'SET_N', '', 'fn'))

# if __name__ == '__main__':
#     unittest.main()

class TestGetValue(unittest.TestCase):
    def setUp(self):
        self.rules = {
            'x': (123, 'SET_N', ''),
            'y': (456, 'SET_N', ''),
            'd': ('x', 'AND', 'y'),
            'e': ('x', 'OR', 'y'),
            'f': ('x', 'LSHIFT', 2),
            'g': ('y', 'RSHIFT', 2),
            'h': ('', 'NOT', 'x'),
            'i': ('', 'NOT', 'y')
        }

    def test_get_value_x(self):
        global rules
        rules = self.rules
        self.assertEqual(get_value('x', rules), 123)

    def test_get_value_y(self):
        global rules
        rules = self.rules
        self.assertEqual(get_value('y', rules), 456)

    def test_get_value_d(self):
        global rules
        rules = self.rules
        self.assertEqual(get_value('d', rules), 72)

    def test_get_value_e(self):
        global rules
        rules = self.rules
        self.assertEqual(get_value('e', rules), 507)

    def test_get_value_f(self):
        global rules
        rules = self.rules
        self.assertEqual(get_value('f', rules), 492)

    def test_get_value_g(self):
        global rules
        rules = self.rules
        self.assertEqual(get_value('g', rules), 114)

    def test_get_value_h(self):
        global rules
        rules = self.rules
        self.assertEqual(get_value('h', rules), 65412)

    def test_get_value_i(self):
        global rules
        rules = self.rules
        self.assertEqual(get_value('i', rules), 65079)

if __name__ == '__main__':
    unittest.main()