


# Matrici


matrice = [
	[1, 2, 3, 4],	# 0
	[1, 2, 3, 4],
	[9, 10, 11, 12],  # 2
	[13, 14, 15, 16],
	[17, 18, 19, 20]  # 4
]
# structura bidimensionala, cu linii si coloane formata din liste in liste
# accesam un element specificam linia si coloana
# print(matrice[3][2])

# numarul de linii
numar_linii = len(matrice)
# numarul de coloane = numarul de elemente dintr-o linie (prima)
numar_coloane = len(matrice[0])

# parcurgerea elementelor unei matrici pe linie si coloana
for i in range(numar_linii):
	# i reprezinta indexul liniei curente
	for j in range(numar_coloane):
		# j reprezinta indexul coloanei curente
		element = matrice[i][j]
		print(element)
print("--------------------------")
# parcurgerea elementelor unei matrici pe coloana si linie
for j in range(numar_coloane):
	for i in range(numar_linii):
		element = matrice[i][j]
		print(element)
print("--------------------------")
# parcurgerea elementelor in ordine inversa
for i in range(numar_linii-1, -1, -1):
	for j in range(numar_coloane-1, -1, -1):
		element = matrice[i][j]
		print(element)

# suma elementelor matricei
suma = 0
for i in range(numar_linii):
	for j in range(numar_coloane):
		suma += matrice[i][j]
print("Suma elementelor matricei este:", suma)

# suma elementelor pe fiecare linie
# sa afisez indexul liniei si suma elementelor
for i in range(numar_linii):
	# pe linia i
	suma_linie = 0
	for j in range(numar_coloane):	# j merge pe fiecare coloana a liniei i
		suma_linie += matrice[i][j]
	print(f"Linia {i}: {suma_linie}")

# cel mai mare numar par de pe fiecare coloana, daca nu exista numar par sa fie -1
# afisez indexul coloanei si cel mai mare numar par

# Aflarea unui maxim
# 1. initializez un maxim ori cu primul element, ori cu o valoare mica (-1)
# 2. parcurgem elementele
# 3. daca gasim un element mai mare decat maximul, actualizam maximul

for j in range(numar_coloane):
	# pe coloana j
	maxim_par = -1
	for i in range(numar_linii):
		if matrice[i][j] % 2 == 0 and matrice[i][j] > maxim_par:
			maxim_par = matrice[i][j]
	print(f"Coloana {j}: {maxim_par}")

# Se dă o matrice cu elemente numere naturale.
# Să se determine câte perechi de linii consecutive din matrice sunt identice.

# ex:
# 1 2 3 4
# 1 2 3 4  -> identice
# 5 6 7 8
# 1 2 3 5
# 1 2 3 5  -> identice
# raspuns: 2

# elementul: matrice[i][j]
# elementul de sub el: matrice[i+1][j]

# parcurg liniile pana la penultima
# presupun ca linia de sub ea e identica
# parcurg elementele liniei si daca un element de sub nu e egal, presupunerea e falsa
# daca presupunerea ramane adevarata, cresc contorul de linii identice


def identice1(matrice):
	nr_linii_identice = 0
	for i in range(numar_linii-1):
		linie_identica = True
		for j in range(numar_coloane):
			if matrice[i][j] != matrice[i+1][j]:
				linie_identica = False
		if linie_identica:
			nr_linii_identice += 1
	return nr_linii_identice

print(identice1(matrice))

# Programul interschimbă valoarea minimă din ultima coloană a tabloului cu
# valoarea minimă din prima coloană a tabloului

# 7   5   19
# 3   8   4
# 23  6   1
# 10  2   9

# minimul pe prima coloana si pozitia
def matrice_10(matrice):
	minim = matrice[0][0]
	j = 0
	i_min_1 = 0
	j_min_1 = 0
	for i in range(numar_linii):
		if matrice[i][j] < minim:
			minim = matrice[i][j]
			i_min_1 = i
			j_min_1 = j
	minim1 = minim

	nr_coloane = len(matrice[0])
	j = nr_coloane - 1
	minim = matrice[0][j]
	i_min_2 = 0
	j_min_2 = j
	for i in range(numar_linii):
		if matrice[i][j] < minim:
			minim = matrice[i][j]
			i_min_2 = i
			j_min_2 = j
	minim2 = minim

	# interschimbare
	matrice[i_min_1][j_min_1], matrice[i_min_2][j_min_2] = matrice[i_min_2][j_min_2], matrice[i_min_1][j_min_1]

	# afisare matrice
	# parcurgem elementele pe linie si coloana, intre elementele de pe linie punem spatiu,
	# intre linii punem rand nou
	for i in range(numar_linii):
		for j in range(numar_coloane):
			print(matrice[i][j], end=" ")
		print()

matrice_10(matrice)

def este_prim(n):
	# parcurgem de la 2 pana la n-1
	# daca gasim un divizor, nu e prim
	if n < 2:
		return False
	if n==2:
		return True
	for i in range(2, n):
		if n % i == 0:
			return False
	return True


def nr_prime(matrice):
	nr_elemente = 0
	for i in range(numar_linii):
		for j in range(numar_coloane):
			# linia i, coloana j, elmentul e matrice[i][j]
			if i % 2 == 0 and este_prim(matrice[i][j]):
				nr_elemente += 1
	return nr_elemente

print(nr_prime(matrice))