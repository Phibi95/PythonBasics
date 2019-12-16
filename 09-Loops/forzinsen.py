bank_balance = 400
interest = 1.5
start_year = 2019
fee = 20
for x in range(25):
    bank_balance = bank_balance - fee                               # Bankgebühr abziehen
    bank_balance = bank_balance + bank_balance * (interest / 100)   # Zinsen
    print(str(start_year + x + 1) + ': neuer Kontostand: ' + str(bank_balance))