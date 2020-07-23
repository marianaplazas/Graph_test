#!/usr/bin/python3

def rutas(inicio, dest, matrix, ruta, guardar_l, weight):

	tmp = []

	for i in range(len(matrix)):
		if (inicio in matrix[i] and matrix[i].index(inicio) == 0):
			tmp.append(matrix[i])

	for i in range(len(tmp)):
		inicio = tmp[i][1]
		ruta.append(inicio)
		weight += int(tmp[i][2])
		result = rutas(inicio, dest, matrix, ruta, guardar_l, weight)
		if (result[-1] == dest):
			guardar_l.append(result[:])
			guardar_l[-1].append(weight)
		weight -= int(tmp[i][2])
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
mini = 100000
for i in range(len(lista_rutas)):
	if (lista_rutas[i][-1] < mini):
		mini = lista_rutas[i][-1]
		
for i in range(len(lista_rutas)):
	if mini in lista_rutas[i]:
		lista_rutas[i].pop()
		print(lista_rutas[i])
		