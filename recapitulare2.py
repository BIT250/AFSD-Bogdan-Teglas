# afiseaza_paralelogram(3, '*')
# *
# **
# ***
# ***
#  **
#   *

# 3 afisari ale caracterului '*', pe linii crescator
# 3 afisari ale caracterului '*', pe linii descrescator, indentate corespunzator

def afiseaza_paraleglogram(n, caracter):
	# repetam de n ori = for i in range(n)
	# prima parte - liniile crescatoare
	# pe linia 1 : 1 caracter *
	# pe linia 2 : 2 caractere *
	# ...
	# pe linia i : i caractere *

	# for i in range(n):    i = 0 1 ... n-1
	# range(n) = 0, 1, 2, ..., n-1
	# range(start, stop) = start, start+1, ..., stop-1
	for i in range(1, n+1):
		# *x la siruri de caractere = repetarea caracterului de x ori
		print(caracter * i)

	# a doua parte - liniile descrescatoare
	# pe linia 1: 0 spatii, 3 caractere *
	# pe linia 2: 1 spatiu, 2 caractere *
	# pe linia 3: 2 spatii, 1 caracter *

	for i in range(n):
		numar_spatii = i
		numar_caractere = n - i
		print(" " * numar_spatii + caracter * numar_caractere)

# afiseaza_paraleglogram(5, "*")

#     *
#    * *
#   *   *
#  *     *
# * * * * *


# primul rand: 4 spatii inainte si un caracter
# -----------------------------------------------  n = 5
# al 2-lea rand: 3 spatii inainte, un caracter, 1 spatiu, un caracter
# al 3-lea rand: 2 spatii inainte, un caracter, 3 spatii, un caracter
# al 4-lea rand: 1 spatiu inainte, un caracter, 5 spatii, un caracter
# ------------------------------------------------
# ultimul rand: 0 spatii, 5 caractere separate de spatiu
def afiseaza_triunghi_gol(n):
	# afisam varful (primul rand)
	# n-1 spatii inainte si un caracter
	print(" " * (n - 1) + "*")

	numar_spatii_inainte = n - 2
	numar_spatii_mijloc = 1
	for i in range(2, n):
		print(" " * numar_spatii_inainte + "*" + " " * numar_spatii_mijloc + "*")
		numar_spatii_inainte -= 1
		numar_spatii_mijloc += 2

	# afisam baza (ultimul rand)
	print("* " * n)

# afiseaza_triunghi_gol(5)

# Scrie o funcție Python care primește o propoziție și înlocuiește
# cuvintele de lungime maximă cu oglinditul lor.
# Restul cuvintelor și ordinea propoziției rămân neschimbate.
# Considerăm cuvânt orice secvență delimitată de spații ce conține cel puțin o literă.

def cuvant_valid(cuvant):
	for caracter in cuvant:
		if caracter.isalpha():
			return True
	return False

def inlocuieste_cuvinte_maxime(propozitie):
	cuvinte = propozitie.split()
	print(cuvinte)

	lungime_maxima = 0
	for cuvant in cuvinte:
		if len(cuvant) > lungime_maxima and cuvant_valid(cuvant):
			lungime_maxima = len(cuvant)

	print(lungime_maxima)

	for cuvant in cuvinte:
		if len(cuvant) ==  lungime_maxima and cuvant_valid(cuvant):
			# Oglinditul unui cuvant
			# cuvant[::-1]
			print(cuvant[::-1], end=" ")
		else:
			print(cuvant, end=" ")


#inlocuieste_cuvinte_maxime("Mara  23a4 1234 %&a* %&*( are mere")

# Probleme matrici
# matricea - linii si coloane = lista de liste

matrice = [
	[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9, 10, 11, 12],
	[13, 14, 15, 16],
	[17, 18, 19, 20]
]

# suma elementelor matricei

# parcurgerea matricii pe linii si coloane
# numarul de linii
numar_linii = len(matrice)
# numarul de coloane = numarul de elemente dintr-o linie (prima linie)
numar_coloane = len(matrice[0])

suma = 0
for i in range(numar_linii):
	for j in range(numar_coloane):
		element = matrice[i][j]
		suma += element
print("Suma elementelor matricei este:", suma)

matrice = [
	[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9, 10, 11, 12],
	[13, 14, 15, 16],
	[17, 18, 19, 20]
]
# suma elementelor pe fiecare linie

for i in range(numar_linii):
	# i reprezinta linia curenta
	suma_linie = 0
	for j in range(numar_coloane):
		element = matrice[i][j]
		suma_linie += element
	print("Suma elementelor de pe linia", i, "este:", suma_linie)

