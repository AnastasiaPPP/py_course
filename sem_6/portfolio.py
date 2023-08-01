_initial_cost = {}


def calculate_portfolio_value(stocks: dict, prices: dict) -> float:
    sum_ = 0
    global _initial_cost
    _initial_cost = prices.copy()
    for value_1, value_2 in zip(stocks.values(), prices.values()):
        sum_ += value_1 * value_2
    return sum_


def calculate_portfolio_return(initial_value: float, current_value: float) -> float:
    return (current_value - initial_value) / initial_value * 100


def get_most_profitable_stock(stocks: dict, prices: dict) -> str:
    profit = {}
    for key, value_1, value_2 in zip(stocks.keys(), _initial_cost.values(),prices.values()):
        profit[key] = calculate_portfolio_return(float(value_1), float(value_2))
    return ''.join([i for i in profit if profit[i] == max(profit.values())])

