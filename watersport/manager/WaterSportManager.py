from typing import List
from .. import WaterSport


class WaterSportManager:
    def __init__(self):
        self.sports = []

    def add_sport(self, sport: WaterSport) -> None:
        self.sports.append(sport)

    def add_sports(self, sports: List[WaterSport]) -> None:
        self.sports += sports

    def sort_by_price(self, reverse: bool = False, sports: List[WaterSport] = None):
        return sorted(sports if sports else self.sports, key=lambda s: s.price, reverse=reverse)

    def sort_by_name(self, reverse: bool = False, sports: List[WaterSport] = None):
        return sorted(sports if sports else self.sports, key=lambda s: s.name.lower(), reverse=reverse)

    def check_for_enough_amount(self):
        return (sport for sport in self.sports if sport.amount_of_players <= 5)
