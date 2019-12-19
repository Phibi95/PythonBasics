greeting = "Hallo Benutzer wir rechnen gleich km in Miles um"
print(greeting)

while True:
    km = input("Gib die Kilometer an: ")

    km = float(km.replace(',','.'))

    mile = km * 0.621371

    print("{0} Kilometer sind {1} Meilen: ".format(km,mile))

    answer = input("Möchtest du noch eine Konvertierung vornehmen? (Ja/Nein):")
    print("Deine Antwort war: " + answer.lower())
    answer_lowercase = answer.lower()
    if(answer_lowercase != "ja"):
        break
    elif (answer_lowercase != "j"):
        break