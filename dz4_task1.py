# Урок 4. Словари, множества и профилирование
# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло a[i] ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном списке урожайности грядки.
import random
round_bush_size = int(random.randint(8, 15))
bush = [random.randint(1, 20) for _ in range(round_bush_size)]
print(bush)
max = 0
bush_left = 0
bush_center = 0
bush_right = 0
for i in range(round_bush_size):
    three_bushes = bush[i-2] + bush[i-1] + bush[i]
    print(f"{bush[i-2]} + {bush[i-1]} + {bush[i]} = {three_bushes}")
    if three_bushes > max:
        max = three_bushes
        bush_left = i-2
        bush_center = i-1
        bush_right = i
print(f"Сумма для куста {bush_center} его левого соседа, куста {bush_left} и правого соседа, куста {bush_right} = {max}")