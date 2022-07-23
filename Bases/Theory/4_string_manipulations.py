if __name__ == '__main__':
    # slicing
    print(' === slicing === ')
    my_str = 'abcdefghax'
    print(my_str[0])
    print(my_str[-1])

    print(my_str[0:3])
    print(my_str[3:6])
    print(my_str[::2])
    print(my_str[::-1])

    print(my_str.replace('a', 'z'))
    print(my_str.index('fgh'))

    my_str = 'Hello python world!'
    print(my_str.split())

    # formating
    print(' === formating === ')
    age = 34
    prenom = 'Pierre'

    print(f'Je m\'appelle {prenom} et j\'ai {age} ans.')
    print('Je m\'appelle %s et j\'ai %s ans.' % (prenom, age))

    data_dict = {'prenom': prenom, 'age': age}
    print('Je m\'appelle %(prenom)s et j\'ai %(age)s ans.' % data_dict)

    # Don't do it at home!
    print('Je m\'appelle ' + prenom + ' et j\'ai ' + str(age) + ' ans.')

    # Ugly way only for print
    print('Je m\'appelle', prenom, 'et j\'ai', age, 'ans.')
