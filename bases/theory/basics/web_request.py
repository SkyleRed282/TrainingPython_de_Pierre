
import requests

response = requests.get('http://google.fr')

for key, value in response.__dict__.items():
    print(key, ':', value)
