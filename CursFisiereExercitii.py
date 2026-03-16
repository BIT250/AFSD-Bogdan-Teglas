# # Exercitiu 1
# from itertools import count
#
# # Se da un fisier text (text.txt), sa numaram frecventa fiecarui cuvant (de cate ori apare fiecare cuvant in fisier)
# # sa afisam {"cuvant1": frecventa, "cuvant2": frecventa, ...}
# frecventa_cuvinte = {}
#
# # deschida fisier text si sa salveze stringul citit
# def salvare_fisier_ca_string():
#     # 1. deschidem fisierul text pentru citire cu open() si r
#     f = open("text.txt", 'r')
#
#     # 2. citim continutul
#     continut = f.read()
#
#     # 3. inchidem fisierul
#     f.close()
#     return continut
#
# def frecventa(text):
#     # metode siruri de caractere
#     # strip() - elimina spatiile
#     text = text.strip()
#     # split() - imparte textul in cuvinte
#     cuvinte = text.split()
#
#     for cuvant in cuvinte:
#         if cuvant not in frecventa_cuvinte:
#             frecventa_cuvinte[cuvant] = cuvinte.count(cuvant)
#
#     print(frecventa_cuvinte)
#
#
# if __name__ == '__main__':
#     text = salvare_fisier_ca_string()
#     print(text)
#     print("-----------------------------")
#     frecventa(text)

# Exercitiu 2
# Se da un fisier csv catalog.csv care contine nume,nota
# sa se calculeze media pentru fiecare elev
# sa se returneze {"nume": {"media": valoare, "note": [lista de note]}, ...}
import csv
catalog_medii = {}

def salvare_fisier_csv_ca_lista():
    f = open('catalog.csv', 'r')
    continut = list(csv.reader(f))

    for linie in continut:
        # sarim peste prima linie care contine header-ul
        if linie[0] == "nume":
            continue
        nume_elev = linie[0]
        nota_elev = float(linie[1])

        if nume_elev not in catalog_medii:
            catalog_medii[nume_elev] = {
                "note": [nota_elev]
            }
        else:
            catalog_medii[nume_elev]["note"].append(nota_elev)

    for nume_elev in catalog_medii:
        note_elev = catalog_medii[nume_elev]["note"]
        media = sum(note_elev) / len(note_elev)
        catalog_medii[nume_elev]["media"] = round(media, 2)

    print(catalog_medii)
if __name__ == '__main__':
    salvare_fisier_csv_ca_lista()