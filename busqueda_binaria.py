# -*- coding: utf8 -*-

"""========================================================================
	Emanuel G.P.
	Lenguajes y Compiladores.
	Facultad de Ciencias, UAEM.
						>>Clases y Objetos: Búsqueda Binaria<<
========================================================================"""

class BinarySearch:
	def __init__(self, num_lista):
		self.vector_num = num_lista
		self.dim_vector = len(self.vector_num)

	def ordena_vector(self, num_lista):
		for num in range(len(num_lista)):
			for item in range(len(num_lista)):
				if num_lista[num] < num_lista[item]:
					num_lista[num], num_lista[item] = num_lista[item], num_lista[num]

	def buscar_numero(self, numero, num_lista):
		index_temp = (self.dim_vector)/2
		num_temp = num_lista[index_temp]
		if numero == num_temp:
			return True
		else:
			izq_lista = num_lista[:index_temp]
			der_lista = num_lista[index_temp:]
			buscar_numero(numero, izq_lista)
			buscar_numero(numero, der_lista)
		return False
