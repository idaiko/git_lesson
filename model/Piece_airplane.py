from model.Aeroflot import Aeroflot

class Piece_airplane(Aeroflot):
    def __init__(self, modele, airplane_type, count_passenger, bagage_volume):
        super().__init__(modele, airplane_type, count_passenger)
        self.__bagage_volume = bagage_volume

    @property
    def bagage_volume(self):
        return self.__bagage_volume
    @bagage_volume.setter
    def bagage_volume(self, value):
        if value > 0:
            self.__bagage_volume = value
