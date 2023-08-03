# Урок 4. Словари, множества и профилирование
# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
import random
arr_length_1 = int(input("Введите размер массива N: "))
arr_1 = [random.randint(1, 20) for _ in range(arr_length_1)]
print(arr_1)
arr_length_2 = int(input("Введите размер массива M: "))
arr_2 = [random.randint(1, 20) for _ in range(arr_length_2)]
print(arr_2)
result = []
for i in arr_1:
    if i in arr_2:
        result.append(i)
list_0 = set(result)
result = (list(list_0))
for f in sorted(result):
    print(f)