from abc import ABC
from datetime import timedelta

from battery import Battery


class SpindlerBattery(Battery, ABC):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date)
        self.current_date = current_date

    def needs_service(self):
        # every 2 years
        if self.current_date - self.last_service_date > timedelta(days=730):
            return True
        else:
            return False
