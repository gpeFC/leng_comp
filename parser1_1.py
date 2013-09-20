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
            elif cadena[idx_2] == "." or cadena[idx_2] == "0" or cadena[idx_2] == "1" or cadena[idx_2] == "2" or cadena[idx_2] == "3" or cadena[idx_2] == "4" or cadena[idx_2] == "5" or cadena[idx_2] == "6" or cadena[idx_2] == "7" or cadena[idx_2] == "8" or cadena[idx_2] == "9":
                temp_token += cadena[idx_2]
                if idx_2 < (len(cadena)-1) and cadena[idx_2+1] != "." and cadena[idx_2+1] != "0" and cadena[idx_2+1] != "1" and cadena[idx_2+1] != "2" and cadena[idx_2+1] != "3" and cadena[idx_2+1] != "4" and cadena[idx_2+1] != "5" and cadena[idx_2+1] != "6" and cadena[idx_2+1] != "7" and cadena[idx_2+1] != "8" and cadena[idx_2+1] != "9":
                    temp_lista.append(temp_token)
                    temp_token = ""
            elif cadena[idx_2] == "a" or cadena[idx_2] == "A" or cadena[idx_2] == "b" or cadena[idx_2] == "B" or cadena[idx_2] == "c" or cadena[idx_2] == "C" or cadena[idx_2] == "d" or cadena[idx_2] == "D" or cadena[idx_2] == "e" or cadena[idx_2] == "E" or cadena[idx_2] == "f" or cadena[idx_2] == "F" or cadena[idx_2] == "g" or cadena[idx_2] == "G" or cadena[idx_2] == "h" or cadena[idx_2] == "H" or cadena[idx_2] == "i" or cadena[idx_2] == "I" or cadena[idx_2] == "j" or cadena[idx_2] == "J" or cadena[idx_2] == "k" or cadena[idx_2] == "K" or cadena[idx_2] == "l" or cadena[idx_2] == "L" or cadena[idx_2] == "m" or cadena[idx_2] == "M" or cadena[idx_2] == "n" or cadena[idx_2] == "N" or cadena[idx_2] == "o" or cadena[idx_2] == "O" or cadena[idx_2] == "p" or cadena[idx_2] == "P" or cadena[idx_2] == "q" or cadena[idx_2] == "Q" or cadena[idx_2] == "r" or cadena[idx_2] == "R" or cadena[idx_2] == "s" or cadena[idx_2] == "S" or cadena[idx_2] == "t" or cadena[idx_2] == "T" or cadena[idx_2] == "u" or cadena[idx_2] == "U" or cadena[idx_2] == "v" or cadena[idx_2] == "V" or cadena[idx_2] == "w" or cadena[idx_2] == "W" or cadena[idx_2] == "y" or cadena[idx_2] == "Y" or cadena[idx_2] == "z" or cadena[idx_2] == "Z":
                temp_token += cadena[idx_2]
                if idx_2 < (len(cadena)-1) and cadena[idx_2+1] != "a" and cadena[idx_2+1] != "A" and cadena[idx_2+1] != "b" and cadena[idx_2+1] != "B" and cadena[idx_2+1] != "c" and cadena[idx_2+1] != "C" and cadena[idx_2+1] != "d" and cadena[idx_2+1] != "D" and cadena[idx_2+1] != "e" and cadena[idx_2+1] != "E" and cadena[idx_2+1] != "f" and cadena[idx_2+1] != "F" and cadena[idx_2+1] != "g" and cadena[idx_2+1] != "G" and cadena[idx_2+1] != "h" and cadena[idx_2+1] != "H" and cadena[idx_2+1] != "i" and cadena[idx_2+1] != "I" and cadena[idx_2+1] != "j" and cadena[idx_2+1] != "J" and cadena[idx_2+1] != "k" and cadena[idx_2+1] != "K" and cadena[idx_2+1] != "l" and cadena[idx_2+1] != "L" and cadena[idx_2+1] != "m" and cadena[idx_2+1] != "M" and cadena[idx_2+1] != "n" and cadena[idx_2+1] != "N" and cadena[idx_2+1] != "o" and cadena[idx_2+1] != "O" and cadena[idx_2+1] != "p" and cadena[idx_2+1] != "P" and cadena[idx_2+1] != "q" and cadena[idx_2+1] != "Q" and cadena[idx_2+1] != "r" and cadena[idx_2+1] != "R" and cadena[idx_2+1] != "s" and cadena[idx_2+1] != "S" and cadena[idx_2+1] != "t" and cadena[idx_2+1] != "T" and cadena[idx_2+1] != "u" and cadena[idx_2+1] != "U" and cadena[idx_2+1] != "v" and cadena[idx_2+1] != "V" and cadena[idx_2+1] != "w" and cadena[idx_2+1] != "W" and cadena[idx_2+1] != "y" and cadena[idx_2+1]!= "Y" and cadena[idx_2+1] != "z" and cadena[idx_2+1] != "Z":
                    temp_lista.append(temp_token)
                    temp_token = ""
            elif cadena[idx_2] == "=" or cadena[idx_2] == "+" or cadena[idx_2] == "-" or cadena[idx_2] == "*" or cadena[idx_2] == "/" or cadena[idx_2] == "^":
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
        if elemento.isdigit(): lista_tokens.append(int(elemento))
        elif elemento.find(".") != -1: lista_tokens.append(float(elemento))
        else: lista_tokens.append(elemento)
    return lista_tokens


def coteja_del(lista):
    cont_del_i = 0
    cont_del_d = 0
    for item in lista:
        if item == "(":
            cont_del_i += 1
        elif item == ")":
            cont_del_d += 1
    if cont_del_i == cont_del_d:
        return True
    else:
        if cont_del_i > cont_del_d:
            return "Falta: )"
        else:
            return "Falta: ("

def clasifica_tokens(lista):
    del_lista = []
    num_lista = []
    var_lista = []
    ope_lista = []
    otros = []
    for item in lista:
        if item == "(" or item == ")":
            del_lista.append(item)
        elif item == "=" or item == "+" or item == "-" or item == "*" or item == "/" or item == "^":
            ope_lista.append(item)
        elif type(item) == int or type(item) == float:
            num_lista.append(item)
        elif item.isalpha() or item.isalnum():
            var_lista.append(item)
        else:
            otros.append(item)
    clasf_tokens = [("DEL", del_lista), ("OPE", ope_lista), ("NUM", num_lista), ("VAR", var_lista), ("OTR", otros)]
    return clasf_tokens

def coteja_asig(lista):
    if lista[1] == "=":
        if lista[0][0] != "0" and lista[0][0] != "1" and lista[0][0] != "2" and lista[0][0] != "3" and lista[0][0] != "4" and lista[0][0] != "5" and lista[0][0] != "6" and lista[0][0] != "7" and lista[0][0] != "8" and lista[0][0] != "9":
            return True
        else:
            return False

def validez_sintactica(lista):
    if len(lista) == 1:
        if type(lista[0]) == int or type(lista[0]) == float: print "Expresión Valida"
        else: print "Expresión Invalida"
    elif len(lista) == 2:
        if lista[0] == "(" and lista[1] == ")": print "Expresión Valida"
        


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
    else:
        tokens_lista = []
        tokens_lista.append(mi_sentencia)
        print "Lista de Tokens_1: ", tokens_lista
        tokens_lista = separa_tokens(tokens_lista)
        print "Lista de Tokens_2: ", tokens_lista
        tokens_lista = castea_tokens(tokens_lista)
        print "Lista de Tokens_3: ", tokens_lista
        bal_del = coteja_del(tokens_lista)
        if bal_del == True:
            print "Delimitadores Balanceados..."
        else:
            print bal_del
    print 
    clasf = clasifica_tokens(tokens_lista)
    for item in clasf:
        print item 
    if len(tokens_lista) > 1:
        if coteja_asig(tokens_lista):
            print "Asignación Valida..."
        else:
            print "Asignación Invalida..."

    validez_sintactica(tokens_lista)

