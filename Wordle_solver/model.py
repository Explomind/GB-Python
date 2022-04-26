def first_filter(grey_letters):
    data = []
    with open('words.txt', 'r') as file:  # чтение слов из файла с фильтром по первой букве
        while True:
            line = file.readline()
            if not line:
                break
            if line[0] not in grey_letters:
                data.append(line.split())
    return data

def grey_letters_filter(data, grey_letters):   # фильтрация по "серым" буквам
    result = []
    for string in data:
        for word in string:
            is_found = False  # проверка есть ли "серая" буква в слове
            for i in range(len(grey_letters)):
                if grey_letters[i] in word:
                    is_found = True
                    break
            if not is_found:
                result.append(word)
    return result

def yellow_letters_filter(data, yellow_letters):   # фильтрация по "желтым" буквам
    result = []
    for string in data:
        for word in string:
            is_found = True  # проверка есть ли "желтая" буква в слове
            for i in range(len(yellow_letters)):
                if yellow_letters[i] not in word:
                    is_found = False
                    break
            if is_found:
                result.append(word)
    return result

def seek_words(green_letters, yellow_letters, grey_letters):
    data = first_filter(grey_letters)
    data = grey_letters_filter(data, grey_letters)
    data = yellow_letters_filter(data, yellow_letters)

    print(data)
