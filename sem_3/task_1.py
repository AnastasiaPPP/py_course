# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов. [1, 2, 3, 1, 2, 4, 5] -> [1, 2]

my_list = [1, 2, 3, 1, 2, 4, 5]
new_list = []

for elem in my_list:
    if elem in new_list:
        continue
    if my_list.count(elem) > 1:
        new_list.append(elem)

print(new_list)