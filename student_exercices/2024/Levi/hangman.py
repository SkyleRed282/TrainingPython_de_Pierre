from pprint import pprint
from string import ascii_lowercase as alphabet

import requests
from random import sample
import string


def get_quotes(url):
    # Make a GET request and get response data
    response = requests.get(url)

    # parse json and get the quote list back
    data = response.json()
    return data


def generate_hidden_quote(text: str):
    hidden_text = ''

    for symbol in text:
        if symbol.lower() in alphabet:
            hidden_text += '_'
        else:
            hidden_text += symbol

    return hidden_text


def show_letter(user_letter, quote_hidden, quote):



    return quote_hidden


if __name__ == '__main__':

    # Get all quotes from api
    api_url = 'https://api.chucknorris.io/jokes/random'
    quote_dict = get_quotes(api_url)
    visible_quote = quote_dict['value']
    hidden_quote = generate_hidden_quote(visible_quote)

    lives = 6
    # solange das Spiel läuft
    while lives >0 and '_' in hidden_quote:

        # Ask for a letter while the letter is valid (only one letter)
        show_letter(guess, hidden_quote, visible_quote)
        print(hidden_quote)


