#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
22/08/2013
Emanuel G.P.
Lenguajes y Compiladores.
Facultad de Ciencias, UAEM.
>>Common I/O operations<<
"""

def countdown(n):
    if n <= 0:
        print "Despegamos"
        return 
    print n
    countdown(n-1)
    
if __name__ == "__main__":
    countdown(3)
