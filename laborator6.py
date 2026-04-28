import json
import os


def incarca_investitii(nume_fisier):
    if not os.path.exists(nume_fisier):
        print("Eroare: fisierul JSON nu exista.")
        return []

    try:
        with open(nume_fisier, "r", encoding="utf-8") as f:
            date = json.load(f)
    except json.JSONDecodeError:
        print("Eroare: fisierul JSON este incorect.")
        return []

    if not isinstance(date, list) or len(date) == 0:
        print("Eroare: fisierul este gol sau nu contine o lista.")
        return []

    campuri_obligatorii = ["nume", "cost", "profit", "categorie", "risc"]

    for investitie in date:
        for camp in campuri_obligatorii:
            if camp not in investitie:
                print(f"Eroare: lipseste campul {camp}.")
                return []

        if investitie["cost"] <= 0 or investitie["profit"] < 0:
            print("Eroare: costul sau profitul nu este valid.")
            return []

    return date


def afiseaza_investitii(investitii):
    print("\nLISTA INVESTITIILOR DISPONIBILE")
    print("-" * 70)

    for inv in investitii:
        raport = inv["profit"] / inv["cost"]
        print(
            f"Nume: {inv['nume']} | "
            f"Cost: {inv['cost']} | "
            f"Profit: {inv['profit']} | "
            f"Categorie: {inv['categorie']} | "
            f"Risc: {inv['risc']} | "
            f"Profit/Cost: {raport:.2f}"
        )


def analiza_descriptiva(investitii):
    print("\nANALIZA DESCRIPTIVA")
    print("-" * 70)

    print(f"Numar total investitii: {len(investitii)}")

    cost_minim = min(investitii, key=lambda x: x["cost"])
    cost_maxim = max(investitii, key=lambda x: x["cost"])
    profit_maxim = max(investitii, key=lambda x: x["profit"])

    print(f"Investitia cu cost minim: {cost_minim['nume']} - {cost_minim['cost']}")
    print(f"Investitia cu cost maxim: {cost_maxim['nume']} - {cost_maxim['cost']}")
    print(f"Investitia cu profit maxim: {profit_maxim['nume']} - {profit_maxim['profit']}")

    categorii = {}
    riscuri = {}

    for inv in investitii:
        categorii[inv["categorie"]] = categorii.get(inv["categorie"], 0) + 1
        riscuri[inv["risc"]] = riscuri.get(inv["risc"], 0) + 1

    print("\nDistributie pe categorii:")
    for categorie, nr in categorii.items():
        print(f"{categorie}: {nr}")

    print("\nDistributie pe niveluri de risc:")
    for risc, nr in riscuri.items():
        print(f"{risc}: {nr}")


def filtrare_ordonare(investitii):
    lista = investitii.copy()

    print("\nFILTRARE SI ORDONARE")
    print("1. Filtrare dupa categorie")
    print("2. Filtrare dupa risc")
    print("3. Ordonare dupa cost")
    print("4. Ordonare dupa profit")
    print("5. Ordonare dupa raport profit/cost")
    print("0. Fara filtrare/ordonare")

    optiune = input("Alege optiunea: ")

    if optiune == "1":
        categorie = input("Introdu categoria: ").lower()
        lista = [inv for inv in lista if inv["categorie"].lower() == categorie]

    elif optiune == "2":
        risc = input("Introdu riscul: ").lower()
        lista = [inv for inv in lista if inv["risc"].lower() == risc]

    elif optiune == "3":
        lista.sort(key=lambda x: x["cost"])

    elif optiune == "4":
        lista.sort(key=lambda x: x["profit"], reverse=True)

    elif optiune == "5":
        lista.sort(key=lambda x: x["profit"] / x["cost"], reverse=True)

    if len(lista) == 0:
        print("Nu exista investitii care respecta filtrul.")
    else:
        afiseaza_investitii(lista)

    return lista


def citeste_buget():
    while True:
        try:
            buget = int(input("\nIntrodu bugetul disponibil: "))
            if buget <= 0:
                print("Bugetul trebuie sa fie pozitiv.")
            else:
                return buget
        except ValueError:
            print("Introdu o valoare numerica valida.")


def programare_dinamica(investitii, buget, exclude_risc_ridicat=False):
    if exclude_risc_ridicat:
        investitii = [inv for inv in investitii if inv["risc"] != "ridicat"]

    n = len(investitii)

    dp = [[0 for _ in range(buget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        cost = investitii[i - 1]["cost"]
        profit = investitii[i - 1]["profit"]

        for b in range(buget + 1):
            if cost <= b:
                dp[i][b] = max(
                    dp[i - 1][b],
                    profit + dp[i - 1][b - cost]
                )
            else:
                dp[i][b] = dp[i - 1][b]

    profit_optim = dp[n][buget]

    investitii_selectate = []
    b = buget

    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            inv = investitii[i - 1]
            investitii_selectate.append(inv)
            b -= inv["cost"]

    investitii_selectate.reverse()

    cost_total = sum(inv["cost"] for inv in investitii_selectate)
    buget_ramas = buget - cost_total

    return profit_optim, investitii_selectate, cost_total, buget_ramas, dp


def afiseaza_tabel_dp(dp, limita_linii=10, limita_coloane=20):
    print("\nTABEL DP - afisare partiala")
    print("-" * 70)

    for i in range(min(len(dp), limita_linii)):
        print(dp[i][:limita_coloane])


def afiseaza_rezultat(buget, profit_optim, investitii_selectate, cost_total, buget_ramas):
    print("\nREZULTAT FINAL")
    print("-" * 70)
    print(f"Buget disponibil: {buget}")
    print(f"Profit optim: {profit_optim}")
    print(f"Cost total utilizat: {cost_total}")
    print(f"Buget ramas: {buget_ramas}")

    print("\nInvestitii selectate:")

    if len(investitii_selectate) == 0:
        print("Nu a fost selectata nicio investitie.")
    else:
        for inv in investitii_selectate:
            print(
                f"- {inv['nume']} | "
                f"Cost: {inv['cost']} | "
                f"Profit: {inv['profit']} | "
                f"Categorie: {inv['categorie']} | "
                f"Risc: {inv['risc']}"
            )


def explicatie_dp():
    print("\nEXPLICATIE PROGRAMARE DINAMICA")
    print("-" * 70)
    print("Problema este asemanatoare cu problema rucsacului 0/1.")
    print("Fiecare investitie poate fi aleasa cel mult o singura data.")
    print("Subproblema: dp[i][b] = profitul maxim folosind primele i investitii si bugetul b.")
    print("Caz de baza: dp[0][b] = 0, deoarece fara investitii profitul este 0.")
    print("Recurenta:")
    print("Daca investitia i incape in buget:")
    print("dp[i][b] = max(dp[i-1][b], profit_i + dp[i-1][b-cost_i])")
    print("Altfel:")
    print("dp[i][b] = dp[i-1][b]")


def compara_doua_bugete(investitii):
    print("\nCOMPARARE PENTRU DOUA BUGETE")
    buget1 = citeste_buget()
    buget2 = citeste_buget()

    rezultat1 = programare_dinamica(investitii, buget1)
    rezultat2 = programare_dinamica(investitii, buget2)

    print("\nRezultat pentru primul buget:")
    afiseaza_rezultat(buget1, rezultat1[0], rezultat1[1], rezultat1[2], rezultat1[3])

    print("\nRezultat pentru al doilea buget:")
    afiseaza_rezultat(buget2, rezultat2[0], rezultat2[1], rezultat2[2], rezultat2[3])


def meniu():
    investitii = incarca_investitii("investitii.json")

    if len(investitii) == 0:
        return

    while True:
        print("\nMENIU PRINCIPAL")
        print("1. Afiseaza investitiile disponibile")
        print("2. Analiza descriptiva")
        print("3. Filtrare si ordonare")
        print("4. Optimizare investitii cu programare dinamica")
        print("5. Optimizare fara investitii cu risc ridicat")
        print("6. Comparare pentru doua bugete")
        print("0. Iesire")

        optiune = input("Alege optiunea: ")

        if optiune == "1":
            afiseaza_investitii(investitii)

        elif optiune == "2":
            analiza_descriptiva(investitii)

        elif optiune == "3":
            filtrare_ordonare(investitii)

        elif optiune == "4":
            explicatie_dp()
            buget = citeste_buget()
            profit_optim, selectate, cost_total, buget_ramas, dp = programare_dinamica(investitii, buget)

            afisare = input("Vrei sa afisezi tabelul DP partial? da/nu: ")
            if afisare.lower() == "da":
                afiseaza_tabel_dp(dp)

            afiseaza_rezultat(buget, profit_optim, selectate, cost_total, buget_ramas)

        elif optiune == "5":
            print("\nRestrictie suplimentara: se exclud investitiile cu risc ridicat.")
            buget = citeste_buget()
            profit_optim, selectate, cost_total, buget_ramas, dp = programare_dinamica(
                investitii,
                buget,
                exclude_risc_ridicat=True
            )
            afiseaza_rezultat(buget, profit_optim, selectate, cost_total, buget_ramas)

        elif optiune == "6":
            compara_doua_bugete(investitii)

        elif optiune == "0":
            print("Program inchis.")
            break

        else:
            print("Optiune invalida.")


meniu()