class WaterSportManager:

    def __init__(self, sport=list):
        self.__sport = sport

    def sort_by_name(self, order):
        self.__sport.sort(key=lambda s: s.name.lower(), reverse=order)
        out = self.__sport
        return out

    def sort_by_price(self, order):
        self.__sport.sort(key=lambda s: s.price, reverse=order)
        out = self.__sport
        return out

    def check_for_enough_amount(self):
        out = list()
        for amount in self.__sport:
            if amount.amount_of_players <= 5:
                out.append(amount)
        self.__sport = out
        return out
