import portfolio as pf

stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
prices = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}
stocks_2 = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
prices_2 = {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50}


print('В результате работы функции calculate_portfolio_value получаем общую стоимость портфеля акций: ',
      pf.calculate_portfolio_value(stocks, prices))
print(f'В результате работры функции calculate_portfolio_return получаем процент дохода портфеля: '
      f'{pf.calculate_portfolio_return(10000, 15000)}%')
print('В результате работы функции get_most_profitable_stock получаем символ наиболее прибыльной акции: ',
      pf.get_most_profitable_stock(stocks_2, prices_2))

