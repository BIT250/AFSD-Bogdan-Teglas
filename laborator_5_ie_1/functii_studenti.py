#16.
def timp_in_format(secunde: int) -> str:
    if secunde < 0:
        return "Eroare: numărul de secunde trebuie să fie nenegativ."
    h = secunde // 3600
    m = (secunde % 3600) // 60
    s = secunde % 60
    return f"{secunde} secunde înseamnă {h}:{m}:{s}."

def produs_scalar(v1: list[float], v2: list[float]) -> str:
    """
    Calculează produsul scalar al celor doi vectori (liste de aceeași lungime).
    Dacă lungimile diferă, returnează un mesaj de eroare.
    Exemplu: "Produsul scalar este 14.0."
    """
    if len(v1) != len(v2):
        return "Eroare: vectorii trebuie să aibă aceeași lungime."


    produs = sum(a * b for a, b in zip(v1, v2))

    return f"Produsul scalar este {produs}."

#functia nr.3
def cmmmc(a: int, b: int) -> str:
    if a == 0 or b == 0:
        return "Eroare: unul dintre numere este 0."
def cmmc(a, b):
    multiplu = max(a, b)
    while True:
        if multiplu % a == 0 and multiplu % b == 0:
            return multiplu
        multiplu += 1

def numar_divizori(n: int) -> str:
    if n <= 0:
        return "Eroare: numarul trebuie sa fie mai mare decat 0"
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1

    return f"Numărul de divizori ai lui {n} este {count}."
#Functia 19
from collections import Counter
from typing import List
def numar_unic(lista: List[int]) -> str:
    if not lista:
        return "Eroare: lista este goală."
    frecvente = Counter(lista)
    o_data = [num for num, cnt in frecvente.items() if cnt == 1]
    de_doua_ori = [num for num, cnt in frecvente.items() if cnt == 2]
    if len(o_data) == 1 and len(o_data) + len(de_doua_ori) == len(frecvente):
        return str(o_data[0])
    else:
        return "Eroare: condiția nu este respectată."
print(numar_unic([1, 2, 3, 2, 1]))

#17
def parola_valida(parola: str) -> str:
    """
    Parola este validă dacă are cel puțin 8 caractere, cel puțin o literă și cel puțin o cifră.

    :param parola: parola introdusa
    :return: Mesaj corespunzator criteriilor
    """
    mesaj = "Parola valida"
    if len(parola) < 8:
        mesaj = "Parola invalida (are sub 8 caractere)"
        return mesaj
    are_litera = False
    are_cifra = False

    for caracter in parola:
        if caracter.isalpha():
            are_litera = True
        if caracter.isdigit():
            are_cifra = True

    if not are_litera and not are_cifra:
        mesaj = "Parola invalida (trebuie sa contina cel putin o litera si cel putin o cifra)"
        return mesaj
    elif not are_litera:
        mesaj = "Parola invalida (trebuie sa contina cel putin o litera)"
        return mesaj
    elif not are_cifra:
        mesaj = "Parola invalida (trebuie sa contina cel putin o cifra)"
        return mesaj
    return mesaj
from typing import List
def rotire_dreapta(lista: List[int], k: int) -> str:
     if not lista:
         return "Lista este goală."
     k = k % len(lista)
     if k == 0:
         lista_rotita = lista
     else:
         lista_rotita = lista[-k:] + lista[:-k]
     return "Lista rotită: " + ", ".join(str(x) for x in lista_rotita)

#12.
def frecventa_litere(text: str) -> str:
    litere = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    text_de_afisat = ""
    for litera in litere:
        nr = text.count(litera)
        if nr > 0:
            text_de_afisat += f"({litera}, {nr}) "
    if text == " ":
        return "nu exista caractere"
    return text_de_afisat

print(frecventa_litere("meow meow meow meow"))