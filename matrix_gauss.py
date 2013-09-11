# -*- coding: utf8 -*-

"""========================================================================
	Emanuel G.P.
	Lenguajes y Compiladores.
	Facultad de Ciencias, UAEM.
						>>Clases y Objetos: Gauss-Jordan<<
========================================================================"""

matriz_0 = [
			[1, 2, 3, 5],
			[4, 5, 6, 7],
			[7, 8, 8, 3],
			[3, 5, 8, 9]
			]



print matriz_0

for i in range(len(matriz_0)):
	for j in range(len(matriz_0[i])):
		matriz_0[i][j]  *= 1.0

print 
for item in matriz_0:
	print item 
print 


dim = len(matriz_0)
col = len(matriz_0[0])
for i in range(dim):
	pivote = matriz_0[i][i]
	print "Pivote => ", pivote
	for j in range(i+1, dim):
		mult = matriz_0[j][i]/pivote
		print ">>", matriz_0[j][i], mult
		for k in range(col):
			matriz_0[j][k] -= (mult*matriz_0[i][k])

print 
for item in matriz_0:
	print item 
print 

for i in reversed(range(dim)):
	pivote = matriz_0[i][i]
	print "Pivote =>", pivote
	print i
	for j in reversed(range(i)):
		mult = matriz_0[j][i]/pivote
		print ">>", i, j
		for k in reversed(range(col)):
			matriz_0[j][k] -= (mult*matriz_0[i][k])

print 
for item in matriz_0:
	print item 
print 

for i in range(dim):
	pivote = matriz_0[i][i]
	print "Pivote =>", pivote 
	for j in range(col):
		matriz_0[j][i] /= pivote 
		print matriz_0[j][i]

print 
for item in matriz_0:
	print item 
print