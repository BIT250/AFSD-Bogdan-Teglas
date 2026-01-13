# Operatorii
# Aritmetici: +, -, *, /, %, //, **
# atribuire =, +=, -=, *=, /=, %=, //=, **=
# Comparare: ==, !=, >, <, >=, <=
# Logici: and, or, not

# Variabile
x = 10
# and = 5
# nume_variabila = valoare
# reguli de denumire:
# incepe cu litera sau _
# nu poate fi cuvant rezervat: if, else, while, for, def, return, import, from, as, class, try, except, finally, with, lambda, pass, break, continue, global, nonlocal, assert, yield, raise, del, is, in
# fara spatii

# valoarea poate fi orice tip de date

# numere: int, float
x = 10
x = 3.5
# string-uri - siruri de caractere
x = "abc"
x = 'abc'
# operatori pe stringuri
# concatenare +
a = "Hello"
b = "World"
print(a+" "+b)
# repetare *
a = "A"
print(a*5)
# metode string
# upper, lower, strip, replace, split, find, join

s = "  Hello World  "
s = s.upper().strip()
print(s)

# liste
fructe = ["mar", "banana", "cireasa"]
lista_numere = [1, 2, 3, 4.5, 5]

# metode
# append - adauga element
fructe.append("portocala")
print(fructe)
# remove - sterge element dupa valoare
fructe.remove("banana")
print(fructe)
# pop - sterge element dupa index
fructe.pop(2)
print(fructe)

# indexare
# incepe de la 0
# index: 0    1   2   3   4
lista = [10, 20, 30, 40, 50]

print(lista[2])

# index negativ
print(lista[-1])  # ultimul element

# slicing
# sublista = lista[start:stop:pas]
print(lista[1:4:2])

# valabil si pentru siruri de caractere
text = "Hello World"
print(text[1:4:2])

# len() - lungime lista sau sir
n = len(lista)
print(n)

# structuri decizionale
# if, elif, else

# if conditie:
#     bloc cod pentru conditie True
# elif alta_conditie:
#	 bloc cod pentru alta_conditie True si conditie False
# elif alta_conditie2:
#     bloc cod pentru alta_conditie2 True si conditiile anterioare False
# else:
#     bloc cod pentru toate conditiile False

x = 22
if x % 3 == 0:
	x *= 10
elif x % 5 == 0:
	x += 5
else:
	x -= 2
print(x)

# cum verific daca un numar e par
if x % 2 == 0:
	print("Numarul este par")
else:
	print("Numarul este impar")

# cum verific element in lista
fruct = "mar"
if fruct in fructe:
	print(f"{fruct} se afla in lista de fructe")
else:
	print(f"{fruct} nu se afla in lista de fructe")

# structuri repetitive
# for si while
# for
# - numar stiut de pasi
# - parcurs elemente din liste/siruri

lista = [10, 20, 30, 40, 50]
fructe = ["mar", "banana", "cireasa"]
for x in lista:
	print(x)

# parcurgere pe index cu range()
for i in range(len(fructe)):	# i = 0, 1, 2
	fruct = fructe[i]			# fructe[i] = fructe[0], fructe[1], fructe[2]
	print(fruct)

# while
# - numar necunoscut de pasi, se repeta pana cand o conditie devine falsa

n = 5
while n > 0:
	print(n)
	n -= 1

# parcurgerea cifrelor unui numar
x = 12345
while x > 0:
	cifra = x % 10	 # extrag ultima cifra
	x //= 10	 # elimin ultima cifra
	print(cifra)

# functii
# def nume(parametrii):
#     bloc cod pe care il refolisim
#     return valoarea de returnat a functiei

# apel functie: nume(argumente)
# argumente = valori pentru parametrii

def adunare(a,b):
	return a + b

suma = adunare(10, 20)
print(suma)

# matrici - lista formata din liste
print("--------------------------")
matrice = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9],
	[10, 11, 12]
]
# print(matrice[1][2])

# numarul de linii
numar_linii = len(matrice)
print(numar_linii)
# numarul de coloane
numar_coloane = len(matrice[0])
print(numar_coloane)

# parcurgere cu for - indexare linii si coloane

for i in range(numar_linii-1, -1, -1):
	for j in range(numar_coloane-1, -1, -1):
		element = matrice[i][j]
		print(element)

print("--------------------------")
# parcurgere pe coloane, inversez
for j in range(numar_coloane):
	for i in range(numar_linii):
		element = matrice[i][j]
		print(element)

print("--------------------------")
for i in range(numar_linii):
	for j in range(numar_coloane):
		element = matrice[i][j]
		print(element, end=" ")
	print()