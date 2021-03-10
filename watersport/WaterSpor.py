from enum import Enum


class SportType(Enum):
    TRANSPORTTYPE = 0
    PHYSICALGAME = 1


class WaterSport:
    def __init__(self, sport_type: SportType, name: str = "", amount_of_players: int = 0, price: int = 0):
        self._sport_type = sport_type
        self._name = name
        self._amount_of_players = amount_of_players
        self._price = price

    def __str__(self):
        return f"type: {self._sport_type}\nname: {self._name}\namount of players: {self._amount_of_players}\n" \
               f"price: {self._price}\n"

