



# Matrici recapitulare
# structura bidimensionala, cu linii si coloane formata din liste in liste

matrice = [
	[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9, 10, 11, 12],
	[13, 14, 15, 16],
	[17, 18, 19, 20]
]

# numarul de linii
numar_linii = len(matrice)
# numarul de coloane = numarul de elemente dintr-o linie (prima linie)
numar_coloane = len(matrice[0])

# parcurgerea matricii pe linii si coloane
for i in range(numar_linii):  # parcurgerea liniilor
	for j in range(numar_coloane):  # parcurgerea coloanelor
		element = matrice[i][j]
		print(element)

print("--------------------------")
# parcurgerea matricii pe coloane si linii
for j in range(numar_coloane-1, -1, -1):
	for i in range(numar_linii-1, -1, -1):
		element = matrice[i][j]
		print(element)
print("--------------------------")
# suma elementor matricei
s = 0
for i in range(numar_linii):
	for j in range(numar_coloane):
		s = s + matrice[i][j]

print(s)

# suma elementelor de pe liinile pare si coloanele impare

# Consideram prima linie sa fie linia 0

# varianta 1
suma = 0
for i in range(numar_linii):
	for j in range(numar_coloane):
		if i % 2 != 0 and j % 2 == 0:
			suma += matrice[i][j]
print(suma)

# varianta 2
suma = 0
for i in range(1, numar_linii, 2):
	for j in range(0, numar_coloane, 2):
		suma += matrice[i][j]
print(suma)

print("--------------------------")

# Să se determine cea mai mică valoare de pe fiecare linie,
# iar dintre acestea să se determine valoarea maximă.
# sa se returneze aceasta valoare

def max_min_matrice(matrice):
	# calculam minimul pe fiecare linie
	# salvam intr o lista toate minimele
	# returnam maximul din lista de minime
	lista_minime = []
	for i in range(numar_linii):
		minim_linie = matrice[i][0]
		for j in range(numar_coloane):
			if matrice[i][j] < minim_linie:
				minim_linie = matrice[i][j]
		lista_minime.append(minim_linie)
	return max(lista_minime)

print(max_min_matrice(matrice))

# Se dă o matrice și elemente numere naturale.
# Să se determine câte dintre elementele situate pe linii cu indici pari sunt prime.
print("--------------------------")
def este_prim(numar):
	if numar < 2:
		return False
	for i in range(2, numar):
		if numar % i == 0:
			return False
	return True

def nr_prime(matrice):
	nr_elemente = 0
	nr_linii = len(matrice) # 5
	nr_coloane = len(matrice[0])
	# 0 1 2 3 4
	# 1 2 3 4 5
	# 0   2   4
	for i in range(0, nr_linii, 2):
		for j in range(nr_coloane):
			if este_prim(matrice[i][j]):
				nr_elemente += 1

	return nr_elemente

print(nr_prime(matrice))

# Se dă o matrice cu n linii şi m coloane şi elemente numere naturale.
# Determinați suma valorilor pare distincte din matrice.

def suma_pare_3(matrice):
	nr_linii = len(matrice)
	nr_coloane = len(matrice[0])

	nr_pare = []
	for i in range(nr_linii):
		for j in range(nr_coloane):
			if matrice[i][j] % 2 == 0 and matrice[i][j] not in nr_pare:
				nr_pare.append(matrice[i][j])

	suma = 0
	for numar in nr_pare:
		suma += numar
	return suma

# Determinati coloanele care au toate elementele egale
# Indexul coloanelor se va afisa pe cate o linie
print("--------------------------")
def col_egale(matrice):
	nr_linii = len(matrice)
	nr_coloane = len(matrice[0])

	for j in range(nr_coloane):
		prim_element = matrice[0][j]
		coloana_ok = True
		for i in range(nr_linii):
			if matrice[i][j] != prim_element:
				coloana_ok = False
		if coloana_ok:
			for i in range(nr_linii):
				print(matrice[i][j])

col_egale([[1, 2, 3, 4],
		   [1, 5, 3, 8],
		   [1, 10, 3, 12],
		   [1, 14, 3, 16],
		   [1, 18, 3, 20]])


# afiseaza_triunghi_gol(5)
#    *
#   * *
#  *   *
# *     *
#* * * * *

# prima linie: 4 spatii, 1 stea - afisarea varfului
# ------------------------------------
# a doua linie: 3 spatii, o stea, 1 spatiu, o stea
# a treia linie: 2 spatii, o stea, 3 spatii, o stea
# a patra linie: 1 spatiu, o steaa, 5 spatii, o stea
# ------------------------------------
# ultima linie: 0 spatii, 5 stele separate printr-un spatiu

# repetat de n-2 ori
	# primele_spatii incep de la n-2, scad din 1 in 1
	# spatiile din mijloc incep de la 1, cresc din 2 in 2
print("--------------------------")
def afiseaza_triunghi_gol(n):
	# afisam varful
	# * = repetarea caracterului de x ori
	print(" " * (n-1) + "*")
	spatii_inainte = n-2
	spatii_mijloc = 1
	for i in range(n-2):
		print(" " * spatii_inainte + "*" + " " * spatii_mijloc + "*")
		spatii_inainte -= 1
		spatii_mijloc += 2

	print("* " * n)

afiseaza_triunghi_gol(5)

# minim_3([10, 15, 7, 3, 12, 1])
# lista[start:stop:pas]
def minim_3(lista):
	lista_sortata_3 = sorted(lista)[:3]
	lista_elemente = []
	for element in lista:
		if element in lista_sortata_3:
			lista_elemente.append(element)
	return lista_elemente

print(minim_3([10, 15, 7, 3, 12, 1]))


# timp_evaporare(100, 10, 50)
# x - numărul inițial de litri de apă (x greater than 0),
# t - intervalul de timp în minute după care un sfert din apă se evaporă (t greater than 0),
# y - numărul maxim de litri rămași.
def timp_evaporare(x, t, y):
	timp_scurs = 0
	while x > y:
		timp_scurs += t
		x -= x / 4
	return timp_scurs

print(timp_evaporare(100, 10, 50))