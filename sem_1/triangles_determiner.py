a = 2
b = 2
c = 2
# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
def check_triangle(a, b, c):
    if a == b == c:
        print('Треугольник равносторонний')
    elif (a + b) <= c or (a + c) <= b or (b + c) <= a:
        print('Такой треугольник не существует')
    elif a == b or a == c or b == c:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')

check_triangle(a, b, c)