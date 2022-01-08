
def say_hello(name):
    print(f'Hello {name}')


def ask_age():
    return input('Age?')


if __name__ == '__main__':

    say_hello('Pierre')

    age = ask_age()
    print(f'You are {age} year(s) old')
