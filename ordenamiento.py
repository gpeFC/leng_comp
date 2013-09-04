# -*- coding: utf8 -*-

"""========================================================================
	Emanuel G.P.
	Lenguajes y Compiladores.
	Facultad de Ciencias, UAEM.
						>>Clases y Objetos: Ordenamiento<<
========================================================================"""




mi_lista_1 = [3, 5, 2, 6, 8, 9, 1, 0, 4, 7]
mi_lista_2 = []

print "Lista a Ordenar: ", mi_lista_1
count = 0
for num in range(len(mi_lista_1)):
	num_min = mi_lista_1[count]
	for item in mi_lista_1:
		if item <= num_min:
			num_min = num
	mi_lista_2.append(num_min)
	count += 1
	print mi_lista_2
print "Lista Ordenada: ", mi_lista_2

print "-"*75

print "Lista a Ordenar: ", mi_lista_1
i = 0
j = 1
num_flag = True
while num_flag:
	if mi_lista_1[j] < mi_lista_1[i]:
		if i > 0:
			m = 0
			m += i
			for n in range(0, m):
				if mi_lista_1[j] < mi_lista_1[m]:
					mi_lista_1[m], mi_lista_1[j] = mi_lista_1[j], mi_lista_1[m]
				m -= 1
	i += 1
	j += 1
	if j == len(mi_lista_1):
		i = 0
		j = 1
	print mi_lista_1
	var = raw_input("entrada: ")
