# Functions
from string import ascii_lowercase as alphabet


def func_sum(int_1: int, int_2: int) -> int:
    return int_1 + int_2


def modulo(int_1: int, int_2: int) -> int:
    return int_1 % int_2


def list_number(end: int, start: int = 1) -> list:
    return list(range(start, end + 1))


def replace_subtext(text: str, search: str, replacement: str) -> str:
    return text.replace(search, replacement)


def count_letters(text: str) -> list:
    result = [0] * 26

    for letter in text:
        index_list = alphabet.index(letter)
        result[index_list] += 1

    return result


def ask_numbers(amount: int) -> list:
    # for _ in range(3)
    list_value = []
    counter = 0
    while counter < amount:
        value = input('nummer ? ')
        list_value.append(value)
        counter += 1

    return list_value


if __name__ == '__main__':
    x = 1
    y = 2
    print(f'{func_sum(x, y)} == 3?')
    print(f'{modulo(x, y)} == 1?')
    print(f'{list_number(end=5)} == [1,2,3,4,5]?')
    print(f'{list_number(start=2, end=5)} == [2,3,4,5]?')
    print(f'{replace_subtext(text="aaaabbbcccddd", search="ab", replacement=" ")} == aaa bbcccddd?')
    print(f'{count_letters(text="aaaabbbcccdddzzb")} == [4,4,3,3,...,2]')
    print(f'{ask_numbers(3)} == [x,x,x]')

    print(f'{sum_asked_numbers()} == 10') # ask the user for numbers until he write 'stop' (input) and return their sum
    print(f'{x_random_numbers(amount=4,min=1,max=100)} == [x,x,x]') # give back x random number between min (incl) and max (excl)
    print(f'{x_random_numbers(amount=3,min=1,max=100, values=[2,3,4])}') # how much tries it takes to get given values?

