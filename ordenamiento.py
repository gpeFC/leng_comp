# -*- coding: utf8 -*-

"""========================================================================
	Emanuel G.P.
	Lenguajes y Compiladores.
	Facultad de Ciencias, UAEM.
						>>Clases y Objetos: Ordenamiento<<
========================================================================"""


mi_lista_0 = [3, -5, 2, -6, 8, -9, 1, 0, -4, 7]
mi_lista_1 = [3, 5, 2, 6, 8, 9, 1, 0, 4, 7]

def selection_sort(num_lista):
	for num in range(len(num_lista)):
		for item in range(len(num_lista)):
			if num_lista[num] < num_lista[item]:
				num_lista[num], num_lista[item] = num_lista[item], num_lista[num]
		print num_lista
	return num_lista

def insertion_sort(num_lista):
	for i in range(len(num_lista)):
		index = -1
		for j in range(i, len(num_lista)):
			if num_lista[index] < num_lista[i]:
				num_temp = num_lista[index]
				num_lista.remove(num_lista[index])
				num_lista.insert(i, num_temp)
			index -= 1
		print num_lista

print "Lista a Ordenar: ", mi_lista_0
mi_lista_2 = selection_sort(mi_lista_0)
print "Lista Ordenada: ", mi_lista_2
print "-"*75
print "Lista a Ordenar: ", mi_lista_1
insertion_sort(mi_lista_1)
