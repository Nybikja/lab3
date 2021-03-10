# from watersport.tester import WaterSportTest

from watersport.manager import WaterSportManager
from watersport import GamesWithBall, TransportCompetitions


class WaterSportTest:
    def __init__(self):
        pass

    def main(self):
        sport = WaterSportManager()
        sport.add_sports([
            TransportCompetitions("yamaha12", 4, 44, "gas", 120),
            GamesWithBall("volleyball", 3, 4, "light", "green"),
            TransportCompetitions("yamaha42", 3, 21, "diesel", 119),
            TransportCompetitions("yamaha33", 5, 56, "gas", 122),
            GamesWithBall("гандбол", 12, 150, "super heavy", "blue"),
            TransportCompetitions("yamaha51", 6, 54, "diesel", 121),
            GamesWithBall("football", 5, 10, "heavy", "red")

        ])

        print('sorted by price\n\n' + '\n'.join([str(x) for x in sport.sort_by_price(True)]), '\n')
        print('Sorted by name:\n\n' + '\n'.join([str(x) for x in sport.sort_by_name()]), '\n')
        print('available sport:\n\n' + '\n'.join([str(x) for x in sport.check_for_enough_amount()]))


if __name__ == '__main__':
    test = WaterSportTest()
    test.main()
