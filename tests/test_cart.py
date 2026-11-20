import unittest

from shop import cart

MUG = {"name": "mug", "price_cents": 1200, "qty": 1}
POSTER = {"name": "poster", "price_cents": 2000, "qty": 2}
GIFT_CARD = {"name": "gift card", "price_cents": 2500, "qty": 1, "digital": True}


class CartTest(unittest.TestCase):
    def test_subtotal(self):
        self.assertEqual(cart.subtotal([MUG, POSTER]), 5200)

    def test_free_shipping_over_threshold(self):
        self.assertEqual(cart.shipping([MUG, POSTER]), 0)

    def test_shipping_per_box(self):
        self.assertEqual(cart.shipping([MUG]), 800)
        self.assertEqual(cart.shipping_per_box([MUG]), 800)

    def test_digital_items_get_no_box(self):
        self.assertEqual(cart.boxes([MUG, GIFT_CARD]), 1)

    def test_bulk_discount(self):
        stickers = {"name": "sticker", "price_cents": 100, "qty": 25}
        self.assertEqual(cart.discount([stickers]), 250)

    def test_no_discount_on_small_orders(self):
        self.assertEqual(cart.discount([MUG]), 0)


if __name__ == "__main__":
    unittest.main()
