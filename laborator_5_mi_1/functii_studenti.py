#8. medie_ponderata(valori: list[float], ponderi: list[float]) -> str

#Calculează media ponderată.
#Listele trebuie să aibă aceeași lungime, să nu fie goale, iar suma ponderilor > 0.
#În caz contrar, mesaj de eroare.
#Exemplu: "Media ponderată este 8.5."
list=[7,9,10]
ponderi=[1,2,3]
def medie_ponderata(valori:list[float], ponderi:list[float]) ->str:
    if len(valori) != len(ponderi):
        return "Eroare"
    if not valori or not ponderi:
        return "Eroare"
    if sum(ponderi) == 0:
        return "Eroare"
    medie = sum(valori[i] * ponderi[i] for i in range(len(valori))) / sum(ponderi)
    return f"Media ponderata este {medie}"
print(medie_ponderata([list],[ponderi]))
