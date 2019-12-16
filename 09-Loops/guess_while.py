import random
guess = 0
secret = random.randint(1, 5)

while True:
    guess = int(input('Rate meine Zahl!'))
    if (guess == secret):
        print('Super!')
        break
    elif (guess > secret):
        print('Deine geratene Zahl ist größer als meine geheime Zahl!')
    elif (guess < secret):
        print('Deine geratene Zahl ist kleiner als meine geheime Zahl!')
    print('Versuche es nochmal')