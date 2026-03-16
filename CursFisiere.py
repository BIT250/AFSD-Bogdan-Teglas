# Fisiere text (.txt)
# Fisiere CSV (.csv) - Comma Separated Values - valori separate prin virgula
# Fisiere JSON (.json) - JavaScript Object Notation - format de date struct

# Pentru a lucra cu fisiere in Python, folosim functia open() care are urmatoarea sintaxa:

nume_fisier = "fisier_text.txt"

# modurile de deschidere a fisierelor sunt:
# 'r' - read (citire) - deschide fisierul pentru citi
# 'w' - write (scriere) - deschide fisierul pentru scriere, daca fisierul exista deja, acesta va fi suprascris
# 'a' - append (adaugare) - deschide fisierul pentru adaugare, daca fisierul exista deja, noile date vor fi adaugate la

mod_deschidere = 'r'

f = open(nume_fisier, mod_deschidere)
pass

# citire continut fisier - metoda read()

continut_citit = f.read()

f.close()
# print(continut_citit)

# citire linie cu linie - metoda readline()
f = open(nume_fisier, 'r')
linie_citita = f.readline()
print(linie_citita)
f.close()

# read lines - metoda readlines() - returneaza o lista cu toate liniile din fisier
f = open(nume_fisier, 'r')
linii_citite = f.readlines()
print(linii_citite)
f.close()

# deschidere fisier cu with as
with open(nume_fisier, 'r') as f:
    continut_citit = f.read()
    print(continut_citit)

with open(nume_fisier, 'r') as f:
    linii_citite = f.readlines()
    print(linii_citite)


# Deschiderea fisierelor - open() - cu modurile 'r', 'w', 'a'
# Citirea fisierelo text - metodele read(), readline(), readlines()

# Scrierea in fisiere text - metodele write(), writelines()

f = open(nume_fisier, 'a')
text = "\nAlt text care va fi scris in fisier"
f.write(text)
f.close()


# scrierea cu writelines
f = open(nume_fisier, 'a')
linii_de_scris = ["\nLinie 1", "\nLinie 2", "\nLinie 3"]
f.writelines(linii_de_scris)

# pentru csv
import csv

with open('fisier_csv.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for linie in reader:
        print(linie)

# pentru json
import json
with open("fisier_json.json", "r") as jsonfile:
    data = json.load(jsonfile)
    print(type(data))

# scriere in fisier json
data_de_scris = {
    "nume": "Alice",
    "varsta": 30,
    "oras": "Bucuresti"
}
with open("fisier_json.json", "w") as jsonfile:
    json.dump(data_de_scris, jsonfile, indent=4)