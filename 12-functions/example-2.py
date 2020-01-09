global_discount = 25

def calculate_discount_with_global(item_price,discount):
    discounted_price = item_price - discount - global_discount
    return discounted_price

print(calculate_discount_with_global(100,50))

