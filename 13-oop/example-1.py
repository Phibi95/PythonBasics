class Person:

    def __init__(self, name, height, weight):
        self.height = height
        self.weight = weight
        self.name = name
        self.bmi = weight / (height * height)

    def printBMI(self):
        print(self.name + '\'s BMI ist: ' + str(self.bmi))

    def getHeightIn(self,metric):
        if (metric == "CM"):
            return self.height * 100
        elif (metric == "FEET"):
            return self.height * 3.281
        return self.height

person_a = {
    "height": 1.7,
    "weight": 50.00,
    "name": "Musterfrau"
}

person_b = Person("Musterfrau",1.7,50)

print(person_a)

person_b_height_cm = person_b.getHeightIn("CM")
if(person_b_height_cm > 160):
    print("Du bist super!")