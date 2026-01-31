# Функция слияния двух отсортированных списков
def merge_two_lists(first: list, second: list) -> list:
    i = 0
    j = 0
    new_array = []
    while i != len(first) and j != len(second):
        if first[i] <= second[j]:
            new_array.append(first[i])
            i += 1
        else:
            new_array.append(second[j])
            j += 1
    new_array.extend(first[i:])
    new_array.extend(second[j:])
    return new_array


first_array = [1, 4, 10, 11]
second_array = [2, 3, 3, 4, 8]

print(merge_two_lists(first_array, second_array))
