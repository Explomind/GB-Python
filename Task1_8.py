# Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У

X = int(input('Input coordinate X: '))
Y = int(input('Input coordinate Y: '))
if X == 0 and Y == 0:
    print('The point is in the origin of coordinates.')
elif X == 0:
    print('The point is on X axis.')
elif Y == 0:
    print('The point is on Y axis.')
elif X > 0 and Y > 0:
    print('The point is in the first quarter.')
elif X < 0 and Y > 0:
    print('The point is in the second quarter.')
elif X < 0 and Y < 0:
    print('The point is in the third quarter.')
elif X > 0 and Y < 0:
    print('The point is in the fourth quarter.')    
    