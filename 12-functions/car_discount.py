def calculate_discount(car_price, discount):
    discounted_price = car_price - discount
    # print("Der rabattierte Preis beträgt: " + str(discounted_price))
    return discounted_price

vw_price = 5
bmw_price = 10
tesla_price = 10000

vw_discounted_price = calculate_discount(vw_price,10)

print(vw_discounted_price)

calculate_discount(bmw_price,10)
calculate_discount(tesla_price,10)
