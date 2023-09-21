
def prime():
    """
    >>> prime(34)
    'Составное число'
    >>> prime(3)
    'Простое число'
    """
    while True:
        number = int(input('Введите число: '))
        if number < 1 or number > 100000:
            print('Введите положительное число до 100 000!')
            continue
        counter = 0
        for i in range(1, number):
            if number % i == 0:
                counter += 1
        return 'Простое число' if counter < 2 else 'Составное число'

if '__name__' == '__main__':
    import doctest

    doctest.testmod(verbose=True)

