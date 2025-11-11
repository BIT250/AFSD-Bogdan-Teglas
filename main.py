# metoda bubble sort

# o lista de numere intregi aleatoare
# cum o sortam prin bubble sort

# 1. definim functia bubble sort
#       - parametru: lista
# 2. parcurgem lista de la primul element pana la penultimul
# 3. comparam elementul curent cu urmatorul
#      - daca elem. curent > urmatorul
#          - le interschimbam
#       - altfel
#          - trecem la urmatorul element
# la fiecare iteratie, ultimul element este la locul lui
# ne oprim cand nu mai sunt schimbari
lista = [25, 12, 22, 11,34,64, 90]

def bubble_sort(lista):
	schimbari = True
	while schimbari:
		i = 0
		schimbari = False
		# i e pozitia curenta
		# lista[i] e elementul curent
		# i+1 pozitia urmatoare
		# lista[i+1] e elementul urmator
		while i < len(lista) - 1:
			if lista[i] > lista[i+1]:
				# interschimbam
				lista[i], lista[i+1] = lista[i+1], lista[i]
				schimbari = True
			i += 1

	print(lista)

bubble_sort(lista)