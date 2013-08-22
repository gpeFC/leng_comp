#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
22/08/2013
Emanuel G.P.
Lenguajes y Compiladores.
Facultad de Ciencias, UAEM.
>>Default Argument Values<<
"""

def some_function(onevalue, other_one, with_default="ok", next="still with value", the_last="I nedd a default too"):
    print onevalue
    print other_one
    print with_dafault

if __name__ == "__main__":
    some_function("hi", "there")
    print 
    some_function("hi", "again", "kid")
    print 
    some_function("hi") # tricky one.
