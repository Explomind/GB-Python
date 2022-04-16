# Напишите программу, удаляющую из текста все слова содержащие "абв".

def del_words(any_text, any_word):
    tmp_list = list(filter(lambda word: any_word not in word, any_text.split()))
    return ' '.join(tmp_list)


with open('Task5_6.txt', 'r+') as file:
    old_text = file.read()
    file.write('\n')
    file.write(del_words(old_text, 'абв'))
