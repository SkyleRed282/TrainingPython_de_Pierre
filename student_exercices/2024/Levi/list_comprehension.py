from pprint import pprint

n_list = [n for n in range(100, -1, -1)]

n_list2 = [n for n in n_list if n % 2 == 0]
n_list3 = [n for n in n_list2 if '7' not in str(n)]
n_list4 = [n for n in n_list3 if n % 6 == 0]

n_list5 = [n for n in n_list4 if n > 9 and n < 100]

# {'9':6, ... , '1':2}
n_dict1 = {str(n)[0]: int(str(n)[1]) for n in n_list5}

n_dict2 = {value: key for key,value in n_dict1.items()}
pprint(n_dict2)
