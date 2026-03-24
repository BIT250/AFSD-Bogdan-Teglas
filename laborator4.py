import json

fisier = "competitori.json"


def citeste_numar(text):
    while True:
        try:
            x = int(input(text))
            return x
        except:
            print("Introdu un numar intreg valid.")


def citeste_din_json():
    lista = []

    try:
        f = open(fisier, "r", encoding="utf-8")
        data = json.load(f)
        f.close()

        if type(data) != list:
            print("Fisierul JSON nu contine o lista.")
            return []

        for x in data:
            if type(x) == dict:
                if "nume" in x and "punctaj" in x and "timp" in x:
                    nume = str(x["nume"]).strip()

                    if nume != "":
                        try:
                            punctaj = int(x["punctaj"])
                            timp = int(x["timp"])

                            competitor = {
                                "nume": nume,
                                "punctaj": punctaj,
                                "timp": timp
                            }

                            lista.append(competitor)
                        except:
                            pass

        return lista

    except FileNotFoundError:
        print("Fisierul JSON nu exista. Programul porneste cu lista goala.")
        return []
    except json.JSONDecodeError:
        print("Fisier JSON invalid.")
        return []
    except:
        print("Eroare la citirea fisierului.")
        return []


def salveaza_in_json(lista):
    try:
        f = open(fisier, "w", encoding="utf-8")
        json.dump(lista, f, ensure_ascii=False, indent=2)
        f.close()
        print("Datele au fost salvate in JSON.")
    except:
        print("Eroare la salvarea in fisier.")


def afisare(lista):
    if len(lista) == 0:
        print("\nLista competitorilor este goala.")
        return

    print("\nLista competitorilor:")
    print("-" * 50)
    print("Nr  Nume                     Punctaj   Timp")
    print("-" * 50)

    for i in range(len(lista)):
        c = lista[i]
        print(f"{i + 1:<3} {c['nume']:<24} {c['punctaj']:<9} {c['timp']}")
    print("-" * 50)


def adauga(lista):
    print("\nAdaugare competitor")

    nume = input("Nume: ").strip()

    if nume == "":
        print("Nu se accepta competitor fara nume.")
        return

    punctaj = citeste_numar("Punctaj: ")
    timp = citeste_numar("Timp: ")

    competitor = {
        "nume": nume,
        "punctaj": punctaj,
        "timp": timp
    }

    lista.append(competitor)
    print("Competitor adaugat cu succes.")


def actualizeaza(lista):
    if len(lista) == 0:
        print("\nLista este goala.")
        return

    print("\nActualizare competitor")
    nume = input("Introdu numele competitorului: ").strip()

    if nume == "":
        print("Numele nu poate fi gol.")
        return

    gasit = False

    for i in range(len(lista)):
        if lista[i]["nume"].lower() == nume.lower():
            gasit = True
            print("Competitor gasit:", lista[i]["nume"])

            punctaj_nou = citeste_numar("Punctaj nou: ")
            timp_nou = citeste_numar("Timp nou: ")

            lista[i]["punctaj"] = punctaj_nou
            lista[i]["timp"] = timp_nou

            print("Rezultatul a fost actualizat.")
            break

    if gasit == False:
        print("Competitorul nu exista.")


def mai_bun(a, b):
    # punctaj descrescator
    if a["punctaj"] > b["punctaj"]:
        return True
    if a["punctaj"] < b["punctaj"]:
        return False

    # timp crescator
    if a["timp"] < b["timp"]:
        return True
    if a["timp"] > b["timp"]:
        return False

    # nume alfabetic
    if a["nume"].lower() < b["nume"].lower():
        return True
    return False


def partition(lista, low, high):
    pivot = lista[high]
    i = low - 1

    for j in range(low, high):
        if mai_bun(lista[j], pivot):
            i = i + 1
            lista[i], lista[j] = lista[j], lista[i]

    lista[i + 1], lista[high] = lista[high], lista[i + 1]
    return i + 1


def quicksort(lista, low, high):
    if low < high:
        p = partition(lista, low, high)
        quicksort(lista, low, p - 1)
        quicksort(lista, p + 1, high)


def sorteaza(lista):
    if len(lista) == 0:
        print("\nLista este goala.")
        return

    quicksort(lista, 0, len(lista) - 1)
    print("\nSortarea a fost realizata cu Quicksort.")


def clasament(lista):
    if len(lista) == 0:
        print("\nNu exista competitori.")
        return

    copie = []
    for c in lista:
        copie.append({
            "nume": c["nume"],
            "punctaj": c["punctaj"],
            "timp": c["timp"]
        })

    quicksort(copie, 0, len(copie) - 1)

    print("\nClasament final:")
    print("-" * 55)
    print("Loc  Nume                     Punctaj   Timp")
    print("-" * 55)

    loc = 1

    for i in range(len(copie)):
        if i == 0:
            loc = 1
        else:
            anterior = copie[i - 1]
            curent = copie[i]

            if curent["punctaj"] == anterior["punctaj"] and curent["timp"] == anterior["timp"]:
                loc = loc
            else:
                loc = i + 1

        print(f"{loc:<4} {copie[i]['nume']:<24} {copie[i]['punctaj']:<9} {copie[i]['timp']}")

    print("-" * 55)


def statistici(lista):
    if len(lista) == 0:
        print("\nNu exista competitori pentru statistici.")
        return

    total = len(lista)
    max_punctaj = lista[0]["punctaj"]
    min_punctaj = lista[0]["punctaj"]
    suma = 0
    cel_mai_bun_timp = lista[0]["timp"]

    for c in lista:
        if c["punctaj"] > max_punctaj:
            max_punctaj = c["punctaj"]

        if c["punctaj"] < min_punctaj:
            min_punctaj = c["punctaj"]

        if c["timp"] < cel_mai_bun_timp:
            cel_mai_bun_timp = c["timp"]

        suma = suma + c["punctaj"]

    media = suma / total

    print("\nStatistici:")
    print("Numar total de competitori:", total)
    print("Punctaj maxim:", max_punctaj)
    print("Punctaj minim:", min_punctaj)
    print("Media punctajelor:", round(media, 2))
    print("Cel mai bun timp:", cel_mai_bun_timp)


def meniu():
    print("\n===== MENIU =====")
    print("1. Afisare lista competitori")
    print("2. Adauga competitor")
    print("3. Actualizeaza competitor")
    print("4. Sorteaza competitori")
    print("5. Afiseaza clasament final")
    print("6. Afiseaza statistici")
    print("7. Salveaza in JSON")
    print("0. Iesire")


def main():
    lista = citeste_din_json()
    print("S-au incarcat", len(lista), "competitori din fisier.")

    while True:
        meniu()
        op = input("Alege optiunea: ").strip()

        if op == "1":
            afisare(lista)

        elif op == "2":
            adauga(lista)

        elif op == "3":
            actualizeaza(lista)

        elif op == "4":
            sorteaza(lista)

        elif op == "5":
            clasament(lista)

        elif op == "6":
            statistici(lista)

        elif op == "7":
            salveaza_in_json(lista)

        elif op == "0":
            print("Programul s-a inchis.")
            break

        else:
            print("Optiune invalida.")


main()