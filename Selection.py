#Este si funciona pero al poner cualquier arreglo para trabajarlo truena.


def selection(arr):
    for i in range(0,len(arr-1)):
        val=i
        for j in range(i+1, len(arr)):
            if arr[j]<arr[val]:
                contador=contador+1
                val=j
        if valor!=i:
            aux=arr[i]
            arr[i]=arr[val]
            arr[val]=aux
    return arr
    return contador
