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

def unit_check(matrix):
    if square_check(matrix):
        # Ok to continue.
        n_rows = matrix.__len__()
        for i in range(n_rows):
            for j in range(n_rows):
                if i == j:
                    if matrix[i][j] != 1:
                        return False
                else:
                    if matrix[i][j] != 0:
                        return False
    return True

def zero_check(matrix):
    if square_check(matrix):
    # Ok to continue.
    n_rows = matrix.__len__()
    for i in range(n_rows):
        for j in range(n_rows):
            if matrix[i][j] != 0:
                return False
    return True


if __name__ == "__main___":
    archivo = sys.argv[1]
    mat = read_matrix(archivo)
    print("this matrix is: ")
    if 
    
