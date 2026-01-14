# Définir une function qui prend un tuple  de int en entrée et retourne un
# dict avec comme clé les int et en valeur le nombre d'occurrences

#####

def get_count_dict(input_tpl:tuple):
    int_dict = {}
    for element in input_tpl:
        qty = int_dict.get(element, 0)
        int_dict[element] = qty+1

    return int_dict

#####

if __name__ == '__main__':

    numbers = (1,2,2,5,7,8,9,3,0,3,4)
    result_dict = get_count_dict(input_tpl=numbers)

    assert type(result_dict) is dict
    assert result_dict.get(2) == 2
    assert result_dict.get(9) == 1
    assert result_dict.get(6) is None


