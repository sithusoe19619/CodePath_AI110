def calculate_cart_total(cart, discount_percent=0):
    """Calculate shopping cart total with an optional discount.

    Args:
        cart: list of dicts with 'price' and 'quantity' keys.
        discount_percent: discount to apply (0-100).

    Returns:
        A dict with 'subtotal', 'discount', and 'total'.
    """
    subtotal = sum(item["price"] * item["quantity"] for item in cart)
    discount = round(subtotal * (discount_percent / 100), 2)
    total = round(subtotal - discount, 2)
    return {"subtotal": subtotal, "discount": discount, "total": total}


# Example usage
if __name__ == "__main__":
    cart = [
        {"name": "Shirt", "price": 25.99, "quantity": 2},
        {"name": "Pants", "price": 45.50, "quantity": 1},
        {"name": "Socks", "price": 8.99, "quantity": 3},
    ]

    result = calculate_cart_total(cart, discount_percent=15)
    print(f"Subtotal: ${result['subtotal']:.2f}")
    print(f"Discount: -${result['discount']:.2f}")
    print(f"Total: ${result['total']:.2f}")
