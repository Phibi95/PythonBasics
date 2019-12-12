tv_available = True
bank_balance = 400.10

preis = float(input('Wie viel möchstest du ausgeben?'))
bank_balance = bank_balance - preis

if bank_balance > 0:
    print('Kontostand ist positiv. Super!')
else:
    print('Achtung du bist im Minus!')