"""Cart math for the shop. Prices are integer cents everywhere."""

FREE_SHIPPING_CENTS = 5000
SHIPPING_PER_BOX_CENTS = 800


def subtotal(items):
    return sum(i["price_cents"] * i["qty"] for i in items)


def boxes(items):
    """How many boxes the warehouse packs: one per physical line.

    Digital items (gift cards, downloads) ship by email, so they get no box.
    """
    return sum(1 for i in items if not i.get("digital"))


def shipping(items):
    if subtotal(items) >= FREE_SHIPPING_CENTS:
        return 0
    return SHIPPING_PER_BOX_CENTS * boxes(items)


def shipping_per_box(items):
    """What each box's label says it cost, for the packing slip."""
    return shipping(items) // boxes(items)


def total(items):
    return subtotal(items) + shipping(items)
