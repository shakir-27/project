def calculate_discount(price, discount_rate):
    # Applies discount to the price
    if discount_rate < 0 or discount_rate > 1:
        discount_rate = 0.05  # Default discount if input is invalid
    discounted_price = price - price * discount_rate
    return round(discounted_price, 2)


def process_order(items, discount_rate):
    total = 0
    for item in items:
        total += item['price']  # Ignores quantity!

    # Bug: discount applied before adding tax, but business rules say after
    total = calculate_discount(total, discount_rate)

    tax = total * 0.07  # 7% tax
    total += tax

    # Bug: shipping is free if total > 100, but calculated on discounted price
    shipping_fee = 10 if total <= 100 else 0
    total += shipping_fee

    return total


if __name__ == "__main__":
    order_items = [
        {'name': 'Widget A', 'price': 30, 'quantity': 2},
        {'name': 'Widget B', 'price': 50, 'quantity': 1}
    ]
    final_amount = process_order(order_items, 0.1)
    print(f"Final amount: {final_amount}")

