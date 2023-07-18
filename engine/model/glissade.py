from datetime import datetime

from engine.battery.spindler_battery import SpindlerBattery
from engine.willoughby_engine import WilloughbyEngine


class Glissade(WilloughbyEngine,SpindlerBattery):
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
