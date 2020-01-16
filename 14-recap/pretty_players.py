class Player():
    def __init__(self,first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight = weight_kg
        self.bmi = weight_kg / ((height_cm/100) * (height_cm/100))

    def get_weight_in_lbs(self):
        return self.weight *2.20462262

    def convert_weight_to_lbs(self):
        self.weight = self.weight * 2.20462262

class FootballPlayer(Player):
    def __init__(self,first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name,last_name,height_cm,weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards

class BasketballPlayer(Player):
    def __init__(self,first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name, last_name, height_cm, weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists

player_1 = BasketballPlayer(first_name="Lebron",last_name="James",height_cm=203,weight_kg=113,points=27.2,rebounds=7.4,assists=7.2)

player_2 = BasketballPlayer(first_name="Kevin", last_name="Durant", height_cm=210, weight_kg=108, points=27.2,
                           rebounds=7.1, assists=4)

basketball_players = [player_1,player_2]