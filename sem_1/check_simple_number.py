# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.


# while True:
#     number = int(input('Введите число: '))
#     if number < 1 or number > 100000:
#         print('Введите положительное число до 100 000')
#         continue
#     else:
#         if number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
#             print('Число составное')
#         else:
#             print('Число простое')
#         break
def prime():
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

print(prime())

