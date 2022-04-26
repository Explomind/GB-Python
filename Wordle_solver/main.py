import user_interface as ui
import model as m


def seek_words():
    grey_letters = ui.input_grey()
    data = m.first_filter(grey_letters)
    while True:
        choice = ui.menu()
        if choice == '1':
            green_letters = ui.input_green()
            data = m.green_letters_filter(data, green_letters)
        elif choice == '2':
            yellow_letters = ui.input_yellow()
            data = m.yellow_letters_filter(data, yellow_letters)
        elif choice == '3':
            grey_letters = ui.input_grey(grey_letters)
            data = m.grey_letters_filter(data, grey_letters)
        elif choice == '4':
            print(data)
            input()
        elif choice == '5':
            break


seek_words()
