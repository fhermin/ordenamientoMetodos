def insertSort( array) :
    length = len(array)

    for i in range (1 , length):
        insert_value = array[i] #toma el siguiente valor a ser insertado
        insert_index = i # Indice donde se insertará el insert_value

        while insert_index > 0 and array[insert_index -1] > insert_value:
            array[insert_index] = array[insert_index -1]
            insert_index -= 1
            # Introducimos el valor al indice que corresponde
            array[insert_index] = insert_value

    return array




scores = [56,12,87,15,68,2,78,45]
print("Antes de ordenarse : ")
print(scores)
print("Despues de ordenarse : ")
print(insertSort(scores))
