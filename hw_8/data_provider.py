list = [['1', 'Саша Сергей Евген', '15.10.1989', 'инж', 'муж'],
        ['2', 'Чиж Юлия Конст', '12.05.1986', 'бух', 'жен'],
        ['3', 'Жук Екатерина Стан', '22.06.2000', 'лаб', 'жен'],
        ['4', 'Сом Владимер Алекс', '02.07.1988', 'нач', 'муж'],
        ['5', 'Вол Валерий Степ', '05.05.1980', 'раб', 'муж']]
def read_file(file):
    f = open(file, 'r', encoding="utf-8")
    data = f.read().splitlines()
    list = []
    for line in data:
        line = line.split(';')
        list.append(line)
    f.close()
    return list



def write_file(list, mod):
    f = open('result.csv', mod, encoding="utf-8")
    for i in range(len(list)):
        for j in range(len(list[i])):
            f.writelines(list[i][j])
            f.writelines(';')
        f.writelines('\n')
    f.close()
    if mod == 'a':
        print('Данные записаны!')
    if mod == 'w':
        print('Данные перезаписаны!')

mod = 'w'
write_file(list, mod)