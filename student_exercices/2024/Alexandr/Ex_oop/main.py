from location import Location
from location_sample import  LocationSample
from list_location_provider import ListLocationProvider

geneve = Location(46.2044, 6.1432)
lausanne = Location(46.517738, 6.632233)
ls1 = LocationSample(lausanne, date=1615806676)
ls2 = LocationSample(geneve, date=1605804670)
lst_locations = ListLocationProvider([ls1, ls2])
lst_loc_ids = [id(loc) for loc in lst_locations.get_location_samples()]
print(lst_locations.print_location_samples())

memes_ids = []
for ls in ls1, ls2:
    vraie_id = id(ls)
    meme_id = vraie_id in lst_loc_ids
    memes_ids.append(meme_id)
if sum(memes_ids) == 0:
    print("On travaille en securite: tous les identifiants sont differents.")
else:
    print("Le programme n'est pas sur.")