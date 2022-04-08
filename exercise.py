from string import ascii_lowercase

if __name__ == '__main__':

    # List 0-100

    my_list = list(range(101))

    list_3 = []
    for value in my_list:
        if value % 3 == 0:
            list_3.append(value)

    list_s7 = []
    for value in list_3:
        if '7' not in str(value):
            list_s7.append(value)


    # [[0,3,6], [9,12,15], ...]
    list_complexe = []
    sub_list = None

    for index, value in enumerate(list_s7):
        if index % 5 == 0:
            if sub_list is not None:
                list_complexe.append(sub_list)
            sub_list = [value]
        else:
            sub_list.append(value)

    print(list_complexe)



