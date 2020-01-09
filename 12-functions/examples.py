discounted_price = 100

global_discount = 25

def calculate_discount(item_price,discount):
    discounted_price = item_price-discount
    return discounted_price

def calculate_discount_with_global(item_price,discount):
    discounted_price = item_price-discount - global_discount
    return discounted_price

print(calculate_discount(100,50))
print(discounted_price)

print(calculate_discount_with_global(100,50))

