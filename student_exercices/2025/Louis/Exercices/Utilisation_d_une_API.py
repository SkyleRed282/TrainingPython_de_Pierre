import requests

# 1) Trouver une API publique

name = ''
while name == '':
    name = input('Donnez un nom : ').strip()

# 2) Executer plusieurs requêtes dessus avec des paramètres

resp = requests.get(f'"https://api.agify.io?name="{name}')
answer = resp.json()


# 3) Faire un traitement sur les données (affichage, tri, modification)
del answer['count']

for key, value in answer.items():
    print(f'{key.title()}: {value}')