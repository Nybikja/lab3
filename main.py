from models import *
from manager import *


def main():
    a = TransportCompetitions("yamaha12", 4, 44, "gas", 120)
    b = GamesWithBall("volleyball", 3, 4, "light", "green")
    c = TransportCompetitions("yamaha42", 3, 21, "diesel", 119)
    d = TransportCompetitions("yamaha33", 5, 56, "gas", 122)
    e = GamesWithBall("гандбол", 12, 150, "super heavy", "blue")
    f = TransportCompetitions("yamaha51", 6, 54, "diesel", 121)
    g = GamesWithBall("football", 5, 10, "heavy", "red")

    all_objects = [a, b, c, d, e, f, g]
    manager_object = WaterSportManager(all_objects)

    def sort_by_name_main():
        out = manager_object.sort_by_name(False)  # [g, b, a, d, c, f, e]
        print("sorted by name\n")
        for i in out:
            print(i)

    def sort_by_price_main():
        out = manager_object.sort_by_price(False)  # [b, g, c, a, f, d, e]
        print("sorted by price: \n")
        for i in out:
            print(i)

    def check_for_enough_amount_main():
        out = manager_object.check_for_enough_amount()
        print("checked for enough amount: \n")
        for i in out:
            print(i)

    sort_by_price_main()  # price
    sort_by_name_main()  # name
    check_for_enough_amount_main()  # enough amount


if __name__ == "__main__":
    main()
