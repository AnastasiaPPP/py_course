# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
# Ответьте на вопросы:
# * Какие вещи взяли все три друга
# * Какие вещи уникальны, есть только у одного друга
# * Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# * Для решения используйте операции с множествами.
# Код должен расширяться на любое большее количество друзей.

friends = {'Петр': ('Зажигалка', 'Палатка', 'Фонарик'),
           'Иван': ('Фонарик', 'Спальный мешок', 'Спички', 'Зажигалка', 'Котелок'),
           'Андрей': ('Консервы', 'Фонарик', 'Спальный мешок', 'Плед')}


def find_common_things():
    names = [name for name in friends.keys()]
    common_things = set(friends.get(names[0])).intersection(set(friends.get(names[1])))
    for i in range(len(names) - 1):
        common_things = set(friends.get(names[0])).intersection(friends.get(names[i+1]))
    return common_things

def find_unique_things():
    unique_things = set()
    duplicates = set()
    names = [name for name in friends.keys()]
    for i in range(len(names) - 1):
        duplicates.update(set(friends.get(names[i])).intersection(friends.get(names[i + 1])))
        unique_things.update(set(friends.get(names[i]) + friends.get(names[i + 1])))
    unique_things -= duplicates
    return unique_things


def search_absent_thing():
    list_of_things = []
    for value in friends.values():
        list_of_things.append(list(value))
    flat_list = [item for sublist in list_of_things for item in sublist]
    count_of_friends = len(friends) - 1
    new_list = []
    for thing in flat_list:
        if flat_list.count(thing) == count_of_friends:
            new_list.append(thing)
    return list(set(new_list))

def get_key(d, value):
    for k, v in d.items():
        if value not in v:
            return k

print('1. Все три друга взяли: ', find_common_things())
print('2. Уникальные вещи, которые есть только у одного друга: ', find_unique_things())
absents_things = search_absent_thing()
print('3. ', end='')
for item in absents_things:
    print(f'{item} нет только у {get_key(friends, item)}')