# 1.1. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
#
# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
#  1-2*3 => -5;


# 1.2 Добавьте возможность использования скобок, меняющих приоритет операций.
#
#     *Пример:*
#     1+2*3 => 7;
#     (1+2)*3 => 9;


# 2.1 Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
#
# Пример:
#
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
#
# - С помощью использования лямбд, filter, map, zip, enumerate, list comprehension


print(f"{'':-^90}")
print('Задание 1.1')


p = lambda a, b: a + b
print(p(2, 2))

o = lambda x, y, u: x + y * u
print(o(1, 2, 3))

s = lambda f, g, h: f - g * h
print(s(1, 2, 3))

print(f"{'':-^90}")
print('Задание 1.2')

o = lambda x, y, u: x + y * u
s = lambda x, y, u: (x + y) * u
print(o(1, 2, 3))
print(s(1, 2, 3))


print(f"{'':-^90}")
print('Задание 2')


myList = [1, 2, 3, 5, 1, 5, 3, 10]

replay = []
for i in myList:
    count = 0
    for x in myList:
        if x == i:
            count += 1
    replay.append(count)


unique = set()
index = 0
while index < len(myList):
    if replay[index] == 1:
        unique.add(myList[index])
    index += 1
print(list(unique))



