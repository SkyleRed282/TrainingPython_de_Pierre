import math


class Location:
    def __init__(self, lat, long):
        if not (-90 <= lat <= 90):
            raise ValueError
        if not (-180 <= long <= 180):
            raise ValueError
        self.__lat = math.radians(float(lat))
        self.__long = math.radians(float(long))

    def __str__(self):
        return f"Location({self.__lat},{self.__long})"

    def distance(self, other):
        R = 6371
        return 2 * R * math.asin(math.sqrt(
            math.sin((other.__lat - self.__lat) / 2) ** 2 + math.cos(self.__lat) * math.cos(other.__lat) * math.sin(
                (other.__long - self.__long) / 2) ** 2))
