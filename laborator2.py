import csv
import os


def initializare_glosar():
    """
    Inițializează glosarul cu câțiva termeni exemplu.
    """
    return {
        "variabilă": {
            "definitie": "nume asociat unei valori",
            "categorie": "fundamente",
            "exemplu": "x = 10"
        },
        "dicționar": {
            "definitie": "structură de date bazată pe perechi cheie-valoare",
            "categorie": "structuri de date",
            "exemplu": "{'a': 1, 'b': 2}"
        }
    }


def citeste_text_nevid(mesaj):
    """
    Cere utilizatorului un text nevid.
    """
    while True:
        text = input(mesaj).strip()
        if text != "":
            return text
        print("Eroare: câmpul nu poate fi gol.")


def normalizeaza_termen(termen):
    """
    Normalizează termenul pentru a evita diferențele de litere mari/mici.
    """
    return termen.strip().lower()


def afiseaza_termen(termen, informatii):
    """
    Afișează datele unui termen.
    """
    print("\n-------------------------")
    print(f"Termen: {termen}")
    print(f"Definiție: {informatii['definitie']}")
    print(f"Categorie: {informatii['categorie']}")
    print(f"Exemplu: {informatii['exemplu']}")
    print("-------------------------")


def adauga_termen(glosar):
    """
    Adaugă un termen nou în glosar.
    """
    termen = normalizeaza_termen(citeste_text_nevid("Introduceți termenul nou: "))

    if termen in glosar:
        print("Eroare: termenul există deja în glosar.")
        return

    definitie = citeste_text_nevid("Introduceți definiția: ")
    categorie = citeste_text_nevid("Introduceți categoria: ")
    exemplu = citeste_text_nevid("Introduceți exemplul: ")

    glosar[termen] = {
        "definitie": definitie,
        "categorie": categorie,
        "exemplu": exemplu
    }

    print("Termenul a fost adăugat cu succes.")


def cautare_exacta(glosar):
    """
    Caută exact un termen în glosar.
    """
    termen = normalizeaza_termen(citeste_text_nevid("Introduceți termenul căutat: "))

    if termen in glosar:
        afiseaza_termen(termen, glosar[termen])
    else:
        print("Termenul nu există în glosar.")


def cautare_fragment(glosar):
    """
    Caută termenii care conțin un fragment de text.
    """
    fragment = normalizeaza_termen(citeste_text_nevid("Introduceți fragmentul căutat: "))

    rezultate = []

    for termen, informatii in glosar.items():
        if (fragment in termen.lower() or
                fragment in informatii["definitie"].lower() or
                fragment in informatii["categorie"].lower() or
                fragment in informatii["exemplu"].lower()):
            rezultate.append((termen, informatii))

    if len(rezultate) == 0:
        print("Nu s-au găsit termeni pentru fragmentul introdus.")
    else:
        print(f"\nS-au găsit {len(rezultate)} rezultat(e):")
        for termen, informatii in rezultate:
            afiseaza_termen(termen, informatii)


def actualizeaza_termen(glosar):
    """
    Actualizează informațiile unui termen existent.
    """
    termen = normalizeaza_termen(citeste_text_nevid("Introduceți termenul de actualizat: "))

    if termen not in glosar:
        print("Eroare: termenul nu există în glosar.")
        return

    print("\nCe doriți să modificați?")
    print("1. definiție")
    print("2. categorie")
    print("3. exemplu")

    optiune = input("Alegeți opțiunea: ").strip()

    if optiune == "1":
        valoare_noua = citeste_text_nevid("Introduceți noua definiție: ")
        glosar[termen]["definitie"] = valoare_noua
        print("Definiția a fost actualizată cu succes.")
    elif optiune == "2":
        valoare_noua = citeste_text_nevid("Introduceți noua categorie: ")
        glosar[termen]["categorie"] = valoare_noua
        print("Categoria a fost actualizată cu succes.")
    elif optiune == "3":
        valoare_noua = citeste_text_nevid("Introduceți noul exemplu: ")
        glosar[termen]["exemplu"] = valoare_noua
        print("Exemplul a fost actualizat cu succes.")
    else:
        print("Eroare: opțiune invalidă.")


def sterge_termen(glosar):
    """
    Șterge un termen din glosar.
    """
    termen = normalizeaza_termen(citeste_text_nevid("Introduceți termenul de șters: "))

    if termen in glosar:
        del glosar[termen]
        print("Termenul a fost șters cu succes.")
    else:
        print("Eroare: termenul nu există în glosar.")


def afiseaza_glosar(glosar):
    """
    Afișează toți termenii din glosar.
    """
    if len(glosar) == 0:
        print("Glosarul este gol.")
        return

    print("\n===== GLOSAR COMPLET =====")
    for termen in sorted(glosar.keys()):
        afiseaza_termen(termen, glosar[termen])


def afiseaza_statistici(glosar):
    """
    Afișează statistici despre glosar.
    """
    total_termeni = len(glosar)
    categorii = {}

    for informatii in glosar.values():
        categorie = informatii["categorie"]
        if categorie in categorii:
            categorii[categorie] += 1
        else:
            categorii[categorie] = 1

    print("\n===== STATISTICI =====")
    print(f"Număr total de termeni: {total_termeni}")

    if total_termeni == 0:
        print("Nu există termeni în glosar.")
        return

    print("Număr de termeni pe categorii:")
    for categorie, numar in categorii.items():
        print(f"- {categorie}: {numar}")


def salveaza_csv(glosar, nume_fisier="glosar.csv"):
    """
    Salvează glosarul într-un fișier CSV.
    """
    try:
        with open(nume_fisier, "w", newline="", encoding="utf-8") as fisier:
            writer = csv.writer(fisier)
            writer.writerow(["termen", "definitie", "categorie", "exemplu"])

            for termen, informatii in glosar.items():
                writer.writerow([
                    termen,
                    informatii["definitie"],
                    informatii["categorie"],
                    informatii["exemplu"]
                ])

        print(f"Glosarul a fost salvat cu succes în fișierul '{nume_fisier}'.")
    except Exception as e:
        print(f"Eroare la salvarea fișierului: {e}")


def incarca_csv(nume_fisier="glosar.csv"):
    """
    Încarcă glosarul dintr-un fișier CSV.
    """
    if not os.path.exists(nume_fisier):
        print(f"Eroare: fișierul '{nume_fisier}' nu există.")
        return None

    glosar_nou = {}

    try:
        with open(nume_fisier, "r", newline="", encoding="utf-8") as fisier:
            reader = csv.DictReader(fisier)

            for linie in reader:
                termen = normalizeaza_termen(linie["termen"])
                glosar_nou[termen] = {
                    "definitie": linie["definitie"].strip(),
                    "categorie": linie["categorie"].strip(),
                    "exemplu": linie["exemplu"].strip()
                }

        print(f"Glosarul a fost încărcat cu succes din fișierul '{nume_fisier}'.")
        return glosar_nou

    except Exception as e:
        print(f"Eroare la încărcarea fișierului: {e}")
        return None


def afiseaza_meniu():
    """
    Afișează meniul principal.
    """
    print("\n========== MENIU PRINCIPAL ==========")
    print("1. Adăugare termen")
    print("2. Căutare exactă")
    print("3. Căutare după fragment")
    print("4. Actualizare termen")
    print("5. Ștergere termen")
    print("6. Afișare glosar complet")
    print("7. Statistici")
    print("8. Salvare în CSV")
    print("9. Încărcare din CSV")
    print("0. Ieșire")
    print("=====================================")


def ruleaza_aplicatia():
    """
    Rulează meniul interactiv al aplicației.
    """
    glosar = initializare_glosar()

    while True:
        afiseaza_meniu()
        optiune = input("Alegeți o opțiune: ").strip()

        if optiune == "1":
            adauga_termen(glosar)

        elif optiune == "2":
            cautare_exacta(glosar)

        elif optiune == "3":
            cautare_fragment(glosar)

        elif optiune == "4":
            actualizeaza_termen(glosar)

        elif optiune == "5":
            sterge_termen(glosar)

        elif optiune == "6":
            afiseaza_glosar(glosar)

        elif optiune == "7":
            afiseaza_statistici(glosar)

        elif optiune == "8":
            nume_fisier = input("Introduceți numele fișierului CSV (sau Enter pentru glosar.csv): ").strip()
            if nume_fisier == "":
                nume_fisier = "glosar.csv"
            salveaza_csv(glosar, nume_fisier)

        elif optiune == "9":
            nume_fisier = input("Introduceți numele fișierului CSV (sau Enter pentru glosar.csv): ").strip()
            if nume_fisier == "":
                nume_fisier = "glosar.csv"
            glosar_incarcat = incarca_csv(nume_fisier)
            if glosar_incarcat is not None:
                glosar = glosar_incarcat

        elif optiune == "0":
            print("Programul s-a închis.")
            break

        else:
            print("Eroare: opțiune invalidă. Încercați din nou.")


if __name__ == "__main__":
    ruleaza_aplicatia()

