from abc import abstractmethod
from engineclass import Engine

from serviceable import Serviceable
from battery import Battery


class Car(Serviceable):

    def __init__(self, last_service_date):
        super().__init__(last_service_date)
        self.engine = Engine(last_service_date)
        self.battery = Battery(last_service_date)

    @abstractmethod
    def needs_service(self):
        pass
