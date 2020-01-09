import datetime
import json
import random



def get_score_list():
    with open("score_list.txt", "r") as score_file:
        return json.loads(score_file.read())

def get_top_scores():
    score_list = get_score_list()
    return sorted(score_list, key=lambda k: k['attempts'])[:3]

def play_game():
    score_list = get_score_list()
    secret = random.randint(1, 30)
    attempts = 0
    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1

        if guess == secret:
            score_list.append({"attempts": attempts, "date": str(datetime.datetime.now())})
            with open("score_list.txt", "w") as score_file:
                score_file.write(json.dumps(score_list))

            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            break
        elif guess > secret:
            print("Your guess is not correct... try something smaller")
        elif guess < secret:
            print("Your guess is not correct... try something bigger")


while True:
    selection = input("Would you like to A) play a new game, B) see the best scores, or C) quit?")

    if selection == "A":
        play_game()
    elif selection == "B":
        for score_dict in get_top_scores():
            print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))
    else:
        break