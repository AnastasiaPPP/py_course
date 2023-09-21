
def check_triangle(a, b, c):
    if a == b == c:
        print('Треугольник равносторонний')
    elif (a + b) <= c or (a + c) <= b or (b + c) <= a:
        print('Такой треугольник не существует')
    elif a == b or a == c or b == c:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')

def test_triangle():
    assert check_triangle(2, 3, 6) == 'Такой треугольник не существует', False



