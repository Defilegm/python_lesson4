# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.
import random

lst = [random.randint(0,10) for i in range(7)]
print(lst)
result = []
for elem in lst:
    if lst.count(elem) == 1:
        result.append(elem)
print(result)

