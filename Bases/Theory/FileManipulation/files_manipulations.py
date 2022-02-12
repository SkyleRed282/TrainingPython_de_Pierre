import os

if __name__ == '__main__':

    # print(type(file_data),file_data)

    # with open('contacts.csv') as file_pointer:
    #     # for x in file_pointer:
    #     #     print(x, type(x))
    #     file_data = file_pointer.read()

    # with open('contacts.bin', 'wb') as file_pointer:
    #     file_pointer.write(file_data.encode())
    #     # print(file_data.encode())

    # for x in range(10):
    #     file_name = f'{x}.txt'
    #
    #     value_to_write = x
    #
    #     if os.path.exists(file_name):
    #         with open(file_name) as file_pointer:
    #             list_lines = file_pointer.readlines()
    #
    #         if len(list_lines) > 0:
    #             last_value = int(list_lines[-1])
    #             value_to_write = last_value + 1
    #
    #     with open(file_name, 'a') as file_pointer:
    #         file_pointer.write(f'{value_to_write}\n')

    with open('contacts.csv') as file_pointer:
        list_lines = file_pointer.readlines()
    headers = list_lines[0].replace('\n', '').split(',')

    for line in list_lines[1:]:
        line_list = line.replace('\n', '').replace(', ', ' ').split(',')
        print(line_list)
