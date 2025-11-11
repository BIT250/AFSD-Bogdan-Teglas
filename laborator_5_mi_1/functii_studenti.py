lista=[1,2,7,4,8,4]
elimina_duplicate(lista:list[int]
def cmmdc(a, b):
    if a == 0 and b == 0:
        return "Eroare:CMMDC(0, 0) nu este definit."
    while b!= 0:
        a, b = b, a % b
    return a
print(f"CMMDC(12, 18) = {cmmdc(12, 18)}")
print( cmmdc(0, 0,))
lista=[2,3,4,5,6,5,4,2,6]
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
    while i < len(lista) - 1:
        if (i == 0 and lista[i] != lista[i + 1]) or \
           (i == len(lista) - 2 and lista[i + 1] != lista[i]) or \
           (lista[i] != lista[i - 1] and lista[i] != lista[i + 1]):
            return lista[i]
        i += 1

    print("Nu exista un numar unic")

if __name__ == '__main__':
    print(numar_unic(lista))