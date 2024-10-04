from pprint import pprint

import requests
import pandas as pd

# Get => Like Browser / read object
# Post => Form / create object
# Delete => delete object
# Put => update object

# response = requests.get('https://de.wikipedia.org/wiki/Python_(Programmiersprache)')
# data = response.text

results = pd.read_html('https://de.wikipedia.org/wiki/Python_(Programmiersprache)')
for result in results:
    for index, line in result.iterrows():
        print(line)


