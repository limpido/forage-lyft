import unittest

from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire

class TestCarriganTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        wear_array = [0.1, 0.2, 0.9, 0.6]
        tire = CarriganTire(wear_array)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        wear_array = [0.1, 0.2, 0.8, 0.6]
        tire = CarriganTire(wear_array)
        self.assertFalse(tire.needs_service())

class TestOctoprimeTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        wear_array = [0.6, 0.7, 0.9, 0.8]
        tire = OctoprimeTire(wear_array)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        wear_array = [0.6, 0.7, 0.8, 0.8]
        tire = OctoprimeTire(wear_array)
        self.assertFalse(tire.needs_service())