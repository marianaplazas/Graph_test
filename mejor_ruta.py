#!/usr/bin/python3

def rutas(inicio, dest, matrix):

	rutas = []
	ruta = []
	tmp = []

	for i in range(len(matrix)):
		if (inicio in matrix[i] and matrix[i].index(inicio) == 0):
			tmp.append(matrix[i])

	if (inicio != dest):
		inicio = tmp[0][1]
		ruta.append(inicio)
		print(tmp, type(tmp))
		print('this is ruta',ruta)
		tmp = rutas(inicio, dest, matrix)
		return(ruta)

with open ('input.txt', 'r') as f:
	lists = f.read().splitlines()
ruta_f = lists.pop()
ruta_f = ruta_f.split(",")
matrix = []
for i in range(len(lists)):
	matrix.append(lists[i].split(","))

rutas(ruta_f[0], ruta_f[1], matrix)