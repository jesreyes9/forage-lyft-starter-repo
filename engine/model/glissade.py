from datetime import datetime
from car import Car
from engine.battery.spindler_battery import SpindlerBattery
from engine.willoughby_engine import WilloughbyEngine


class Glissade(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        self.battery = SpindlerBattery(last_service_date, datetime.today().date())

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date() or self.engine.needs_service():
            return True
        else:
            return False
