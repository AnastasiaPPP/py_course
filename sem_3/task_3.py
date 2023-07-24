# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

staff = {'Компас': 10, 'Палатка': 50, 'Спальный мешок': 40, 'Котелок': 20, 'Спички': 5,
         'Крем от москитов': 5,'Паёк': 30, 'Инструменты': 50, 'Плед': 15, 'Powerbank': 5}

SIZE = 150
def check_empty_space(sum_size, next_size):
    return sum_size + next_size <= SIZE

def count_rest(sum_size):
    return SIZE - sum_size
def collect_things():
    temp_2 = {(value, key) for key, value in staff.items()}
    temp = sorted(temp_2, reverse=True)

    for i in range(len(temp)):
        sum_size = 0
        res_staff = {}
        for j in range(i, len(temp)):
            if check_empty_space(sum_size, temp[j][0]):
                res_staff.setdefault(temp[j][1], temp[j][0])
                sum_size += temp[j][0]
        if i == 0:
            print('"Жадный" вариант: ')
        elif i == 1:
            print('Другие варианты: ')
        print(res_staff)
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

print(collect_things())


