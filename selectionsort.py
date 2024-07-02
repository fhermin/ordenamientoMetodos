def SelectSort( array ) :
    length = len(array) - 1

    for i in range(0 , length):
        min_index = i #mantiene en que posición quedo el min_value
        min_value = array[min_index]   #es donde esta el que tiene el menor valor

        for j in range (i , length):
            if min_value > array[j + 1 ]:
                min_value = array[j + 1]
                min_index = j + 1
            
        if min_index != i:
            aux = array[i]
            array[i] = array[min_index]
            array[min_index] = aux
    return array


scores = [56,12,87,15,68,2,78,45]
print("Antes de ordenarse : ")
print(scores)
print("Despues de ordenarse : ")
print(SelectSort(scores))
