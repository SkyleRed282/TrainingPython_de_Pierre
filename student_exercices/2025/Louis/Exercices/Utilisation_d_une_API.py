import requests

# 1) Trouver une API publique

name = None
while name is None:
    name = input('Donnez un nom : ')


base_url = ("https://api.agify.io?name=")

# 2) Executer plusieurs requêtes dessus avec des paramètres

resp = requests.get(f'{base_url}{name}')
answer = resp.json()

del answer['count']

for key, value in answer.items():
 print(f'{key.title()}: {value}')

 # 3) Faire un traitement sur les données (affichage, tri, modification)
