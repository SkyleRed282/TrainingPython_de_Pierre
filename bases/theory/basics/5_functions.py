def say_hello(name: str = 'Lucas') -> None:
    """
    Say hello to with a given name
    """
    print(f'Hello {name} ')


def ask_age() -> str:
    """
    Ask the user for his age and return it
    """
    user_age = input('Age?')
    return user_age


def say_hello_mp(name, age_user=25):
    """
    Say hello to with a given name and age
    """
    print(f'Hello {name} {age_user}')


# *args and **kwargs are standard names for those special parameters
def args_and_kwargs(*positional_argument, **keyword_argument):
    """
    Print the list of kwargs and args
    """
    print(type(positional_argument), positional_argument)
    print(type(keyword_argument), keyword_argument)


def sum_example(*positional_argument):
    """
    Return the sum of any number of positional arguments
    """
    return sum(positional_argument)


if __name__ == '__main__':
    print('\n# Use default value')
    say_hello()

    print('\n# passed value with wrong type')
    say_hello(123)

    print('\n# function without return')
    print(say_hello('Pierre'))

    print('\n# variable order inversion')
    say_hello_mp(age_user=23, name='toto')
    say_hello_mp('toto', 23)

    print('\n# user input')
    age = ask_age()
    print(f'You are {age} year(s) old')

    print('\n# *args + **kwargs')
    args_and_kwargs(1, 3, 5, 6, 7, x=1, y=2, z=3)

    print('\n# Sim ')
    print(sum_example(1, 3, 5, 6, 7))
