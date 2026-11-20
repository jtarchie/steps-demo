"""The packing slip printed for every order, digital or not."""

from shop import cart, money


def packing_slip(order):
    items = order["items"]
    lines = [f"Order {order['id']}"]
    # Alphabetical, so the packer walks the shelves in order.
    for i in sorted(items, key=lambda i: i["name"]):
        lines.append(f"  {i['qty']} x {i['name']}  {money.dollars(i['price_cents'] * i['qty'])}")
    off = cart.discount(items)
    if off:
        lines.append(f"Bulk discount: -{money.dollars(off)}")
    lines.append(f"Shipping per box: {money.dollars(cart.shipping_per_box(items))}")
    lines.append(f"Total: {money.dollars(cart.total(items))}")
    return "\n".join(lines)
