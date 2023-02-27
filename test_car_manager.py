import unittest

from car_manager import CarManager


class TestCarManager(unittest.TestCase):

    def setUp(self):
        self.car_manager = CarManager()
    #
    # def test_create_car(self):
    #     # Check if a car is created and added to the all_cars list
    #     self.car_manager.create_car()
    #     self.assertNotEqual(len(self.car_manager.all_cars), 0)

    # def test_move_cars(self):
    #     # Check if the car is moved backwards by the car_speed value
    #     self.car_manager.create_car()
    #     initial_pos = self.car_manager.all_cars[0].position()[0]
    #
    #     self.car_manager.move_cars()
    #     self.assertLess(self.car_manager.all_cars[0].position()[0], initial_pos)