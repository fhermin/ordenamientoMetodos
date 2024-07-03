def quick_sort(array, low, high):
    if low < high:
        aux = partition(array, low, high)
        quick_sort(array, low, aux - 1)
        quick_sort(array, aux + 1, high)

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

scores = [56, 12, 87, 15, 68, 2, 78, 45]
print("Antes de ordenarse:")
print(scores)
quick_sort(scores, 0, len(scores) - 1)
print("Despues de ordenarse:")
print(scores)
