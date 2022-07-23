from battery.nubbin_battery import NubbinBattery
from car import Car
from engine.capulet_engine import CapuletEngine
from battery.spindler_battery import SpindlerBattery
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class CarFactory():
    def __init__(self):
        pass

    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car
    
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car
    
    def create_palindrome(self, current_date, last_service_date, warning_light_is_on):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car
    
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car
    
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car