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

