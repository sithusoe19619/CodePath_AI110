def calculate_cart_total(items, discount_percent=0):
    """
    Calculate the total cost of a shopping cart with an optional discount.

    Args:
        items: list of dicts with 'price' and 'quantity' keys
        discount_percent: discount percentage (0-100), defaults to 0

    Returns:
        float: final total after discount
    """
    subtotal = sum(item['price'] * item['quantity'] for item in items)
    discount_amount = subtotal * (discount_percent / 100)
    return subtotal - discount_amount


# Example usage
if __name__ == "__main__":
    cart = [
        {'name': 'Apple', 'price': 1.50, 'quantity': 4},
        {'name': 'Bread', 'price': 3.99, 'quantity': 1},
        {'name': 'Milk',  'price': 2.49, 'quantity': 2},
    ]

    total = calculate_cart_total(cart, discount_percent=10)
    print(f"Total after 10% discount: ${total:.2f}")
