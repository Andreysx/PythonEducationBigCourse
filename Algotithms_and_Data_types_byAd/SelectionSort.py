# Сортировка выбором
# Сортировка массива по возрастанию

def findSmallest(array: list):#функция для поиска наименьшего элемента массива
    smallest_value = array[0] #для хранения наименьшего значения
    smallest_index = 0        # для хранения индекса наименьшего значения
    for i in range(1, len(array)):
        if array[i] < smallest_value:
            smallest_value = array[i]
            smallest_index = i
    return smallest_index


def selectionSort(array: list): # функция для сортировки массива Сортировка выбором
    newArray = []
    for i in range(len(array)):
        smallest = findSmallest(array) #нахождение наименьшего элемента в массиве
        newArray.append(array.pop(smallest))  #добавление наименьшего элемента в новый массим с удаленим из старого
    return newArray


print(selectionSort([5, 3, 6, 2, 10]))
