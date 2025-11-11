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
#print(filtreaza_pare(lista))