import requests
from string import ascii_uppercase as alphabet


def func1(x, y):
    return x * y


def func2(x, y):
    return x / y


def func3(a, b):
    return a == b


def func4(a):
    param_type = type(a)
    print(param_type)
    if param_type == int:
        a *= 2
        return a


def func5(a_text, a_word):
    return a_word in a_text


def func6(url):
    try:
        resp = requests.get(url)
    except requests.exceptions.ConnectionError:
        return 'Ko'

    else:
        return 'Ok'


def func7(a_list: list):
    if type(a_list) is list:
        return len(a_list)
    else:
        raise Exception(f'Invalid parameter list awaited but {type(a_list)} received')


def func8(ver, text):
    encoded_text = ''

    for letter in text:
        if letter not in alphabet:
            encoded_text += letter
        else:
            letter_position = alphabet.index(letter)
            letter_position += ver
            if letter_position > 25:
                letter_position -= 26
            encoded_text += alphabet[letter_position]
    return encoded_text


if __name__ == '__main__':
    result = func1(4, 5)
    print(f'result = 20? {result == 20}')

    result = func2(20, 10)
    print(f'result = 2? {result == 2}')

    # Func3 check if 2 parameters have the same value
    result = func3(a=10, b=10)
    print(f'result = True? {result == True}')
    result = func3(a=5, b='5')
    print(f'result = True? {result == False}')

    # Func4 print the type from the parameter, and if it is an int it gives back its double (*2)
    result = func4(a=10)
    print(f'result = 20? {result == 20}')
    result = func4(a='abc')
    print(f'result = None? {result == None}')

    # Func5 take one text and one word and give back if the word is in the text
    result = func5(
        a_text='''If you set your goals ridiculously high and it\'s a failure,
         you will fail above everyone else\'s success''',
        a_word='fail'
    )

    print(f'result = True? {result == True}')

    # Func6 take an url as parameter and if the website is working it give back 'Ok' else 'Ko' # requests.get()
    result = func6(url='https://google.fr')
    print(f'result = Ok? {result == "Ok"}')
    result = func6(url='https://goxogle.fr')
    print(f'result = Ko? {result == "Ko"}')

    # Func7 take as parameter a list and give back its length, if this is not a list
    # it should raise an Exception('Invalid parameter list awaited but xxx received')
    result = func7(a_list=['a', 'b', 'c'])
    print(f'result = 3? {result == 3}')

    try:
        result = func7(a_list='abc')
    except Exception as e:
        print(f'Exception = Invalid? {"Invalid" in e.__str__()}')

    # Func8 take a text and a number as parmeter, it give back a new string with all letter moved from x letters
    # Example with 'GOOD MORNING' and 1 => HPPE NPSJOH
    result = func8(3, text='GOOD DAY')
    print(f'result = JRRG GDB? {result == "JRRG GDB"}')

    # Func9 receive as parameter a dict and a text, and give back each letter
    # replaced from the value from the dict (if in the dict)
    result = func9(text='Good Morning', tranlate_dict={'g': 't', 'r': 'z'})
    print(f'result = Tood Moznint {result == "Tood Moznint"}')
