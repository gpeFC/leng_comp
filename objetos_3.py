#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
27/08/2013
Emanuel G.P.
Lenguajes y Compiladores.
Facultad de Ciencias, UAEM.
>>Clases y Objetos: Archivos<<
"""


import csv


# Obtenemos objeto de archivo.
archivo = open("ejemplo.csv", "r")

renglones = csv.reader(archivo, delimiter=",", quotechar="|")
for renglon in renglones:
    print renglon 

# noten la diferencia.
print "\n\n\n"
otro = open("ejemplo.csv", "r")
for renglon in otro:
    print renglon, 
