def in_binar(n: int) -> str:
    res = ''  # binary result
    while n > 0:
        res = str(n & 1) + res
        n >>= 1
    return res.zfill(8)


#13. cel_mai_frecvent_cuvant(text: str) -> str
#Determină cuvântul cu cea mai mare frecvență (separare după spații).
#dacă nu există cuvinte, mesaj corespunzător.
#Exemplu: "Cel mai frecvent cuvânt este 'ana' (apariții: 3)."
def cel_mai_frecvent_cuvant(text: str) -> str:
    text = text.strip()
    if not text:
        return "Nu există cuvinte în text."

    cuvinte = text.split()
    frecvente = {}
    for cuv in cuvinte:
        cuv = cuv.lower()
        frecvente[cuv] = frecvente.get(cuv, 0) + 1
    cuvant_maxim = max(frecvente, key=frecvente.get)
    aparitii = frecvente[cuvant_maxim]

    return f"Cel mai frecvent cuvânt este '{cuvant_maxim}' (apariții: {aparitii})."
def numar_unic(lista):
    numar_unic_gasit= "Eroare"
    for i in range(len(lista)):
        numar=lista[i]
        contor=0
        for j in range(len(lista)):
            if lista[j]==numar:
                contor+=1
        if contor==1:
            numar_unic_gasit=lista[i]
    return str(numar_unic_gasit)


def medie_ponderata(valori: list[float], ponderi: list[float]) -> str:
    if len(valori) != len(ponderi) or len(valori)==0:
        return "Error : Listele trebuie să aibă aceeași lungime, să nu fie goale"
    suma_poderi = sum(ponderi)
    if suma_poderi <= 0:
        return "Error : Suma ponderilor trebuie sa nu fie 0"
    media = sum(v * p for v, p in zip(valori,ponderi)) / suma_poderi
    return f"Medie ponderi: {media:.1f}"
print(medie_ponderata([9,8,10], [2,1,3]))
print(medie_ponderata([7, 8], [0, 0]))
print(medie_ponderata([7], []))

def filtreaza_pare(lista: list[int]) -> str:
    pare = []
    for numar in lista:
        if numar % 2 == 0:
            pare.append(numar)
    if len(pare) == 0:
        return "Nu exista numere pare,exemple de numere pare:2,4"
    text = "Numere pare: "
    for i in range(len(pare)):
        text += str(pare[i])
        if i < len(pare) - 1:
            text += ", "
    return text
#lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]