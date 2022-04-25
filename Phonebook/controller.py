import user_interface as ui
import data_input as di

def start():
    welcome_text = 'телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах'
    print(welcome_text)
    while True:
        choice = ui.menu_choice()
        if choice == '1':
            data = di.input_data()
            print(*data, '\n')
        elif choice == '2':
            print('output, form 1')
        elif choice == '3':
            print('output, form 2')
        elif choice == '4':
            break

start()
