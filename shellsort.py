def shellSort( array ):
    length = len( array )
    interval = length // 2

    while interval > 0:
        #Insert sort
        for i in range (interval , length):
            insert_value = array[i] #toma el siguiente valor a ser insertado
            insert_index = i # Indice donde se insertará el insert_value

            while insert_index >= interval and array[insert_index - interval] > insert_value:
                array[insert_index] = array[insert_index - interval]
                insert_index -= interval

            # Introducimos el valor al indice que corresponde
            array[insert_index] = insert_value

        interval //=2

    return array

scores = [56,12,87,15,68,2,78,45]
print("Antes de ordenarse : ")
print(scores)
print("Despues de ordenarse : ")
print(shellSort(scores))
