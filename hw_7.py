# Создать телефонный справочник используя файлы,
# модули и исключения




try:
    file = open('phone_book.txt', "r", encoding="utf-8")
    try:
        lines = file.readlines()
        for line in lines:
            print(line.strip())
        print(f"{'':-^90}")
        d = int(input('Если необходимо добавить запись нажмите 1 :'))
        if d == 1:
            l = input('Добавте телефон, Ф.И.О., адрес: ')
            with open('phone_book.txt', "a", encoding="utf-8") as file:
                file.write(l)

    finally:
        file.close()
except FileNotFoundError:
    print('0000 NOOOOOO!!')




