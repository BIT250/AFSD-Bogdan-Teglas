text = """ Documente pentru scoala."""

text = text.replace(_old: ".",  _new:"") .replace(_old: "," _new:) ##pentru a scoate punctele, semnele de punctuatie.

semne_punctuatie = "! . , ?"

for character in text:
    if characater in semne_punctuatie:
        text = text.replace(character, _new:"")

print(text)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#indexare
#de la 0 la 9(len())

print(len(lista)) #10
#parcurgere cu cu index
#range(strat, stop, step) => [strat, strat + step, strat + 2 * step,..., stop - 1]
#valori implicite: strat = 0, step = 1
#range(10) => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#range(1, 8, 2) => [1, 3, 5, 7]

#index: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#lista: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range (len(lista)):
    print(f"Index {i} are valoare {lista[i]}")

#accesare valoare cu index
print(lista[5]) # "6"

#parcurgere direct a valorilor
for value in lista:
    print(f"Index {value} are valoare {lista[value]}")

#operatori de liste: +, *, in, not in
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1 + lista2 #concatenarea
print(lista3) #[1, 2, 3, 4, 5, 6]

#repetare *
lista4 = lista1 * 3
print(lista4) #[1, 2, 3, 1, 2, 3, 1, 2, 3]

lista_de_0 = [0] * 100
print(lista_de_0) #[0, 0, 0, ...., 0] (100 de 0-uri)

#adaugare element in lista: append, insert
lista_test = [1, 2, 3]
element_de_adaugat = 4

#append - adaugat la final
lista_test.append(element_de_adaugat)
print(lista_test)  #[1, 2, 3, 4]

#insert - adaugat la o pozitie specifica
lista_test.insert (element_de_adaugat)
print(lista_test) #[1, 4, 2, 3, 2]


#stergere element din lista: remove, pop, del

#remove - sterge prima apartie a unui element
lista_test.remove(4)
print(lista_test)

#pop - sterge elementul de la o pozitie specifica si il returneaza
print(lista_test)
lista_test.pop(2)
print(lista_test)

#cautare element in lista: in, index
print(2 in lista_test) #True
print(100 in lista_test) #Flase

#index - returneaza indexul primei aparitii a unui element
print(lista_test.index("4"))


#max min sum
lista_numere = [10, 20, 5, 30, 15]
#cel mai mare numar
print(max(lista_numere))
#cel mai mic numar
print(min(lista_numere))
#suma numerelor
print(sum(lista_numere))
#media numerelor
avg = sum(lista_numere) / len(lista_numere)
print(avg)

#sortare lista: sort, sorted
#sort - sorteaza lista in-place (modifica lista originala)
print(lista_numere)
lista_numere.sort(reverse = True)
print(lista_numere) #[5, 10 15, 20, 30]
#sorted - returneaza o copie sortata a listei
lista_sortata = sorted(lista_numere)
print(lista_numere)
print(lista_sortata)

#liste
#parcurgere
#adaugarea
#stergerea
#max / min / sum
#sortarea

#afisarea numerelor de la 1 la 100
for i in range (1, 101):
    print(i, end=" ")
#end = " " => pentru a afisa numerele una dupa alta

print()
#suma numerelor dintr-o lista fara sum
suma_numerelor = 0
for i in range(1, 101):
    suma_numerelor += i
print(suma_numerelor)

#suma numerelor de la 1 la 100
print(100 * 101 // 2)

#suma numerelor impare dintr-o lista
lista_nuemerelor_2 = [1, 202, 123, 4, 5, 7, 8 900, 10]
 = 0
    for numa in lista_nuemerelor_2:
        if numarele % 2 != 0
            suma_nuemerelr += numa

print(suma_numerelor)


#afisarea numerelor de 2 cifre:
for numar in lista_numere_2:
    if 10 <= numar <= 99:
        print(numar, end=" ")
print()

