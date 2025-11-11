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