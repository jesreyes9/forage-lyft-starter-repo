from datetime import datetime
from car import Car
from engine.battery.spindler_battery import SpindlerBattery
from engine.sternman_engine import SternmanEngine


class Palindrome(Car):
    def __init__(self, last_service_date, warning_light_is_on):
        super().__init__(last_service_date)
        self.last_service_date = last_service_date
        self.warning_light_is_on = warning_light_is_on
        self.engine = SternmanEngine(last_service_date, warning_light_is_on)
        self.battery = SpindlerBattery(last_service_date, datetime.today().date())

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.engine.needs_service():
            return True
        else:
            return False
