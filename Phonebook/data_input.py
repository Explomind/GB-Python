# ввод данных пользователем и запись в файл

def input_data():
    name = input('Name: ')
    surname = input('Surname: ')
    phone = input('Phone number: ')
    comment = input('Comment: ')
    data = '{0};{1};{2};{3}\n'.format(name, surname, phone, comment)
    with open('data.csv', 'a') as file:
        file.write(data)
    return (name, surname, phone, comment)

# print(input_data())
