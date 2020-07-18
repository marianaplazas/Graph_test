#!/usr/bin/python3

def rutas(inicio, dest, matrix):

	rutas = []
	tmp = []

	for i in range(len(matrix)):
		if (inicio in matrix[i] and matrix[i].index(inicio) == 0):
			tmp.append(matrix[i])
	if (tmp[0][1] != dest):
		construir_ruta(inicio, dest, tmp, matrix)

def construir_ruta(inicio, dest, tmp, matrix):
	ruta = []

	if (inicio != dest):
		print(tmp)
		inicio = tmp[0][1]
		ruta.append(inicio)
		tmp= rutas(inicio, dest, matrix)
	return(ruta)

with open ('input.txt', 'r') as f:
	lists = f.read().splitlines()
ruta_f = lists.pop()
ruta_f = ruta_f.split(",")
matrix = []
for i in range(len(lists)):
	matrix.append(lists[i].split(","))

rutas(ruta_f[0], ruta_f[1], matrix)

