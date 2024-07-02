def mergeSort( array ):
    if len(array) == 1:
        return array
    
    middle = len(array) // 2
    left_array = array[:middle]
    right_array = array[middle:]

    sorted_left = mergeSort(left_array)
    sorted_right = mergeSort(right_array)

    return Merge(sorted_left , sorted_right)


def Merge(left_array, right_array):
    arr_resultado = []
    while len(left_array) > 0 and len(right_array) > 0 :
        if left_array[0] > right_array[0]:
            arr_resultado.append(right_array[0])
            right_array.pop(0)
        else:
            arr_resultado.append(left_array[0])
            left_array.pop(0)
    
    while len(left_array) > 0 :
        arr_resultado.append(left_array[0])
        left_array.pop(0)

    while len(right_array) > 0:
        arr_resultado.append(right_array[0])
        right_array.pop(0)
    
    return arr_resultado


scores = [56,12,87,15,68,2,78,45]
print("Antes de ordenarse : ")
print(scores)
print("Despues de ordenarse : ")
print(mergeSort(scores))