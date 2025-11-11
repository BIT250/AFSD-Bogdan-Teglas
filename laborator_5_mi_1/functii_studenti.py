def lista_prime_pana_la(n: int) -> str:
    if not isinstance(n, int) or n < 2:
        return "Eroare: introduceți un număr întreg mai mare sau egal cu 2."

    def este_prim(numar):
        if numar < 2:
            return False
        for i in range(2, int(numar ** 0.5) + 1):
            if numar % i == 0:
                return False
        return True
    prime = [str(i) for i in range(2, n + 1) if este_prim(i)]
    if prime:
        return f"Numere prime până la {n}: {', '.join(prime)}"
    else:
        return f"Nu există numere prime până la {n}."

def cmmdc(a, b):
    if a == 0 and b == 0:
        return "Eroare:CMMDC(0, 0) nu este definit."
    while b!= 0:
        a, b = b, a % b
    return a

def produs_scalar(v1, v2)-> str:
    suma=0
    if len(v1)!=len(v2):
        return "Eroare, vectorii nu au aceeasi lungime."
    i=0
    while i<len(v1):
        produs = (v1[i] * v2[i])
        i+=1
        suma+=produs
    return f"Produsul scalar este {produs}"

def numar_unic(lista: list[int]):
    def bubble_sort_baza(lista):
        n = len(lista)
        schimbat = True
        while schimbat:
            schimbat = False
            for i in range(n - 1):
                if lista[i] > lista[i + 1]:
                    lista[i], lista[i + 1] = lista[i + 1], lista[i]
                    schimbat = True
        return lista

    lista = bubble_sort_baza(lista)
    i = 0


def timp_in_format(secunde: int) -> str:
    if secunde<0:
        return "Eroare: numărul de secunde trebuie să fie nenegativ."
    ore=secunde//3600
    minute=(secunde%3600)//60
    secunde_ramase=secunde%60
    hh=f"{ore:02d}"
    mm=f"{minute:02d}"
    ss=f"{secunde_ramase:02d}"
    timp_format=f"{hh}:{mm}:{ss}"
    return f"{secunde} secunde inseamna {timp_format}."
def este_isograma(text: str) -> str:
    filtrat = text.replace(" ", "").lower()
    if len(set(filtrat)) == len(filtrat):
        return f"'{text}' este isogramă."
    else:
        return f'\'{text}\' NU este isogramă.'
