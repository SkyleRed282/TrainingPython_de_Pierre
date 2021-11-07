if __name__ == '__main__':

    # for each
    # for l in 'abcd':
    #     print(l)
    #
    # conteur = 0
    # while conteur < 6:
    #     print(conteur)
    #     conteur+=1
    #
    # for index, l in enumerate('abcd'):
    #     print(f'{index} - {l}')
    #
    my_dict = {
        'cle1':1,
        'cle2':2
    }
    for key, value in my_dict.items():
        print(f'{key} - {value}')

    for value in my_dict.values():
        print(f'{value}')

    print(my_dict.keys())
