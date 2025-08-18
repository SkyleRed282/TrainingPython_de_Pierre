from pprint import pprint

dogs_data = [
    {
        'nom': 'Rex',
        'nb_pattes': 4,
        'age_ans': 5.3,
        'nourriture': ['viande', 'croquettes', 'canapé']
    },
    {
        'nom': 'Rocky',
        'nb_pattes': 4,
        'age_ans': 2.3,
        'nourriture': ['poisson', 'croquettes', 'glaces']
    }
]

del dogs_data[0]['nourriture'][2]
dogs_data[1]['is_male'] = False

# reverse
dogs_data[1]['nourriture'].append('cookie')

del dogs_data[1]['nourriture']
pprint(dogs_data)

