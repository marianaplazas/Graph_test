#!/usr/bin/python3
import pdb

def cmpr(matrix, start, dest):
	weight = []
	for a in range(len(matrix)):
		if (matrix[a].index(start) == 0 and matrix[a].index(dest) == 1):
			weight.append(matrix[i][2])
	final = sum(weight)
	return(finals)

def f_weight(s_r, matrix):
	for i in range(len(s_r)):
		start = s_r[i]
		if (i + 1 < len(s_r)):
			dest = s_r[i + 1]
		weight = cmpr(matrix, start, dest)
		print(weight)

def order_r(all_r, matrix):
	weights = []
	copy_all = all_r
	for i in range(len(all_r)):
		s_r = copy_all.pop(i)
		f_weight(s_r, matrix)

def rutas(inicio, dest, matrix, ruta, guardar_l, weight):

	tmp = []

	for i in range(len(matrix)):
		if (inicio in matrix[i] and matrix[i].index(inicio) == 0):
			tmp.append(matrix[i])

	for i in range(len(tmp)):
		inicio = tmp[i][1]
		ruta.append(inicio)
		result = rutas(inicio, dest, matrix, ruta, guardar_l, weight)
		if (result[-1] == dest):
			guardar_l.append(result[:])
		ruta.pop()
	if (len(ruta) == 1):
		return guardar_l
	return (ruta)
	
	
with open ('input.txt', 'r') as f:
	lists = f.read().splitlines()
ruta_f = lists.pop()
ruta_f = ruta_f.split(",")
matrix = []
for i in range(len(lists)):
	matrix.append(lists[i].split(","))
weight = 0

lista_rutas = rutas(ruta_f[0], ruta_f[1], matrix, [ruta_f[0]], [], weight)
order_r(lista_rutas, matrix)