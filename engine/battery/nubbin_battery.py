from abc import ABC
from datetime import datetime, timedelta
from battery import Battery


class NubbinBattery(Battery, ABC):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date)
        self.current_date = current_date

    def needs_service(self):
        # every 4 years
        if self.current_date - self.last_service_date > timedelta(days=1460):
            return True
        else:
            return False
