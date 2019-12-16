price = 490
while True:
    #In Prozent
    discount_input = input("Wie hoch ist der Rabatt?: (in Prozent) ")

    discount = price / 100 * float(discount_input)

    price = price - discount

    text = "Dein finaler Preis lautet: "

    print(text + str(price))