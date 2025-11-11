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

    while i < len(lista) - 1:
        if (i == 0 and lista[i] != lista[i + 1]) or \
           (i == len(lista) - 2 and lista[i + 1] != lista[i]) or \
           (lista[i] != lista[i - 1] and lista[i] != lista[i + 1]):
            return lista[i]
        i += 1

    print("Nu exista un numar unic")

if __name__ == '__main__':
    print(numar_unic(lista))