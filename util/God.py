from model.War_airplane import War_airplane
from model.Piece_airplane import Piece_airplane
from random import randint

class God():
    def create():
        airline_1 = [War_airplane("IL-2", "War airplane", 3, 10),
                     Piece_airplane("SY-100", "Piece airplane", 500, 10000),
                     Piece_airplane("SY-82", "Piece airplane", 300, 5000)]
        airline_2 = [War_airplane("FE-14", "War airplane", 4, 30),
                     War_airplane("JET-18", "War airplane", 3, 15),
                     Piece_airplane("SY-72", "Piece_airplane", 250, 3000)]
        list_airlines = [airline_1, airline_2]
        return list_airlines
