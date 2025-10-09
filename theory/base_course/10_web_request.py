import datetime
import json
from pprint import pprint

import requests
import pandas as pd

# CRUD => Create Read Update Delete

# Get => Like Browser / read object
# Post => Form / create object
# Delete => delete object
# Put => update object

# response = requests.get('https://sports.orange.fr/football/ligue-1/classement-equipes.html')
# data = response.text
# print(data)


# results = pd.read_html('https://sports.orange.fr/football/ligue-1/classement-equipes.html')
# for result in results:
#     for index, line in result.iterrows():
#         print(line)

# Example API https://github.com/shevabam/breaking-bad-quotes?tab=readme-ov-file

resp = requests.get('https://api.breakingbadquotes.xyz/v1/quotes/5')
list_quotes = resp.json()

# for quote_dict in list_quotes:
#     print(
#         quote_dict["quote"][:30],
#         '...' if len(quote_dict["quote"]) > 30 else '',
#         'from',
#         quote_dict["author"]
#     )



