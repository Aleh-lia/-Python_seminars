# ДЗ 1
# 1) Создать список случайных чисел от -10, до 10 на num * 2 элементов.
#  num вводим с клавиатуры.
# 2) Вывести все числа меньше 0 и делящиеся на 3
# 3) Сказать кол-во элементов 5 и 3
# 4) Вывести разницу между кол-вом максимальных и минимальных значений
# 5) Сделать копию списка. Равзернуть и упорядочить список список
# 6) Удалить половину элементов списка
# 7) Очистить список

# ДЗ 2
# Сгенерировать список на num элементов от 150 до 200. num вводим с клавиатуры.
# Мы вводим с клавиатуры какое-то число в этом диапазоне ( от 150 до 200).
# Это построение по росту в строю. Необходимо поставить в строй введеный элемент
# Например: сгенерировались 163, 175, 169 , 200
# Вбили с клавиатуры 180
# Вы второй в строю. И вывести список.

import random

print(f"{'':-^90}")
print('Задание 1.1')
num1 = int(input('Введите число: '))
# num1 = 20
num = num1 * 2
spisok = []
for i in range(num):
    spisok.append(random.randint(-10, 10))
print(spisok)

print(f"{'':-^90}")
print('Задание 1.2')

for u in spisok:
    if u < 0:
        if u % 3 == 0:
            print(u, end=' ')
print()

print(f"{'':-^90}")
print('Задание 1.3')
count = 0
for u in spisok:
    if u == 5 or u == 3:
        count += 1
print(count)

print(f"{'':-^90}")
print('Задание 1.4')

mini = min(spisok)
maxi = max(spisok)
diff = maxi - mini
print(mini, maxi, diff)

print(f"{'':-^90}")
print('Задание 1.5')

c = spisok.copy()
print(c)
c.reverse()
print(c)
c.sort()
print(c)

print(f"{'':-^90}")
print('Задание 1.6')
del c[:(len(c) // 2)]
print(c)

print(f"{'':-^90}")
print('Задание 1.7')

c.clear()
print(c)

print(f"{'':/^90}")
print('Задание 2.0')

num_2_0 = int(input('Введите число от 150 до 200: '))
# num_2_0 = 171
spisok = []
count = 0
for t in range(23):
    spisok.append(random.randint(150, 201))
spisok.append(num_2_0)
spisok.sort()
for r in spisok:
    if r <= num_2_0:
        count += 1

print(f'Вы {count} в строю.')
print(spisok)
