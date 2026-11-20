"""Cart math for the shop. Prices are integer cents everywhere."""

FREE_SHIPPING_CENTS = 5000
SHIPPING_PER_BOX_CENTS = 800
BULK_QTY = 10


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


def discount(items):
    """10% off every line with 10 or more of the same item."""
    if not items:
        return 0
    biggest = max(i["qty"] for i in items)
    if biggest < BULK_QTY:
        return 0
    return sum(i["price_cents"] * i["qty"] // 10 for i in items if i["qty"] > BULK_QTY)


def total(items):
    return subtotal(items) - discount(items) + shipping(items)
