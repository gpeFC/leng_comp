# -*- coding: utf8 -*-

"""========================================================================
    Octubre / 2013
    Emanuel G.P.
    Lenguajes y Compiladores.
    Facultad de Ciencias, UAEM.
                        >>Parser-Calculadora<<
========================================================================"""



    # Modulos importados.
import re



class Parser:
    """ Clase para el Parser de la Calculadora. """
    
    def __init__(self, cadena):
        """ Método Constructor de la Clase. """
        self.__cadena_ingresada = cadena # Cadena a evaluar (parsear) ingresada por el usuario.
        self.__lista_tokens = [] # Lista que almacenará los tokens contenidos en la cadena evaluada.
        self.__dicc_tokens = {'NUMERO':[], 'VARIABLE':[], 'DELIMITADOR':[], 'OPERADOR':[], 'OTRO':[]} # Diccionario que guardará los tokens clasificados.
        
    
    def separa_tokens(self):
        """ Método que identifica y separa todos los tokens que componen la cadenada evaluada. """
        lista = self.__cadena_ingresada.split(" ") # Primera lista que segmenta la cadena evaluada por espacios en blanco.
        nueva_lista = [] # Lista temporal para almacenar los tokens que se encuentran en la cadena evaluada.
        for idx_1 in range(len(lista)): # Bucle para buscar los tokens en la cadena evaluada.
            temp_lista = [] # Lista temporal, local al bucle, para ir guardando las palabras extraidas de la cadena evaluada.
            temp_token = "" # Cadena temporal para ir capturando los simbolos (letras, numeros, puntos, comas) integran cada token.
            cadena = lista[idx_1] # Cadena temporal para guardar cada palabra encontrada en la primera lista generada por la cadena evaluada.
            for idx_2 in range(len(cadena)): # Bucle para identificar y separar los tokens contenidos en la cadena evaluada. 
                if cadena[idx_2] == "(" or cadena[idx_2] == ")": # Condicion que identifica los tokens 'delimitadores'.
                    temp_lista.append(cadena[idx_2]) # Anexo del token 'delimitador' a la lista temporal (local al bucle).
                elif cadena[idx_2] == "," or cadena[idx_2] == "." or cadena[idx_2] == "0" or cadena[idx_2] == "1" or cadena[idx_2] == "2" or cadena[idx_2] == "3" or cadena[idx_2] == "4" or cadena[idx_2] == "5" or cadena[idx_2] == "6" or cadena[idx_2] == "7" or cadena[idx_2] == "8" or cadena[idx_2] == "9": # Condicion que identifica los tokens 'numeros'.
                    temp_token += cadena[idx_2] # Concatenacion de simbolos para obtener el token 'numero'.
                    if idx_2 < (len(cadena)-1) and cadena[idx_2+1] != "," and cadena[idx_2+1] != "." and cadena[idx_2+1] != "0" and cadena[idx_2+1] != "1" and cadena[idx_2+1] != "2" and cadena[idx_2+1] != "3" and cadena[idx_2+1] != "4" and cadena[idx_2+1] != "5" and cadena[idx_2+1] != "6" and cadena[idx_2+1] != "7" and cadena[idx_2+1] != "8" and cadena[idx_2+1] != "9" and cadena[idx_2+1] != "a" and cadena[idx_2+1] != "A" and cadena[idx_2+1] != "b" and cadena[idx_2+1] != "B" and cadena[idx_2+1] != "c" and cadena[idx_2+1] != "C" and cadena[idx_2+1] != "d" and cadena[idx_2+1] != "D" and cadena[idx_2+1] != "e" and cadena[idx_2+1] != "E" and cadena[idx_2+1] != "f" and cadena[idx_2+1] != "F" and cadena[idx_2+1] != "g" and cadena[idx_2+1] != "G" and cadena[idx_2+1] != "h" and cadena[idx_2+1] != "H" and cadena[idx_2+1] != "i" and cadena[idx_2+1] != "I" and cadena[idx_2+1] != "j" and cadena[idx_2+1] != "J" and cadena[idx_2+1] != "k" and cadena[idx_2+1] != "K" and cadena[idx_2+1] != "l" and cadena[idx_2+1] != "L" and cadena[idx_2+1] != "m" and cadena[idx_2+1] != "M" and cadena[idx_2+1] != "n" and cadena[idx_2+1] != "N" and cadena[idx_2+1] != "o" and cadena[idx_2+1] != "O" and cadena[idx_2+1] != "p" and cadena[idx_2+1] != "P" and cadena[idx_2+1] != "q" and cadena[idx_2+1] != "Q" and cadena[idx_2+1] != "r" and cadena[idx_2+1] != "R" and cadena[idx_2+1] != "s" and cadena[idx_2+1] != "S" and cadena[idx_2+1] != "t" and cadena[idx_2+1] != "T" and cadena[idx_2+1] != "u" and cadena[idx_2+1] != "U" and cadena[idx_2+1] != "v" and cadena[idx_2+1] != "V" and cadena[idx_2+1] != "w" and cadena[idx_2+1] != "W" and cadena[idx_2+1] != "y" and cadena[idx_2+1] != "Y" and cadena[idx_2+1] != "z" and cadena[idx_2+1] != "Z": # Condicion para verificar el siguiente simbolo en la palabra evaluada actualmente.
                        temp_lista.append(temp_token) # Anexo del token 'numero' a la lista temporal (local al bucle).
                        temp_token = "" # Limpieza de la cadena temporal que captura los simbolos (letras, numeros, puntos, comas) que integran cada token.
                elif cadena[idx_2] == "a" or cadena[idx_2] == "A" or cadena[idx_2] == "b" or cadena[idx_2] == "B" or cadena[idx_2] == "c" or cadena[idx_2] == "C" or cadena[idx_2] == "d" or cadena[idx_2] == "D" or cadena[idx_2] == "e" or cadena[idx_2] == "E" or cadena[idx_2] == "f" or cadena[idx_2] == "F" or cadena[idx_2] == "g" or cadena[idx_2] == "G" or cadena[idx_2] == "h" or cadena[idx_2] == "H" or cadena[idx_2] == "i" or cadena[idx_2] == "I" or cadena[idx_2] == "j" or cadena[idx_2] == "J" or cadena[idx_2] == "k" or cadena[idx_2] == "K" or cadena[idx_2] == "l" or cadena[idx_2] == "L" or cadena[idx_2] == "m" or cadena[idx_2] == "M" or cadena[idx_2] == "n" or cadena[idx_2] == "N" or cadena[idx_2] == "o" or cadena[idx_2] == "O" or cadena[idx_2] == "p" or cadena[idx_2] == "P" or cadena[idx_2] == "q" or cadena[idx_2] == "Q" or cadena[idx_2] == "r" or cadena[idx_2] == "R" or cadena[idx_2] == "s" or cadena[idx_2] == "S" or cadena[idx_2] == "t" or cadena[idx_2] == "T" or cadena[idx_2] == "u" or cadena[idx_2] == "U" or cadena[idx_2] == "v" or cadena[idx_2] == "V" or cadena[idx_2] == "w" or cadena[idx_2] == "W" or cadena[idx_2] == "y" or cadena[idx_2] == "Y" or cadena[idx_2] == "z" or cadena[idx_2] == "Z": # Condicion que identifica los tokens 'variables'.
                    temp_token += cadena[idx_2] # Concatenacion de simbolos para obtener el token 'variable'.
                    if idx_2 < (len(cadena)-1) and (cadena[idx_2+1] == "=" or cadena[idx_2+1] == "+" or cadena[idx_2+1] == "-" or cadena[idx_2+1] == "*" or cadena[idx_2+1] == "/" or cadena[idx_2+1] == "^"): # Condicion para verificar el siguiente simbolo en la palabra evaluada actualmente.
                        temp_lista.append(temp_token) # Anexo del token 'variable' a la lista temporal (local al bucle).
                        temp_token = "" # Limpieza de la cadena temporal que captura los simbolos (letras, numeros, puntos, comas) que integran cada token.
                elif cadena[idx_2] == "=" or cadena[idx_2] == "+" or cadena[idx_2] == "-" or cadena[idx_2] == "*" or cadena[idx_2] == "/" or cadena[idx_2] == "%" or cadena[idx_2] == "^": # Condicion que identifica los tokens 'operadores'.
                    temp_lista.append(cadena[idx_2]) # Anexo del token 'operador' a la lista temporal (local al bucle).
            temp_lista.append(temp_token) # Anexo de token arbitrario a la lista temporal (local al bucle).
            nueva_lista += temp_lista # Anexo de los tokens contenidos en la lista temporal (local al bucle) a la lista temporal de tokens.
        for token in nueva_lista: # Bucle para obtener la lista final de tokens de la cadena evaluada, excluyendo los tokens nulos.
            if len(token) != 0: # Condicion para identificar los tokens no nulos.
                self.__lista_tokens.append(token) # Anexo de los tokens a la lista final de tokens
    
    def clasifica_tokens(self):
        """ Método que clasifica los tokens contenidos en la cadena evaluada segun su categoría. """
        for token in self.__lista_tokens:
            if token.isdigit():
                pass 

    
    def imprime_datos(self):
        """ Método que muestra en la pantalla los datos actuales del Parser. """
        print "Cadena Evaluada: ", self.__cadena_ingresada
        print "Lista de Tokens: ", self.__lista_tokens
        print "Diccionario de Tokens: ", self.__dicc_tokens



if __name__ == "__main__":
    print "Parser para una Calculadora...\n"
    
    mi_cadena = raw_input("Ingresa la cadena a evaluar: ")
    
    print 
    
    parser = Parser(mi_cadena)
    parser.separa_tokens()
    parser.imprime_datos()
    
    print 


