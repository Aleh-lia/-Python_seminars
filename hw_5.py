# 1) Дан список чисел. Создайте список, в который попадают числа,
#   описываемые возрастающую последовательность.
#   Порядок элементов менять нельзя.
#
# Пример:
#
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
#
# 2) Создайте программу для игры с конфетами человек против человека.
#
#   Условие задачи: На столе лежит 2021 конфета.
#   Играют два игрока делая ход друг после друга.
#   Первый ход определяется жеребьёвкой.
#   За один ход можно забрать не более чем 28 конфет.
#   Все конфеты оппонента достаются сделавшему последний ход.
#   Сколько конфет нужно взять первому игроку,
#   чтобы забрать все конфеты у своего конкурента?
#
#           НЕ ОБЯЗАТЕЛЬНАЯ. ДОП.
# 3*. Создайте программу для игры в "Крестики-нолики".

print(f"{'':-^90}")
print('Задание 1')

import random

# num = int(input('Введите число: '))
# num = 10
# spisok = []
# for i in range(num):
#     spisok.append(random.randint(1, 100))
# print(spisok)
#
# def list_up(spisok):
#     s = [spisok[0]]
#     for i in spisok:
#         if i > max(s):
#             s.append(i)
#     return s
#
# print(list_up(spisok))

print(f"{'':-^90}")
print('Задание 2')

greeting = ('Здравствуйте! Вас приветствует игра "Забери все конфеты!"\n '
            '\n'
            '               Основные правила игры:\n '
            'Вам будет дана 2021 конфета,'
            'за один ход вы можете взять не более 28 конфет.\n '
            '\n'
            '               Поехали!')


def introduce_players():
    player1 = "Player 1"
    player2 = "Player 2"
    return [player1, player2]


def get_draws(players):
    n = 2021    # количество конфет
    m = 28      # можно взять за один ход
    first = random.randint(1, 2)
    return [n, m, int(first)]


def play_game(draw, players):
    count = draw[2]
    while draw[0] > 0:
        if not count % 2:
            print("\033[5m\033[35m {}".format('Player 2 Ваш ход:'))
            move = int(input())
            if move > draw[0] or move > draw[1]:
                print("\033[31m {}".format(
                    f'Это слишком много, можно взять не более {draw[1]} конфет,'
                    f' у нас всего {draw[0]} конфет'))
                attempt = 3
                while attempt > 0:
                    if draw[0] >= move <= draw[1]:
                        break
                    print("\033[37m {}".format(f'Попробуйте ещё раз, у Вас {attempt} попытки'))
                    move = int(input())
                    attempt -= 1
                else:
                    return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
        else:
            print("\033[32m {}".format('Player 1 Ваш ход:'))
            move = int(input())
            if move > draw[0] or move > draw[1]:
                print("\033[31m {}".format(
                    f'Это слишком много, можно взять не более {draw[1]} конфет,'
                    f' у нас осталось {draw[0]} конфет'))
                attempt = 3
                while attempt > 0:
                    if draw[0] >= move <= draw[1]:
                        break
                    print("\033[37m {}".format(f'Давай ещё разок, у Вас {attempt} попытки'))
                    move = int(input())
                    attempt -= 1
                else:
                    return print("\033[31m {}".format(f'Попыток больше не осталось. Game over!'))
        draw[0] = draw[0] - move
        if draw[0] > 0:
            print("\033[34m {}".format(f'Осталось {draw[0]} конфет'))

        else:
            print("\033[34m {}".format('Конфет больше нет.'))
        count += 1
    return players[count % 2]

print(f"{'':-^90}")
print("\033[30m\033[46m {}".format(greeting))
print("\033[0m {}".format(''))

players = introduce_players()
draw = get_draws(players)

winer = play_game(draw, players)
if not winer:
    print("\033[31m\033[4m {}".format('У нас нет победителя.'))
else:
    print("\033[36m\033[1m {}".format(
        f'Поздравляю! В этот раз победил {winer}!'))
