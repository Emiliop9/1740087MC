def OrdenPorInsercion(array):
	global cnt
	for indice in range (1, len(array)):
		valor=array[indice] #valor es el elemento que vamos a comparar
		i=indice-1          #i es el valor anterior al elemento que comparamos
		while i>=0:
			cnt+=1
			if valor<array[i]: #comparamos valor con el valor anterior
				array[i+1]=array[i] #intercambiamos los valores
				array[i]=valor
				i-=1
			else:
				break
	return array
