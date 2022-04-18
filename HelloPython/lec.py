# # Input and output
#
# # print('hello, world')
# value = None
# print(type(value))
# a = 123
# b = 1.23
# print(type(a))
# print(type(b))
# value = 345
# print(type(value))
# s = 'hello "world"'
# s2 = "hello \nworld"
# print(a, '-', b, '-', s, '-', s2)
# print('{1} - {2} - {0}'.format(a, b, s))
# print(f'{a} - {b} - {s}')
# f = True
# print(f)
# list = ['1', '2', '3']
# print(list)
# col = [4, 5.6, True]
# print(col)
# # print('Input x:')
# # x = int(input())
# # print('Input y:')
# # y = float(input())
# # print(x, y, 'x+y=', x+y)
# # print('type of x+y:', type(x+y))
# # print(f'{x} {y}')
#
# # Arithmetic operations
# # +, -, *, /, % - остаток от деления, // - целочисленное деление, ** - возведение в степень
# a = 1.3
# b = 3
# c = round (a * b, 2)
# print(c)
# b += 5
# print(b)
#
# # Logic operations
# # >, <, >=, <=, ==, !=
# # not, and, or
# # is, is not, in, not in
# # gen
#
# d = 1 < 3 < 5 < 10
# print(d)
# f = [1, 2, 3, 4]
# print(f)
# print(2 in f)
# print(not 2 in f)
#
# is_odd = f[0] % 2 == 0 # equal to is_odd = not f[0] % 2
# print(is_odd)
# is_odd = not f[0] % 2
# print(is_odd)
#
# # strings
# text = '0123456789'
# print(text[0:len(text):6])
# print(text[::6])
# print(text[2:6])

# def calc(x):
#     return x * 10
#
# def math(op, x):
#     print(op(x))
#
# math(calc, 10)

# def sum(x, y):
#     return x + y

# sum = lambda x, y: x + y
#
# def mult(x, y):
#     return x * y

# def calc(op, a, b):
#     return op(a, b)
#
# # f = sum
#
# print(calc(lambda x, y: x + y, 4, 10))

# list = [(i, i) for i in range(1, 21) if i % 2 == 0]
# print(list)

# with open('lec.txt', 'r') as file:
#     data = file.read() + ' '
# any_list = []
# while data != '':
#     space_pos = data.index(' ')
#     any_list.append(int(data[:space_pos]))
#     data = data[space_pos + 1:]
# new_list = [(i, i ** 2) for i in any_list if i % 2 == 0]
# print(new_list)

# def select(f, col):
#     return [f(x) for x in col]
#
# def where(f, col):
#     return [x for x in col if f(x)]
#
# data = '1 2 3 5 8 15 23 38'.split()
# res = select(int, data)
# print(res)
# res = where(lambda x: not x % 2, res)
# print(res)
# res = select(lambda x: (x, x ** 2), res)
# print(res)

# li = [x for x in range(1, 20)]
# li = list(map(lambda x: x * 2, li))
# print(li)

# data = list(map(int, '1 2 3'.split()))
# print(data)

# data = '1 2 3 5 8 15'.split()
# res = map(int, data)
# # print(res)
# res = filter(lambda x: not x % 2, res)
# # print(res)
# res = list(map(lambda x: (x, x ** 2), res))
# print(res)

# users = ['user1', 'user2', 'user3', 'user4']
# ids = [2, 3, 5, 8, 4]
# data = list(zip(ids, users))
# print(data)
# salaries = [222, 444, 555]
# data = list(zip(ids, users, salaries))
# print(data)
# data = list(enumerate(users))
# print(data)

any_list = [0, 1, 2, 3, 4, 5]
print(any_list)
any_list.insert(2, 10)
print(any_list)
