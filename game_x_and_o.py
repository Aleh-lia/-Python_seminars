def check_winner():
    if area[0][0] == "X" and area[0][1] == "X" and area[0][2] == "X":
        return "X"
    if area[1][0] == "X" and area[1][1] == "X" and area[1][2] == "X":
        return "X"
    if area[2][0] == "X" and area[2][1] == "X" and area[2][2] == "X":
        return "X"
    if area[0][0] == "X" and area[1][0] == "X" and area[2][0] == "X":
        return "X"
    if area[0][1] == "X" and area[1][1] == "X" and area[2][1] == "X":
        return "X"
    if area[0][2] == "X" and area[1][2] == "X" and area[2][2] == "X":
        return "X"
    if area[0][0] == "X" and area[1][1] == "X" and area[2][2] == "X":
        return "X"
    if area[0][2] == "X" and area[1][1] == "X" and area[2][0] == "X":
        return "X"
    if area[0][0] == "0" and area[0][1] == "0" and area[0][2] == "0":
        return "0"
    if area[1][0] == "0" and area[1][1] == "0" and area[1][2] == "0":
        return "0"
    if area[2][0] == "0" and area[2][1] == "0" and area[2][2] == "0":
        return "0"
    if area[0][0] == "0" and area[1][0] == "0" and area[2][0] == "0":
        return "0"
    if area[0][1] == "0" and area[1][1] == "0" and area[2][1] == "0":
        return "0"
    if area[0][2] == "0" and area[1][2] == "0" and area[2][2] == "0":
        return "0"
    if area[0][0] == "0" and area[1][1] == "0" and area[2][2] == "0":
        return "0"
    if area[0][2] == "0" and area[1][1] == "0" and area[2][0] == "0":
        return "0"
    return "*"

area = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]

for turn in range(1, 10):
    print(f"Ход: {turn}")
    if turn % 2 == 0:
        turn_char = "0"
        print("\033[35m {}".format("Ходят нолики"))
    else:
        turn_char = "X"
        print("\033[34m {}".format("Ходят крестики"))
    row = input("Введите номер строки(0,1 или 2): ")
    row = int(row)
    column = input("Введите номер столбса(0,1 или 2): ")
    column = int(column)

    if area[row][column] == "*":
        area[row][column] = turn_char
    else:
        print("\033[31m {}".format("Ячейка уже занята, вы пропускаете ход"))
        if turn == 9:
            print("Ничья")
        continue

    for cell in area:
        print(cell)

    if check_winner() == "X":
        print("")
        print("Победа крестиковвв")
        break
    if check_winner() == "0":
        print("")
        print("Победа ноликов")
        break
    if turn == 9 and check_winner() == "*":
        print("")
        print("Ничья")