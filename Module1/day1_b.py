def discount_calc(cart, code, all_codes):
    if code not in all_codes:
        return {
            "originalCart": cart,
            "discountedCart": cart
        }

    discount_percent = all_codes[code]

    discounted_cart = []
    for item in cart:
        total_price = item["Price"] * item["Quantity"]
        discounted_price = total_price * (1 - discount_percent / 100)
        discounted_cart.append({
            "Name": item["Name"],
            "Price": discounted_price
        })

    return {
        "originalCart": cart,
        "discountedCart": discounted_cart
    }


cart = [
    {"Name": "Shirt", "Price": 25.00, "Quantity": 2},
    {"Name": "Hat", "Price": 15.00, "Quantity": 1}
]
codes = {"SAVE20": 20, "HALF": 50}

result = discount_calc(cart, "SAVE20", codes)
print(result)
