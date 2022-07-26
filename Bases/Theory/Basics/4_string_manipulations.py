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
    print(' === formatting === ')
    age = 34
    firstname = 'Pierre'

    print(f'Je m\'appelle {firstname} et j\'ai {age} ans.')
    print('Je m\'appelle %s et j\'ai %s ans.' % (firstname, age))

    data_dict = {'firstname': firstname, 'age': age, 'nationality': 'CH'}
    print('Je m\'appelle %(firstname)s et j\'ai %(age)s ans.' % data_dict)

    # Don't do it at home!
    print('Je m\'appelle ' + firstname + ' et j\'ai ' + str(age) + ' ans.')

    # Ugly way only for print
    print('Je m\'appelle', firstname, 'et j\'ai', age, 'ans.')
    
