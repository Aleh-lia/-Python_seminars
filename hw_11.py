
# 1) Ввести с клавиатуры N и M
# Создать 2 таблицы данных в NumPy размера NxM -
# одну заполнить вручную, а вторую случайными числами.
# Найти сумму элементов всех массивов,
# Найти самый большой элемент массивов и самый маленький.
#
# 2) Создать таблицу данных в pandas - заполнить
# Добавить новый столбец.
#
# 3) Построить график y = 1\x
# Настроить внешний вид таблицы

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
print(f"{'':-^90}")
print('Задание 1')

n = int(input('Введите число N: '))
m = int(input('Введите число M: '))



array_r = np.random.random((n,m))
array_i = np.array(([[1, 5, 6],
 [5, 4, 1 ],
 [1, 1,  1],
 [5, 6, 9],
 [5, 4, 7]]))

print(array_r)
print(array_i)



array_sumr = np.sum(array_r)
array_sumi = np.sum(array_i)
array_maxr = np.max(array_r)
array_maxi = np.max(array_i)
array_minr = np.min(array_r)
array_mini = np.min(array_i)

print(array_sumr)
print(array_sumi)
print(array_minr)
print(array_mini)
print(array_maxr)
print(array_maxi)

# print(f"{'':-^90}")
# print('Задание 2')
#
# data = {'car': ['Ferrari', 'Porsche', 'McLaren', 'Koenigsegg', 'Bugatti', 'SSC'],
#         'model': ['LaFerrari', '918', 'P1', 'Agera', 'Veyron', 'Tuatara'],
#         'speed': [350, 343, 350, 443, 431, 532]}
# frame = pd.DataFrame(data)
# frame.index.name = 'id'
# frame.columns.name = 'item'
# print(frame)
# frame['Acceleration time'] = [2.7, 2.8, 2.8, 2.9, 2.5, 2.5]
# print(frame)
#
#
# print(f"{'':-^90}")
# print('Задание 3')
#
# x = np.linspace(-100, 100)
# y = 1/x
# plt.plot(x, y, color='gold', linestyle='solid', linewidth=3)
# plt.title('График y = 1/x')
# plt.xlabel('ось X')
# plt.ylabel('ось Y')
# plt.grid()
# plt.show()