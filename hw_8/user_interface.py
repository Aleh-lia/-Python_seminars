def choice():
    while True:
        user_input = input('''
        1 - ID,        2 - ФИО 
        3 - ДР,        4 - должность
        5 - пол,       6 - все данные
              0 - выход\n
Выберите что необходимо вывести на экран : ''')
        try:
            user_input = int(user_input)
        except:
            print('Введите номер цифрой!')
            continue
        if user_input >= 0 and user_input <= 6:
            return user_input
        else:
            print('Выбрать нужно от 0 до 6!')


if __name__ == '__main__':
    choice()