# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида «10.25%».
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

names = ['Егор', 'Андрей', 'Иван']
rates = [7000, 5000, 6500]
percent = ['10.25%', '7.15%', '23.14%']


def generate_rewards_dict(names: list[str], rate: list[int], reward: list[str]) -> dict:
    return {key: value * float(percent_[:-1]) for (key, value, percent_) in zip(names, rate, reward)}


print(generate_rewards_dict(names, rates, percent))
