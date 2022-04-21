# Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# входные и выходные данные хранятся в отдельных текстовых файлах

def compress(data):
    count = 1
    result = ''
    for i in range(1, len(data)):
        if data[i - 1] == data[i]:
            count += 1
        else:
            result += str(count) + data[i - 1]
            count = 1
    return result + str(count) + data[i]


def decompress(data):
    result = ''
    for i in range(0, len(data), 2):
        result += data[i + 1] * int(data[i])
    return result


with open('Task5_10_in.txt', 'r') as file:
    data = file.read()
print('{}\tlength: {}'.format(data, len(data)))
data = compress(data)
print('{}\tlength after compression: {}'.format(data, len(data)))
with open('Task5_10_out.txt', 'w') as file:
    file.write(data)
with open('Task5_10_out.txt', 'r') as file:
    data = file.read()
data = decompress(data)
print('{}\tlength after decompression: {}'.format(data, len(data)))
