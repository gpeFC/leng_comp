#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
27/08/2013
Emanuel G.P.
Lenguajes y Compiladores.
Facultad de Ciencias, UAEM.
>>Clases y Objetos: Matrices<<
"""

import sys
import csv

def read_matrix(name):
    # file objetc.
    f = open(name, "r")
    matrix = []
    rows = csv.reader(f, delimiter=",", quotechar="|")
    for row in rows:
        new_row = []
        for col in row:
            # add col to row.
            new_row.append(int(col))
        # add row to matrix.
        matrix.append(new_row)
    return matrix

def square_check(matrix):
    # check rows.
    n_rows = matrix.__len__()
    for row in matrix:
        n_cols = row.__len__()
        if n_cols != n_rows:
            sys.exit("Not square matrix.")
    return 0

mi_matriz = read_matrix(raw_input("nombre del archivo: "))
for row in mi_matriz:
    print (row)
