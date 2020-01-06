import random
import os.path
import json

secret = random.randint(1, 30)
secret = 12
attempts = 0
if os.path.isfile('score.txt'):
    with open('score.txt','r') as file:
        score_list = json.loads(file.read())
        print('Das sind die letzten Highscores: ')
        score_list.sort()
        print(score_list[:3])
else:
    score_list = []

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))

        score_list.append(attempts)
        with open('score.txt', 'w') as file:
            file.write(json.dumps(score_list))

        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")