# 09-10-2025:
# 1) Trouver une API publique,
import json
from pprint import pprint

import requests

base_url = "https://official-joke-api.appspot.com/"

endpoints = [
    'jokes/random'
    # , 'jokes/ten'
]

# 2) Executer plusieurs requêtes dessus avec des paramètres

# for endpoint in endpoints:
#
#     resp = requests.get(f'{base_url}{endpoint}')
#     joke_dict = resp.json()
#
#     del joke_dict['id']
#     del joke_dict['type']
#
#
#     for key, value in joke_dict.items():
#         print(f'{key.title()}: {value}')



# 3) Faire un traitement sur les données (affichage, tri, modification)

saved_id = None
counter = 0

while True:
    counter +=1

    if counter % 50 == 0:
        print(f'Loop {counter}')

    resp = requests.get(f'{base_url}jokes/random')
    if resp.status_code != 200:
        print(resp.text)
        exit()

    joke_id = resp.json()['id']

    if not saved_id:
        saved_id = joke_id

    elif saved_id == joke_id:
        break



print(counter)