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
		self.valor_bool = False

	def ordena_vector(self, num_lista):
		for num in range(len(num_lista)):
			for item in range(len(num_lista)):
				if num_lista[num] < num_lista[item]:
					num_lista[num], num_lista[item] = num_lista[item], num_lista[num]

	def buscar_numero(self, numero, num_lista):
		index_temp = (len(num_lista))/2
		if index_temp > 0:
			num_temp = num_lista[index_temp]
			if numero == num_temp:
				self.valor_bool = True
			else:
				if numero > num_temp:
					self.buscar_numero(numero, num_lista[index_temp:])
				else:
					self.buscar_numero(numero, num_lista[:index_temp])
		elif index_temp == 0:
			num_temp = num_lista[index_temp]
			if numero == num_temp:
				self.valor_bool = True
	def resultado_busqueda(self, numero, num_lista):
		self.buscar_numero(numero, num_lista)
		if self.valor_bool:
			return True
		else:
			return False

if __name__ == "__main__":
	#mi_lista_0 = [3, -5, 2, -6, 8, -9, 1, 0, -4, 7]
	mi_lista_0 = [3, 5, 2, 6, 8, 9, 1, 0, 4, 7]
	print "Lista Original: ", mi_lista_0
	nueva_busqueda = BinarySearch(mi_lista_0)
	nueva_busqueda.ordena_vector(mi_lista_0)
	print "Lista Ordenada: ", mi_lista_0
	num_busq = int(raw_input("Numero a buscar: "))
	valor = nueva_busqueda.resultado_busqueda(num_busq, mi_lista_0)
	if valor:
		print "Número encontrado."
	else:
		print "Número no encontrado."