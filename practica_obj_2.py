#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
27/08/2013
Emanuel G.P.
Lenguajes y Compiladores.
Facultad de Ciencias, UAEM.
>>Clases y Objetos: Practica2<<
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
            return False
    return True

def scl_matrix(matrix, num_esc):
    n_dim = matrix.__len__()
    for i in range(n_dim):
        for j in range(n_dim):
            matrix[i][j] = (matrix[i][j]) * int(num_esc)

matrix_1 = read_matrix(sys.argv[1])

for row in matrix_1:
    print(row)

print("\n")

if square_check(matrix_1):
    matrix_2 = scl_matrix(matrix_1, sys.argv[2])
    for row in matrix_1:
        print(row)
