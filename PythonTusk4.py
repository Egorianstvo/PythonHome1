# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).

part_n = int(input('Сколько долек в длину? '))
part_m = int(input('Сколько долек в ширину? '))
part_k = int(input('Сколько долек нужно отломить? '))

if (part_k % part_n == 0 or part_k % part_m == 0) and part_k <= part_n * part_m:
    print('YES')
else:
    print('NO')