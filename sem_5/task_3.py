# Создайте функцию генератор чисел Фибоначчи (см. Википедию)

def fib_generator(n: int):
    num_1, num_2 = 0, 1
    for _ in range(n):
        yield num_1 + num_2
        num_1, num_2 = num_2, num_1 + num_2


