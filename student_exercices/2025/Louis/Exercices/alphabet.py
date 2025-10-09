

def get_position_letter(text:str, letter:str):
    return text.find(letter)

if __name__ == '__main__':

    print(get_position_letter('abcd', 'c'))
    print(get_position_letter('abcd', 'f'))

