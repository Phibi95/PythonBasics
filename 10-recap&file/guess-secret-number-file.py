import random
import os.path


secret = random.randint(1, 30)
attempts = 0
if os.path.isfile('score.txt'):
    with open('score.txt','r') as file:
        highscore = int(file.read())
else:
    highscore = 10000

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))

        if(attempts < highscore):
            with open('score.txt', 'w') as file:
                file.write(str(attempts))

        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")