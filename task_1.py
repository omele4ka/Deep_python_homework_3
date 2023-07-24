# Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов. [1, 2, 3, 1, 2, 4, 5] -> [1, 2]

my_list = [1, 2, 3, 1, 2, 4, 5]
duplicate_list = list()

for item in my_list:
    if my_list.count(item) > 1 and item not in duplicate_list:
        duplicate_list.append(item)

print(duplicate_list)