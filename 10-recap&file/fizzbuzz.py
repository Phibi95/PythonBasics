while True: #Zwinge Benutzer zur richtigen Eingabe
    number = int(input('Gib eine Zahl zwischen 1 und 100 ein:'))
    if(number > 100):
        print('Falsche Zahl!')
    elif(number<1):
        print('Falsche Zahl!')
    else:
        break

for x in range(1,number+1):
    if (x % 3 == 0) and (x % 5 == 0):
        print("fizzbuzz")
    elif (x % 3 == 0):
        print("fizz")
    elif (x % 5 == 0):
        print("buzz")
    else:
        print(x)