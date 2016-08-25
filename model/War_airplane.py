from model.Aeroflot import Aeroflot

class War_airplane(Aeroflot):
    def __init__(self, modele, airplane_type, count_passenger, count_rockets):
        super().__init__(modele, airplane_type, count_passenger)
        self.__count_rockets = count_rockets

    @property
    def count_rockets(self):
        return self.__count_rockets
    @count_rockets.setter
    def count_rockets(self, value):
        if value > 0:
            self.__count_rockets = value
    
