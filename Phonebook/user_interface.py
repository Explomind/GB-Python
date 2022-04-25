def menu_choice():
    while True:
        menu_text = ('1 - input data',
                     '2 - show data, form 1',
                     '3 - show data, form 2',
                     '4 - quit')
        for each in menu_text:
            print(each)
        choice = input('Choose action: ')
        menu_items = '1234'
        if choice in menu_items:
            return choice
        else:
            print('Incorrect input!', '\n')

# menu_choice()
