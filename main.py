lista = [1, 5, 3, 7, 2, 9, 4]

def bubble_sort(lista):
	interschimbare = True
	while interschimbare:
		interschimbare = False
		i = 0
		while i < len(lista) - 1:
			# i e pozitia curenta
			# i + 1 e pozitia urmatoare
			# valoarea curenta: lista[i]
			# valoarea urmatoare: lista[i + 1]
			if lista[i] > lista[i + 1]:
				interschimbare = True
				lista[i], lista[i + 1] = lista[i + 1], lista[i]
			i += 1
	print(lista)
	return lista

bubble_sort(lista)