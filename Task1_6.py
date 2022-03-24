# Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.

day_number = int(input('Input day of the week number: ')) - 1
day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
if 0 <= day_number < 5:
    print(f'{day_names[day_number]} is weekday')
elif 5 <= day_number < 7:
    print(f'{day_names[day_number]} is weekend!')
else: print("There are only 7 days in week on Earth!")    
