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

dogs_data[0]['nourriture'][1] = 'salade'
print(dogs_data)
