import unittest

from shop import cart

MUG = {"name": "mug", "price_cents": 1200, "qty": 1}
POSTER = {"name": "poster", "price_cents": 2000, "qty": 2}


class CartTest(unittest.TestCase):
    def test_subtotal(self):
        self.assertEqual(cart.subtotal([MUG, POSTER]), 5200)

    def test_free_shipping_over_threshold(self):
        self.assertEqual(cart.shipping([MUG, POSTER]), 0)

    def test_shipping_per_box(self):
        self.assertEqual(cart.shipping([MUG]), 800)
        self.assertEqual(cart.shipping_per_box([MUG]), 800)


if __name__ == "__main__":
    unittest.main()
