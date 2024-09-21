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
    # _x__ ___ _x__
    # axbd abc axcd

    new_quote_hidden = ''
    for index, symbol in enumerate(quote):
        if symbol.lower() == user_letter:
            new_quote_hidden += quote[index]
        else:
            new_quote_hidden += quote_hidden[index]

    return new_quote_hidden


def draw_hangman(remaining_lives):
    print('x')


if __name__ == '__main__':

    # Get all quotes from api
    api_url = 'https://api.chucknorris.io/jokes/random'
    quote_dict = get_quotes(api_url)
    visible_quote = quote_dict['value']
    # words = quote.split()
    # visible_quote = ''
    # for word in words:
    #     if len(visible_quote) < 50:
    #         visible_quote += f' {word}'
    # visible_quote = visible_quote[1:]

    for symbol in '!.?':
        if symbol in visible_quote:
            visible_quote = visible_quote.split(symbol)[0] + symbol
    hidden_quote = generate_hidden_quote(visible_quote)

    lives = 6
    guessed_letters = ''

    # solange das Spiel läuft
    while lives > 0 and '_' in hidden_quote:
        print(f'{hidden_quote} | Lives : {lives}/6'),

        while True:
            guess = input('Letter : ')
            if guess in guessed_letters:
                print(f'Letter {guess} already tried')
            elif guess not in alphabet:
                print(f'Letter {guess} is not a letter')
            elif len(guess) != 1:
                print(f'Only one letter at the time!')
            elif guess:
                guessed_letters += guess
                break

        if guess in visible_quote.lower():
            hidden_quote = show_letter(guess, hidden_quote, visible_quote)
        else:
            draw_hangman()
            lives -= 1

    if lives > 0:
        print(f'You won, the quote to find was: *{visible_quote}*')
    else:
        print(f'You lost, the quote to find was: *{visible_quote}*')
