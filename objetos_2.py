#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
27/08/2013
Emanuel G.P.
Lenguajes y Compiladores.
Facultad de Ciencias, UAEM.
>>Clases y Objetos<<
"""

class ClasePadre:
    def suma_num(self, num1, num2):
        return num1 + num2
    def otra(self, num1, num2):
        return num1 * num2

class ClaseHijo(ClasePadre):
    def suma_num(self):
        return num1 - num2
    def muestra_op(self, num1, num2):
        print "La resta es: ", num1 - num2


padre = ClasePadre()
hijo = ClaseHijo()

print padre.suma_num(5, 3)
print padre.otra(5, 3)

print "-"*10

#print hijo.suma_num(5, 3)
hijo.muestra_op(5, 3)
