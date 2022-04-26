import user_interface as ui
import data_input as di
import data_output as do


def start():
    welcome_text = 'телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах'
    print(welcome_text)
    while True:
        choice = ui.menu_choice()
        if choice == '1':
            data = di.input_data()
            print(*data, '\n')
            di.write_data_one_string(data)
            di.write_data_dif_string(data)
        elif choice == '2':
            do.print_data('data_os.csv')
        elif choice == '3':
            do.print_data('data_ds.csv')
        elif choice == '4':
            break
