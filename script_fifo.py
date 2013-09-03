# -*- coding: utf8 -*-

"""========================================================================
	Emanuel G.P.
	Lenguajes y Compiladores.
	Facultad de Ciencias, UAEM.
						>>Clases y Objetos: FIFO<<
	// ESTE SCRIPT ESTÁ IMPLEMENTADO EN PYTHON VERSION 3(Python v3). //
========================================================================"""

 	# Modulos importados.
import os

class MyQueue:
	"""Estructura FIFO implementada con una lista."""
	def __init__(self):
		"""Constructor que crea e inicializa el nuevo objeto 'Queue' vacío y también 
			inicializa una variable que contendra su longitud actual."""
		self.__my_queue = []
		self.__dim_queue = len(self.my_queue)

	def __queue_empty(self, dim_queue):
		"""Método que verifica si la estructura 'Queue' actual es vacía o no."""
		if dim_queue == 0:
			return True
		else:
			return False

	def push_queue(self, new_element):
		"""Método que permite insertar un nuevo elemento a la estructura 'Queue' actual."""
		self.__my_queue.append(new_element)
		self.__dim_queue = len(self.__my_queue)

	def pop_queue(self):
		"""Método que permite extraer un elemento de la estructura 'Queue' actual si es no vacía."""
		if __queue_empty(self.__dim_queue):
			print("La estructura 'Queue' actual está vacía...")
			return None
		else:
			pop_element = self.__my_queue[:1]
			self.__my_queue = self.__my_queue[1:]
			self.__dim_queue = len(self.__my_queue)
			return pop_element

	def view_elements(self):
		"""Método que pemite mostrar todos los elementos actuales contenidos 
			en la estructura 'Queue' actual si no es vacía."""
		if __queue_empty(self.__dim_queue):
			print("La estructura 'Queue' actual está vacía...")
		else:
			print()
			for item in range(__dim_queue):
				print ("|",)
				print (self.__my_queue[item],)
				print("|")
			print()

def main():
	"""Función principal del script."""
	tad_queue = MyQueue()
	flag_exit = True
	while flag_exit:
		os.system("clear")
		print("\t\t TAD FIFO con Listas...\n")
		print("\tA) Agregar elemento al TAD 'Queue'.")
		print("\tB) Extraer elemento del TAD 'Queue'.")
		print("\tC) Mostar elementos actuales en el TAD 'Queue'.")
		print("\tD) Salir del script.\n")
		opc_menu = raw_input("Indica la opción a realizar: ")
		opc_menu = opc_menu.lower()
		if opc_menu  == "A":
			try:
				os.system("clear")
				print("\t\tPUSH\n\n")
				nuevo_elemento = input("Ingresa el nuevo elemento a ingresar al tad queue: ")
				tad_queue.push_queue(nuevo_elemento)
				continuar = raw_input("El nuevo elemento fue ingresado con exito, presiona <Enter> \
										para continuar...")
			except:
				os.system("clear")
				print("\tFallo en la ejecución de la acción actual.")
				continuar = raw_input("Presiona <Enter> para continuar...")
		elif opc_menu == "B":
			try:
				os.system("clear")
				print("\t\tPOP\n\n")
				elemento = tad_queue.pop_queue()
				print("Se extrajo el elemento: ", elemento)
				continuar = raw_input("El elemento fue extraido con exito, presiona <Enter> \
									   para continuar...")
			except:
				os.system("clear")
				print("\tFallo en la ejecución de la acción actual.")
				continuar = raw_input("Presiona <Enter> para continuar..."
		elif opc_menu == "C":
			try:
				os.system("clear")
				print("\t\tVIEW\n\n")
				tad_queue.view_elements()
				continuar = raw_input("Presiona <Enter> para continuar..."
			except:
				os.system("clear")
				print("\tFallo en la ejecución de la acción actual.")
				continuar = raw_input("Presiona <Enter> para continuar..."
		elif opc_menu == "D":
			try:
				flag_exit = False:
				os.system("clear")
			except:
				os.system("clear")
				print("\tFallo en la ejecución de la acción actual.")
				continuar = raw_input("Presiona <Enter> para continuar..."
		else:
			try:
				os.system("clear")
				print("\tOpción invalida.")
				continuar = raw_input("Presiona <Enter> para continuar..."
			except:
				os.system("clear")
				print("\tFallo en la ejecución de la acción actual.")
				continuar = raw_input("Presiona <Enter> para continuar..."


if __name__ == '__main__':
	main()
	exit()