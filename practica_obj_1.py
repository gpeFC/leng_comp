#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
27/08/2013
Emanuel G.P.
Lenguajes y Compiladores.
Facultad de Ciencias, UAEM.
>>Clases y Objetos: Practica1<<
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

def transp_matrix(matrix):
    """n_rows = matrix.__len__() # Determine row number.
    n_cols = 0
    # Determine maximum column size.
    for i in range(n_rows):
        if matrix[i].__len__() > n_cols:
            n_cols = matrix[i].__len__()
    # set the rows for transposed matrix.
    new_matrix = [None] * n_cols
    """
    matrix_t = []
    n_rows = matrix.__len__()
    n_cols = matrix[0].__len__()
    for i in range(n_rows):
        row_t = []
        for j in range(n_cols):
            try:
                row_t.append(matrix[j][i])
            except:
                row_t.append(0)
        matrix_t.append(row_t)
    
    return matrix_t
    
mtz_1 = read_matrix(sys.argv[1])

for row in mtz_1:
    print(row)

mtz_2 = transp_matrix(mtz_1)

for row in mtz_2:
    print(row)
    
print("\n")
