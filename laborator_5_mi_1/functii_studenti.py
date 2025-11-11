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

