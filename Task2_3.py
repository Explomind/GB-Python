# Дана строка текста. Напишите программу для подсчета стоимости строки, исходя из того,
# что один любой символ (в том числе пробел) стоит 60 копеек. Ответ дайте в рублях и копейках.

def cost_string(text):
    cost_full = len(text) * 60
    cost_rub = cost_full // 100
    cost_kop = cost_full % 100
    print(f'Cost of the text: {cost_rub} rub {cost_kop} kop')


text_str = input('Input text: ')
cost_string(text_str)
