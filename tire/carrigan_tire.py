from tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self, wear_array):
        self.wear_array = wear_array
    
    def needs_service(self):
        for value in self.wear_array:
            if value >= 0.9:
                return True
        return False