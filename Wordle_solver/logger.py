# запись отгаданных слов

def log_words():
    word = input('Введите отгаданное слово: ') + '\n'
    if word.split():
        with open('log.txt', 'r') as file:
            data = file.read()
            if word in data:
                return
        with open('log.txt', 'a') as file:
            file.write(word)


def random_word():
    from random import randint
    data = []
    with open('log.txt', 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            data.append(line)
    word_number = randint(0, len(data) - 1)
    return data[word_number]
