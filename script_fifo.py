# -*- coding: utf8 -*-

"""========================================================================
	Emanuel G.P.
	Lenguajes y Compiladores.
	Facultad de Ciencias, UAEM.
						>>Clases y Objetos: FIFO<<
========================================================================"""

 	# Modulos importados.
import os

class MyQueue:
	"""Estructura FIFO implementada con una lista."""
	def __init__(self):
		"""Constructor que crea e inicializa el nuevo objeto 'Queue' vacío y también 
			inicializa una variable que contendra su longitud actual."""
		self.__my_queue = [] # Inicialización de la lista vacía que fungira como la estructura Queue.
		self.__dim_queue = len(self.__my_queue) # Inicialización de la variable que contendrá la longitud de la estructura Queue.

	def __queue_empty(self, dim_queue):
		"""Método que verifica si la estructura 'Queue' actual es vacía o no."""
		if dim_queue == 0:
			return True
		else:
			return False

	def push_queue(self, new_element):
		"""Método que permite insertar un nuevo elemento a la estructura 'Queue' actual."""
		self.__my_queue.append(new_element) # Actualización de la estructura, anexando el elemento nuevo a la Queue.
		self.__dim_queue = len(self.__my_queue) # Actualización de la longitud de la Queue.

	def pop_queue(self):
		"""Método que permite extraer un elemento de la estructura 'Queue' actual si es no vacía."""
		if self.__queue_empty(self.__dim_queue): # Condición que verifica que la Queue sea no vacía.
			print "La estructura 'Queue' actual está vacía..."
			return None # Retorno de un valor nulo cuando la Queue es vacía.
		else:
			pop_element = self.__my_queue[0] # Captura del elemento a extraer de la Queue.
			self.__my_queue = self.__my_queue[1:] # Actualización de la estructura, quitando el elemento extraido.
			self.__dim_queue = len(self.__my_queue) # Actualización de la longitud de la Queue.
			return pop_element # Retorno del elemento extraido de la Queue.

	def view_elements(self):
		"""Método que pemite mostrar todos los elementos actuales contenidos 
			en la estructura 'Queue' actual si no es vacía."""
		if self.__queue_empty(self.__dim_queue): # Condición que verifica que la Queue sea no vacía.
			print "La estructura 'Queue' actual está vacía..."
		else:
			print 
			for item in self.__my_queue: # Ciclo que imprime en pantalla los elementos contenidos actualmente en la Queue.
				print item, "|",
			print 

def main():
	"""Función principal del script."""
	tad_queue = MyQueue() # Instanciación del nuevo objeto Queue.
	flag_exit = True # Inicialización de una bandera para controlar el bucle principal del script.
	while flag_exit: # Bucle que permite controlar ciclicamente la ejecución del script. 
		os.system("clear") # Método para limpiar la pantalla actual.
		print "\t\t TAD FIFO con Listas...\n"
		print "\tA) Agregar elemento a la estructura 'Queue'."
		print "\tB) Extraer elemento de la estructura 'Queue'."
		print "\tC) Mostar elementos actuales en la estructura 'Queue'."
		print "\tD) Salir del script.\n"
		opc_menu = raw_input("Indica la opción a realizar: ") # Captura de la acción a realizar.
		opc_menu = opc_menu.upper() # Método para convertir a mayúsculas la entrada de la variable.
		if opc_menu  == "A": # Hacer un Push en la Queue.
			try: # Control de excepciones del script.
				os.system("clear")
				print "\t\tPUSH\n\n"
				nuevo_elemento = input("Introduce el nuevo elemento a ingresar al tad queue[para ingresar texto, excribirlo entre comillas('')]: ")
				tad_queue.push_queue(nuevo_elemento) # Invocación del método push del objeto Queue.
				continuar = raw_input("El nuevo elemento fue ingresado con exito, presiona <Enter> para continuar...")
			except: # Captura de la excepción. 
				os.system("clear")
				print "\tFallo en la ejecución de la acción actual."
				continuar = raw_input("Presiona <Enter> para continuar...") # Variable para controlar la espera del prompt. 
		elif opc_menu == "B": # Hacer un Pop en la Queue.
			try:
				os.system("clear")
				print"\t\tPOP\n\n"
				elemento = tad_queue.pop_queue() # Invocación del método pop del objeto Queue.
				if elemento != None: # Condición que verifica que el elemento recuperado no sea nulo.
					print "Se extrajo el elemento: ", elemento
					continuar = raw_input("El elemento fue extraido con exito, presiona <Enter> para continuar...")
				else:
					continuar = raw_input("Presiona <Enter> para continuar...")
			except:
				os.system("clear")
				print "\tFallo en la ejecución de la acción actual."
				continuar = raw_input("Presiona <Enter> para continuar...")
		elif opc_menu == "C": # Hacer un View de la Queue.
			try:
				os.system("clear")
				print "\t\tVIEW\n\n"
				tad_queue.view_elements() # Invocación del método view del objeto Queue.
				continuar = raw_input("Presiona <Enter> para continuar...")
			except:
				os.system("clear")
				print "\tFallo en la ejecución de la acción actual."
				continuar = raw_input("Presiona <Enter> para continuar...")
		elif opc_menu == "D": # Salir de la ejecución del script.
			try:
				flag_exit = False # Cambio del valor booleano de la bandera que controla el bucle principal.
				os.system("clear")
			except:
				os.system("clear")
				print "\tFallo en la ejecución de la acción actual."
				continuar = raw_input("Presiona <Enter> para continuar...")
		else: # Condicional alternativo para entradas incorrectas. 
			try:
				os.system("clear")
				print "\tOpción invalida."
				continuar = raw_input("Presiona <Enter> para continuar...")
			except:
				os.system("clear")
				print "\tFallo en la ejecución de la acción actual."
				continuar = raw_input("Presiona <Enter> para continuar...")


if __name__ == '__main__': # Inicialización de la función principal main.
	main() # Llamada de la funcion main.
	exit() # Finalización del script.