if __name__ == '__main__':

    with open(file='numbers_1_100.txt', mode='r') as file_pointer:
        number_as_text = file_pointer.read()

    print(number_as_text)
