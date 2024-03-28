import copy

from location_provider import LocationProvider
from location_sample import LocationSample


class ListLocationProvider(LocationProvider):

    def __init__(self, location_sample: [LocationSample]):
        self._samples = sorted(location_sample)

    def get_location_samples(self):
        return copy.deepcopy(self._samples)


    def print_location_samples(self):
        return str(self.get_location_samples())
