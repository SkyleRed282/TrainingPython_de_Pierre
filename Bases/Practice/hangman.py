import requests
from random import sample
import string


def get_quotes(url):
    # Make a GET request and get response data
    response = requests.get(url)

    # parse json and get the quote list back
    data = response.json()
    return data


def generate_hidden_quote(text):

    # replace all alphabetic signs with _
    for letter in string.ascii_letters:
        text = text.replace(letter, '_')

    # Return hidden quote
    return text


if __name__ == '__main__':

    # Get all quotes from api
    api_url = 'https://type.fit/api/quotes'
    all_quotes = get_quotes(api_url)

    # extract one quote text

    # print(type(all_quotes))
    print(len(all_quotes))

    chosen_quote = sample(all_quotes, 1)
    # print(chosen_quote)

    dict_chosen_quote = chosen_quote[0]

    # print(dict_chosen_quote)
    # print(type(dict_chosen_quote))

    chosen_quote_text = dict_chosen_quote.get('text')
    # print(chosen_quote_text)

    # generate hidden version of the quote
    hidden_quote = generate_hidden_quote(chosen_quote_text)
    print(hidden_quote)

    life_amount = 5

    # While life > 0 and not all letter have been found
    while life_amount > 0 and hidden_quote.count('_') > 0:
        # ask user for a letter
        chosen_letter = input('Choose a letter: ')
        # if letter not in quote, remove a life
        if chosen_quote_text.count(chosen_letter) == 0:
            life_amount -=1
            print(f'{chosen_letter} is not in the quote')
        # else display letter in hidden quote
        else:
            # display in hidden quote, the found letter
            # loop on chosen_quote, if letter matches,
            # replace _ with the letter in the hidden quote

    # tell the user weather he won or lost