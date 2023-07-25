# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
# Пример: rev_kwargs(res=1, reverse=[1, 2, 3]) -> {1: 'res', '[1, 2, 3]': 'reverse'}

def return_values_dict(**kwargs) -> dict:
    values_dict = {}
    for key, value in kwargs.items():
        try:
            hash(value)
            values_dict[value] = key
        except TypeError:
            values_dict[str(value)] = key
    return values_dict


print(return_values_dict(res=1, reverse=[1, 2, 3]))
