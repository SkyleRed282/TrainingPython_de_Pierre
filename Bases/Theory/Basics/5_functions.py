def say_hello(name: str = 'Lucas'):
    print(f'Hello {name} ')


def ask_age():
    user_age = input('Age?')
    return user_age


def say_hello_mp(name, age_user=25):
    print(f'Hello {name} {age_user}')


if __name__ == '__main__':

    # use default value
    say_hello()

    # passed value with wrong type
    say_hello(123)

    # function without return
    print(say_hello('Pierre'))

    # variable order inversion
    say_hello_mp(age_user=23, name='toto')
    say_hello_mp('toto', 23)

    # user input
    age = ask_age()
    print(f'You are {age} year(s) old')

    # TODO **args + **kwargs
