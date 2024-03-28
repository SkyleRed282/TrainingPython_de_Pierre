from abc import ABC


class LocationProvider(ABC):

    def __init__(self):
        raise NotImplementedError

    def get_location_samples(self):
        raise NotImplementedError

    def print_location_samples(self):
        raise NotImplementedError
