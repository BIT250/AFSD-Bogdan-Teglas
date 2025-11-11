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

print(numar_unic([6, 7, 8, 6, 7]))