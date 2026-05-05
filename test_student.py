import unittest
from proj2 import *


class TestProject2(unittest.TestCase):

    def test_listlen_empty(self):
        self.assertEqual(listlen(None), 0)

    def test_listlen_three(self):
        row = Row("Canada", 2010, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0)
        data = Node(row, Node(row, Node(row, None)))
        self.assertEqual(listlen(data), 3)

    def test_parse_float_missing(self):
        self.assertEqual(parse_float(""), None)

    def test_parse_float_number(self):
        self.assertEqual(parse_float("12.5"), 12.5)

    def test_filter_country(self):
        row1 = Row("Canada", 2010, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0)
        row2 = Row("USA", 2011, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0)
        data = Node(row1, Node(row2, None))

        result = filter_rows(data, "country", "equal", "Canada")

        self.assertEqual(listlen(result), 1)
        self.assertEqual(result.value.country, "Canada")


if __name__ == "__main__":
    unittest.main()
