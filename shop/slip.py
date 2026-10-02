"""The packing slip printed for every order, digital or not."""

from shop import cart


def packing_slip(order):
    items = order["items"]
    lines = [f"Order {order['id']}"]
    for i in items:
        lines.append(f"  {i['qty']} x {i['name']}")
    lines.append(f"Shipping per box: {cart.shipping_per_box(items)} cents")
    lines.append(f"Total: {cart.total(items)} cents")
    return "\n".join(lines)
