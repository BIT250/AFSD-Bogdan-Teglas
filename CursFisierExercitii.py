#Exercitiu
# Se da un fisier csv catalog.csv care contine nume si nota
# Sa se calculeze ptr fiecare elev
# Sa se returneze{"nume: " media}

import csv
catalog_medii = {}

def salvare_fisier_csv_ca_lista():
    f = open('catalog.csv', 'r')
    continut = list(csv.reader(f))
    print(continut)

    for linie in continut:
        #sari peste prima linie care contine header-ul
        if linie[0] == "nume":
            continue
        nume_elev = linie[0]
        nota_elev = float(linie[1])

        if nume_elev not in catalog_medii:
            catalog_medii[nume_elev] = []
            "note": [nota_elev]

        else:
            catalog_medii[nume_elev]["note"].append(nota_elev)

            for nume_elev in catalog_medii:
                note_elev = catalog_medii[nume_elev]["note"]
                media = sum(note_elev) / len(note_elev)
        print(linie)
if __name__ == '__main__':
    salvare_fisier_csv_ca_lista()