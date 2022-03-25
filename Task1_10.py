# Найти расстояние между двумя точками пространства

X_1 = int(input('Input X coordinate of the first point: '))
Y_1 = int(input('Input Y coordinate of the first point: '))
X_2 = int(input('Input X coordinate of the second point: '))
Y_2 = int(input('Input Y coordinate of the second point: '))
dist = ((X_1 - X_2) ** 2 + (Y_1 - Y_2) ** 2) ** 0.5
print(f'Distance between the points = {round(dist, 2)}')
