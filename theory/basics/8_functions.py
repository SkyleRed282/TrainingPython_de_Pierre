import datetime
import random


def say_hello(name: str = 'Lucas') -> None:
    """
    Say hello to with a given name
    :param name: optional name from someone
    :return: None
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
def args_and_kwargs(*positional_arguments, **keyword_arguments):
    """
    Print the type and the list of kwargs and args
    """
    print(type(positional_arguments), positional_arguments)
    print(type(keyword_arguments), keyword_arguments)


def sum_example(*positional_arguments):
    """
    Return the sum of any number of positional arguments
    """
    result = 0
    for param in positional_arguments:
        result += param

    return result


def exemple_mix_positional(operation: str, *numbers):
    if operation == '+':
        print(sum(numbers))
    else:
        print(f'Operation {operation} non supportée')




def list_shuffle(some_list: list) -> None:
    """
    This function shuffle a given list
    """
    # if some_list is not None and not empty
    if some_list:
        random.shuffle(some_list)


def current_time() -> None:
    """
    This function print the current date time
    """
    print(datetime.datetime.now().isoformat())


def current_time_iso() -> str:
    """
    This function return the current date time
    """
    return datetime.datetime.now().isoformat()


if __name__ == '__main__':

    # No return no parameter
    print("\nNo return no parameter")
    print(current_time())

    # No return, one parameter
    print("\nNo return, one parameter")
    my_list = list(range(10))
    print(list_shuffle(my_list), my_list)

    # Return, without parameter
    print("\nReturn, no parameter")
    print(type(current_time_iso()), current_time_iso())

    # print('\n# Use default value')
    # say_hello()
    #
    # print('\n# passed value with wrong type')
    # say_hello(123)
    #
    # print('\n# function without return')
    # returned_value = say_hello('Pierre')
    # print(returned_value)
    #
    # print('\n# variable order inversion')
    # say_hello_mp(age_user=23, name='toto')
    # say_hello_mp('toto', 23)
    #
    # print('\n# user input')
    # age = ask_age()
    # print(f'You are {age} year(s) old')
    #
    # print('\n# *args + **kwargs')
    # args_and_kwargs(1, 3, 5, 6, 7, x=1, y=2, z=3)
    #
    # print('\n# Sum')
    # print(sum_example(1, 3, 5, 6, 7))

    # exemple_mix_positional('+', 1, 2, 3, 4, 5, 6, 7, 8)
