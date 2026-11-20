import unittest

from shop import money, slip


class SlipTest(unittest.TestCase):
    def test_dollars(self):
        self.assertEqual(money.dollars(1999), "$19.99")
        self.assertEqual(money.dollars(125000), "$1,250.00")

    def test_slip_lists_items_alphabetically(self):
        order = {"id": 7, "items": [
            {"name": "poster", "price_cents": 2000, "qty": 1},
            {"name": "mug", "price_cents": 1200, "qty": 1},
        ]}
        lines = slip.packing_slip(order).splitlines()
        self.assertIn("mug", lines[1])
        self.assertIn("poster", lines[2])


if __name__ == "__main__":
    unittest.main()
