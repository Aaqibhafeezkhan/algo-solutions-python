import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice63 import bigger_price  # noqa: E402


class BiggerPriceTest(unittest.TestCase):
    def test_examples(self):
        data = [
            {"name": "bread", "price": 100},
            {"name": "wine", "price": 138},
            {"name": "meat", "price": 15},
            {"name": "water", "price": 1},
        ]
        self.assertEqual(
            bigger_price(2, data),
            [{"name": "wine", "price": 138}, {"name": "bread", "price": 100}],
        )

    def test_duplicate_prices_keep_all_items_in_input_order(self):
        data = [
            {"name": "first", "price": 100},
            {"name": "second", "price": 100},
            {"name": "highest", "price": 150},
            {"name": "third", "price": 100},
        ]
        self.assertEqual(
            bigger_price(3, data),
            [
                {"name": "highest", "price": 150},
                {"name": "first", "price": 100},
                {"name": "second", "price": 100},
            ],
        )

    def test_limit_larger_than_data_returns_all_items_sorted(self):
        data = [{"name": "low", "price": 1}, {"name": "high", "price": 10}]
        self.assertEqual(
            bigger_price(5, data),
            [{"name": "high", "price": 10}, {"name": "low", "price": 1}],
        )

    def test_non_positive_limit_returns_empty_list(self):
        data = [{"name": "item", "price": 5}]
        self.assertEqual(bigger_price(0, data), [])
        self.assertEqual(bigger_price(-1, data), [])

    def test_empty_data_returns_empty_list(self):
        self.assertEqual(bigger_price(2, []), [])


if __name__ == "__main__":
    unittest.main()
