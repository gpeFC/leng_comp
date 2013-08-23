#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
22/08/2013
Emanuel G.P.
Lenguajes y Compiladores.
Facultad de Ciencias, UAEM.
>>Manejo de Excepciones<<
"""

while True:
    try:
        x = int(raw_input("Please, enter a number: "))
        break 
    except ValueError:
        print "Oops! That was no valid number. Try again..."
        
