# ввод данных пользователем и запись в файл

def input_data():
    name = input('Name: ')
    surname = input('Surname: ')
    phone = input('Phone number: ')
    comment = input('Comment: ')
    return [name, surname, phone, comment]


def write_data_one_string(data):
    data_str = ''
    for each in data:
        data_str += each + ';'
    data_str += '\n'
    with open('data_os.csv', 'a') as file:
        file.write(data_str)


def write_data_dif_string(data):
    with open('data_ds.csv', 'a') as file:
        for each in data:
            file.write(each)
            file.write('\n')
