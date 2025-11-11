#Functie Filtreaza Pare (6)
def filtreaza_pare(lista):
    print(lista)
    numere_pare = []
    for numar in lista:
        if numar % 2 == 0:
            numere_pare.append(numar)
    print(numere_pare)
    if not numere_pare:
        return "nu exista numere pare"
    return numere_pare
#FUNCTIA 5
def lista_prime_pana_la(n: int) -> str:
    prime = []

    #  pana la 2
    for numar in range(2, n + 1):
        este_prim = True  # daca prim

        # verificam
        for divizor in range(2, numar):
            if numar % divizor == 0:
                este_prim = False
                break

def suma_cifrelor(n: int):
    s = 0
    c = n
    if n == 0:
        return 0
    else:
        while n!=0:
            s = s+(n%10)
            n//=10
    return f"Suma cifrelor lui {c} este {s}"

    print (f"Suma cifrelor lui {c} este {s}")

# media poderata (8)
def medie_ponderata(valori: list[float], ponderi: list[float]):
    if len(list) != len(ponderi):
        print("error")
    suma_produse = sum(valoare * ponderi for valoare, ponderi in zip(list, ponderi))
    suma_ponderi = sum(ponderi)
    if suma_ponderi == 0:
        return print("error ponderea este 0")

def cmmmc(a,b):
    produs = a*b
    if produs == 0:
        return "Imposibil"
    else:
        while a != b:
            if a > b:
                a-=b
            else:
                b-=a
        return produs//a
