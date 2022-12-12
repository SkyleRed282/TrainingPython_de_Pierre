import random

import requests


def get_quote_from_api(url):
    response = requests.get(url)
    quote_list = response.json()
    index_quote = random.randint(0, len(quote_list)-1)
    quote_dict = quote_list[index_quote]
    return quote_dict['text']


# Wird ein Satz definiert
# Werden die leeren Buchstabenfelder der Wörter aufgeschrieben
# Dann gibt es einen Hangman, der x Wiederholungen zulässt und dann das Spiel beendet, wenn zu oft falsch geraten wurde

# Die Spieler raten Buchstaben
# Reaktion: Richtig geraten: Buchstabe kommt rein
# Rekation: Falsch geraten: Der Hangman counter wird +1 gezähglt - es wird ein Symbol am Hangman hinzugefügt

# Gewonnen, wenn der Satz voll dasteht bevor der Hangman fertig ist
# Verloren wenn der Hangman fertig ist bevor der Satz steht

if __name__ == '__main__':

    api_url = 'https://type.fit/api/quotes'
    quote = get_quote_from_api(api_url)
    print(quote)
