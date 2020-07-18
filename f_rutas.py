#!/usr/bin/python3
import pdb

def rutas(inicio, dest, matrix, ruta, guardar_l):

	tmp = []

	for i in range(len(matrix)):
		if (inicio in matrix[i] and matrix[i].index(inicio) == 0):
			tmp.append(matrix[i])

	for i in range(len(tmp)):
		inicio = tmp[i][1]
		ruta.append(inicio)
		result = rutas(inicio, dest, matrix, ruta, guardar_l)
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

print(rutas(ruta_f[0], ruta_f[1], matrix, [ruta_f[0]], []))

