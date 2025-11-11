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