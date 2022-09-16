# задача 1

 from sys import argv
script, x, y, z = argv
print("Имя скрипта: ", script)
print("Выработка в часах: ", x)
print("Ставка в час: ", y)
print("Премия: ", z)
print("Зарплата сотрудника: ", (float(x) * float(y)) + float(z))

# задача 2

n = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new = [el for el in range (len(n)-1) if n[el] > n[el-1]]
print(new)

# задача 3

list = [i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0]
print(list)

# задача 4

n = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new = [el for el in n if n.count(el) == 1]
print(new)

# задача 5

from functools import reduce
list = [i for i in range(100, 1001, 2)]
print(reduce(lambda x, y: x * y, list))

# задача 6

from itertools import count,  cycle
for el in count(3):
        if el == 10:
            break
        print(el)


# задача 7







