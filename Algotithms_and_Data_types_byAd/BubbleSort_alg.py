# Алгоритм сортировки пузырьком
# Сложность алгоритма O(n2) - квадратичная, количество необходимых операций растет квадратично n2
#Медленный алгоритм, подходит для данных небольшого размера.

def bubble_sort(array):
    for i in range(0, len(array) - 1):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


unsort_ar = [4, 2, 6, 1, 3]
print(bubble_sort(unsort_ar))
