if __name__ == '__main__':

    # slicing
    my_str = 'abcdefghax'
    print(my_str[0:3])
    print(my_str[0])
    print(my_str[-1])
    print(my_str[3:6])
    print(my_str[::2])
    print(my_str[::-1])

    print(my_str.replace('a', 'z'))

    my_str = 'Bonjour à tous'
    print(my_str.split())

    # formating
    age = 34
    prenom = 'Pierre'
    print(f'Je m\'appelle {prenom} et j\'ai {age} ans.')
    print('Je m\'appelle ' + prenom + ' et j\'ai ' + str(age) + ' ans.')
    print('Je m\'appelle ', prenom, ' et j\'ai ', age, ' ans.')
    print('Je m\'appelle %s  et j\'ai %s ans.' % (prenom, age))
