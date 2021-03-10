from watersport import WaterSport, SportType


class TransportCompetitions(WaterSport):
    def __init__(self, name: str = "", amount_of_players: int = 0, price: int = 0, type_of_engine: str = "",
                 horsepower: int = 0):
        super().__init__(SportType.TRANSPORTTYPE, name, amount_of_players, price)
        self.name = name
        self.amount_of_players = amount_of_players
        self.price = price
        self.type_of_engine = type_of_engine
        self.horsepower = horsepower
