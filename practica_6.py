#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
22/08/2013
Emanuel G.P.
Lenguajes y Compiladores.
Facultad de Ciencias, UAEM.
>>Argumentos de Sistema<<
"""

import sys

def main():
    """Argumentos de Ejecución"""
    print len(sys.argv)
    if len(sys.argv) > 0:
        print sys.argv[1]

if __name__ == "__main__":
    main()
