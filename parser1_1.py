# -*- coding: utf8 -*-

"""========================================================================
    Emanuel G.P.
    Lenguajes y Compiladores.
    Facultad de Ciencias, UAEM.
                        >>Parser: 1_1<<
========================================================================"""


def separa_tokens(lista):
    nueva_lista = []
    for idx_1 in range(len(lista)):
        temp_lista = []
        temp_token = ""
        cadena = lista[idx_1]
        for idx_2 in range(len(cadena)):
            if cadena[idx_2] == "(" or cadena[idx_2] == ")":
                temp_lista.append(cadena[idx_2])
            elif cadena[idx_2] == "0" or cadena[idx_2] == "1" or cadena[idx_2] == "2" or cadena[idx_2] == "3" or cadena[idx_2] == "4" or cadena[idx_2] == "5" or cadena[idx_2] == "6" or cadena[idx_2] == "7" or cadena[idx_2] == "8" or cadena[idx_2] == "9":
                temp_token += cadena[idx_2]
                if idx_2 < (len(cadena)-1) and cadena[idx_2+1] != "0" and cadena[idx_2+1] != "1" and cadena[idx_2+1] != "2" and cadena[idx_2+1] != "3" and cadena[idx_2+1] != "4" and cadena[idx_2+1] != "5" and cadena[idx_2+1] != "6" and cadena[idx_2+1] != "7" and cadena[idx_2+1] != "8" and cadena[idx_2+1] != "9":
                    temp_lista.append(temp_token)
                    temp_token = ""
            elif cadena[idx_2] == "+" or cadena[idx_2] == "-" or cadena[idx_2] == "*" or cadena[idx_2] == "/" or cadena[idx_2] == "^":
                temp_lista.append(cadena[idx_2])
        temp_lista.append(temp_token)
        nueva_lista += temp_lista
    lista_tokens = []
    for token in nueva_lista:
        if len(token) != 0:
            lista_tokens.append(token)
    return lista_tokens


def castea_tokens(lista):
    lista_tokens = []
    for elemento in lista:
        if elemento.isdigit():
            lista_tokens.append(int(elemento))
        else:
            lista_tokens.append(elemento)
    return lista_tokens




if __name__ == "__main__":
    mi_sentencia = raw_input("Ingresa la expresión: ") 
    print "La expresión es: ", mi_sentencia
    if mi_sentencia.find(" ") != -1:
        tokens_lista = mi_sentencia.split(" ")
        print "Lista de Tokens_1: ", tokens_lista
        tokens_lista = separa_tokens(tokens_lista)
        print "Lista de Tokens_2: ", tokens_lista
        tokens_lista = castea_tokens(tokens_lista)
        print "Lista de Tokens_3: ", tokens_lista

