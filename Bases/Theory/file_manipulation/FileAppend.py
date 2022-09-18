from string import ascii_lowercase as alphabet


if __name__ == '__main__':

    for letter in alphabet:
        with open('alphabet.txt', 'a') as file_pointer:
            file_pointer.write(letter)
