"""Money formatting. Everything upstream is integer cents; this is the one
place cents become something a person reads."""


def dollars(cents):
    """1999 -> "$19.99", 125000 -> "$1,250.00"."""
    return f"${cents / 100:,.2f}"
