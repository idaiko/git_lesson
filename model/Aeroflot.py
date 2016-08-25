class Aeroflot():
    def __init__(self, modele, airplane_type, count_passenger):
        self.__modele = modele
        self.__airplane_type = airplane_type
        self.__count_passenger = count_passenger

    @property
    def modele(self):
        return self.__modele

    @property
    def airplane_type(self):
        return airplane_type

    @property
    def count_passenger(self):
        return self.__count_passenger
    @count_passenger.setter
    def count_passenger(self, value):
        if value > 0:
            self.__count_passenger = value
