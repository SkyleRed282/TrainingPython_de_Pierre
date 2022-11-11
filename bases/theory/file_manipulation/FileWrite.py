if __name__ == '__main__':

    # Write numbers between 1 and 100 in a file
    with open(file='numbers_1_100.txt', mode='w') as file_pointer:
        numbers_as_text = ''
        for number in range(1, 101):  # [1, 2, 3, ... , 100]
            numbers_as_text += f'{number}\n'

        file_pointer.write(numbers_as_text)
