from location import Location


class LocationSample:
    def __init__(self,  loc: Location, date: int,):
        self.__date = date
        self.__loc = loc

    def __str__(self):
        return f"LocationSample [timestamp:{self.__date}, Location:{self.__loc}]"

    def __repr__(self):
        return self.__str__()

    def get_date(self):
        return self.__date

    def get_loc(self):
        return self.__loc

    def __lt__(self, other):
        if not isinstance(other, LocationSample):
            return NotImplemented
        return self.__date < other.__date

    def distance_spatiale(self, other: Location):
        return self.get_loc().distance(other)
