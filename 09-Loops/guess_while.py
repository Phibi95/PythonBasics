secret = 22
guess = 0

while True:
    guess = int(input('Rate meine Zahl!'))
    if(guess == secret):
        print('Super!')
        break
    else:
        if(guess>secret):
            print('Deine geratene Zahl ist größer als meine geheime Zahl!')
        else:
            print('Deine geratene Zahl ist kleiner als meine geheime Zahl')
        print('Versuche es nochmal')