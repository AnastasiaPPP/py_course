# Напишите программу банкомат.
#
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

PERCENTAGE_FOR_WITHDRAWAL = 1.5
THIRD_OPERATION_PERCENT = 3
WEALTH_TAX = 10
DEPOSIT_LIMIT = 5_000_000
MULTIPLE_AMOUNT = 50
LOWER_WITHDRAWAL_AMOUNT = 30
UPPER_WITHDRAWAL_AMOUNT = 600
deposit = 0
operations_counter = 0
def print_menu():
    print('Выберите действие:\n1. Пополнить\n2. Снять\n3. Выйти')

def show_deposit():
    print(f'На счету: {deposit}')

def make_a_deposit():
    global operations_counter
    global deposit
    while True:
        user_deposit = int(input('Введите сумму: '))
        if user_deposit % MULTIPLE_AMOUNT == 0:
            if operations_counter == 3:
                deposit += deposit * THIRD_OPERATION_PERCENT / 100
                operations_counter = 0
            deposit += user_deposit
            operations_counter += 1
            if check_deposit_limit():
                deposit -= deposit * WEALTH_TAX / 100
            break
        else:
            print('Сумма должна быть кратной 50!')

def make_a_withdrawal():
    global operations_counter
    global deposit
    while True:
        amount = int(input('Сколько денег хотите снять? '))
        if amount > deposit:
            print('Столько денег у вас нет!')
            continue
        if amount % MULTIPLE_AMOUNT == 0 and LOWER_WITHDRAWAL_AMOUNT < amount < UPPER_WITHDRAWAL_AMOUNT:
            if operations_counter == 3:
                deposit += deposit * THIRD_OPERATION_PERCENT / 100
                operations_counter = 0
            deposit -= (amount * PERCENTAGE_FOR_WITHDRAWAL / 100) - amount
            operations_counter += 1
            if check_deposit_limit():
                deposit -= deposit * WEALTH_TAX / 100
            break
        else:
            print('Сумма должна быть от 30 до 600 у.е. и кратной 50')


def check_deposit_limit():
    global deposit
    if deposit > DEPOSIT_LIMIT:
        return True
    return False



while True:
    print_menu()
    user_input = int(input())
    if user_input == 1:
        show_deposit()
        make_a_deposit()
    elif user_input == 2:
        show_deposit()
        make_a_withdrawal()
    elif user_input == 3:
        print('Всего доброго!')
        exit()
    else:
        print('Неверный ввод')


