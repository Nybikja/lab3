import unittest
from manager import *
from models import *


class TestWaterSportManager(unittest.TestCase):

    def setUp(self):
        self.a = TransportCompetitions("yamaha12", 4, 44, "gas", 120)
        self.b = GamesWithBall("volleyball", 3, 4, "light", "green")
        self.c = TransportCompetitions("yamaha42", 3, 21, "diesel", 119)
        self.d = TransportCompetitions("yamaha33", 5, 56, "gas", 122)
        self.e = GamesWithBall("гандбол", 12, 150, "super heavy", "blue")
        self.f = TransportCompetitions("yamaha51", 6, 54, "diesel", 121)
        self.g = GamesWithBall("football", 5, 10, "heavy", "red")

        all_objects = [self.a, self.b, self.c, self.d, self.e, self.f, self.g]
        self.water_sport_manager = WaterSportManager(all_objects)

    def test_sort_by_name(self):
        self.assertEqual(self.water_sport_manager.sort_by_name(False), [self.g, self.b, self.a, self.d, self.c,
                                                                        self.f, self.e])

    def test_sort_by_price(self):
        self.assertEqual(self.water_sport_manager.sort_by_price(False), [self.b, self.g, self.c, self.a, self.f,
                                                                         self.d, self.e])

    def test_check_for_amount(self):
        self.assertEqual(self.water_sport_manager.check_for_enough_amount(), [self.a, self.b, self.c, self.d, self.g])


if __name__ == "__main__":
    unittest.main()
