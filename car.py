from abc import abstractmethod
from engineclass import Engine

from serviceable import Serviceable
from battery import Battery

class Car(Serviceable):
    engine = Engine()
    battery = Battery()
    def __init__(self, last_service_date):
        super().__init__(last_service_date)
        self.last_service_date = last_service_date


    @abstractmethod
    def needs_service(self):
        pass
