from models import WaterSport, SportType


class GamesWithBall(WaterSport):
    def __init__(self, name: str = "", amount_of_players: int = 0, price: int = 0, type_of_ball: str = "",
                 uniform_color: str = ""):
        super().__init__(SportType.PHYSICALGAME, name, amount_of_players, price)
        self.name = name
        self.amount_of_players = amount_of_players
        self.price = price
        self.type_of_ball = type_of_ball
        self.uniform_color = uniform_color

    def __str__(self):
        return f"type: {self._sport_type}\nname: {self._name}\namount of players: {self._amount_of_players}\n" \
               f"price: {self._price}\ntype of ball: {self.type_of_ball}\nuniform color: {self.uniform_color}\n"
