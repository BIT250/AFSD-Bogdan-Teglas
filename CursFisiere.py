# Fisiere txt (.txt)
# Fisiere csv (.csv) -  Comma Separated Values - valori separate prin virgula
# Fisiere JSON(.json) - JavaScript Object Notation - format de date struct

# Pnetru a lucra cu fisiere in Paython, folosim fuctia open() care are urmatoarea structura:

nume_fisier = "fisier_text.txt"

# modurile de deschidere a fisierelor sunt:
# 'r' - read (citire) - deschide fisierul pentru citi
# 'w' - write ( scriere) - deschide fisierul pentru scriere, daca fisierul exista deja, acesta va fi suprascris
# 'a' - append (adaugare) - deschide fisierul pentru adaugare, daca fisierul exista deja, noile date vor fi adaugate la

mod_deschidere = 'r'

f = open(nume_fisier, mod_deschidere)
pass

#citire continut fisier - metoda read() citeste tot continutul fisierului si il returneaza ca un string

continut_citit = f.read()

f.close()
#print(continut.citit)

#citire linie cu linie - metoda readLine()
#read lines - metoda readlines() - returneaza o lista cu toate liniile din fisier
f = open(nume_fisier, 'r')
linii_citite = f.readlines()
print(linii_citite)
f.close()

#deshcidere fisier cu with as
with open(nume_fisier, 'r') as f:
    continut_citit = f.read()
    print(continut_citit)

with open(nume_fisier, 'r') as f:
    linii_citite = f.readlines()
    print(linii_citite)

# Deschiderea fisierelor - open() - cu modurile 'r', 'w', 'a'
# Citirea fisierelor text - metodele read(), readline(), readlines()

#Scrierea in fisere text - metodele write(), writelines()

f = open(nume_fisier, 'w')
text = "Acesta este un text scris in fisier."
f.write(text)
f.close()

#Scrierea cu writelines
f = open(nume_fisier, 'a')
linii_de_scris = ("\nlinie 1", "\nlinie 2", "\nlinie 3")
f.writelines(linii_de_scris)

#pentru csv
import csv

with open("fisier_csv.csv", 'a', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for linie in reader:
        print(linie)

