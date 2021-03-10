from watersport import WaterSport, SportType


class GamesWithBall(WaterSport):
    def __init__(self, name: str = "", amount_of_players: int = 0, price: int = 0, type_of_ball: str = "",
                 uniform_color: str = ""):
        super().__init__(SportType.PHYSICALGAME, name, amount_of_players, price)
        self.name = name
        self.amount_of_players = amount_of_players
        self.price = price
        self.type_of_ball = type_of_ball
        self.uniform_color = uniform_color

