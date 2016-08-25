from model.Aeroflot import Aeroflot

class Airplane_count():
    def result(list_airlines):
        pos = 1
        x = 0
        for airline in list_airlines:
            for airplane in airline:
                x += airplane.count_passenger

            print("Airline #", pos, "common count passenger:", x)
            pos += 1
            x = 0
        
        return x 
