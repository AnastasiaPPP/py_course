# Напишите функцию для транспонирования матрицы

matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]


def transport_matrix(matr: list) -> list[int]:
    new_matrix = []
    for i in range(len(matr[0])):
        inner_list = []
        for j in range(len(matr)):
            inner_list.append(matr[j][i])
        new_matrix.append(inner_list)
    return new_matrix


def print_matrix(matr):
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            print(matr[i][j], end=' ')
        print()


print_matrix(matrix)
print()
print_matrix(transport_matrix(matrix))
