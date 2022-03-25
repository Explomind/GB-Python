# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат 
# (Попробовать решить с помощью таблицы истинности)

print('Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат')
print(f'X\tY\tZ\t¬(X ⋁ Y ⋁ Z)\t¬X ⋀ ¬Y ⋀ ¬Z')
for X in [True, False]:
    for Y in [True, False]:
        for Z in [True, False]:
            print(f'{X}\t{Y}\t{Z}\t  {not(X or Y or Z)}\t\t  {not X and not Y and not Z}')
