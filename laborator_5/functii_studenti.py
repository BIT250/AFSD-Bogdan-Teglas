def suma_cifrelor(n):
    suma=0
    while(n):
        uc=n%10
        n=n//10
        suma += uc
    return f"{suma}"

def cmmdc(a,b):
    if a==b==0:
        return "Eroare"
    while(b!=0):
        rest=a%b
        a=b
        b=rest
    return f"{a}"

def cmmmc(a,b):
    if(a==0 or b==0): return "Eroare"
    if(a<=b):
        multiplu = b
    else: multiplu = a
    while True:
        if(multiplu%a==0 and multiplu%b==0):
            return f"{multiplu}"
        else: multiplu+=1

def numar_divizori(n):
    if n<=0: return "Eroare"
    numar_divizori=0
    for i in range(1, n+1):
        if (n%i==0):
            numar_divizori+=1
    return f"{numar_divizori}"

def lista_prime_pana_la(n):
    lista=[]
    for i in range(2, n+1):
        nrdiv = 0
        for j in range(1, i+1):
            if (i%j==0):
                nrdiv += 1
        if nrdiv==2:
            lista.append(i)
    if (lista==[]):
        return "Nu exista numere prime"
    rezultat = ", ".join(map(str, lista))
    return f"{rezultat}"

def filtreaza_pare(lista):
    lista2=[]
    for i in lista:
        if i%2==0:
            lista2.append(i)
    if (lista2==[]):
        return "Nu exista numere pare"
    rezultat= ", ". join(map(str,lista2))
    return f"{rezultat}"
def produs_scalar(v1: list[float],v2: list[float]):
    suma=0
    if len(v1)!=len(v2):
        return ("Lungimile difera, produsul scalar nu se poate calcula")
    for i in range(len(v1)):
        suma = suma + (v1[i]*v2[i])
    return f"{suma}"

def medie_ponderata(valori:list[float], ponderi:list[float]):
    if(len(valori)!=len(ponderi) or valori==[] or ponderi==[]):
        return "Eroare"
    sumavalori=0
    if(sum(ponderi)<=0):
        return "Eroare"
    for i in range(len(valori)):
        sumavalori=sumavalori + (valori[i]*ponderi[i])
    sumaponderi=sum(ponderi)
    sumafinala=sumavalori/sumaponderi
    return f"{sumafinala}"

def rotire_dreapta(lista: list[int], k: int):
    if len(lista) == 0:
        return "Lista este goală"
    n = len(lista)
    k = k % n
    lista_noua = lista[n-k:] + lista[:n-k]
    rezultat = ", ".join(map(str, lista_noua))
    return f"{rezultat}"

def interclaseaza(l1: list[int], l2: list[int]):
    rezultat_lista = []
    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            rezultat_lista.append(l1[i])
            i=i+1
        else:
            rezultat_lista.append(l2[j])
            j=j+1
    while i < len(l1):
        rezultat_lista.append(l1[i])
        i=i+1
    while j < len(l2):
        rezultat_lista.append(l2[j])
        j=j+1
    text = ", ".join(map(str, rezultat_lista))
    return f"{text}"

def elimina_duplicate(lista: list[int]):
    lista_noua=[]
    for x in lista:
        if x not in lista_noua:
            lista_noua.append(x)
    text=", ".join(map(str, lista_noua))
    return f"{text}"

def frecventa_litere(text: str):
    frecventa={}
    for litera in text:
        if litera!=" ":
            if litera in frecventa:
                frecventa[litera]=frecventa[litera]+1
            else:
                frecventa[litera]=1
    if not frecventa:
        return "Nu există caractere"
    rezultat=""
    for cheie in frecventa:
        rezultat=rezultat+f"'{cheie}': {frecventa[cheie]}, "
    return rezultat[:-2]

def cel_mai_frecvent_cuvant(text: str):
    cuvinte=text.split()
    if not cuvinte:
        return "Eroare"
    frecventa={}
    for c in cuvinte:
        if c in frecventa:
            frecventa[c]=frecventa[c]+1
        else:
            frecventa[c]=1
    max_ap=0
    cuv_final=""
    for c in frecventa:
        if frecventa[c]>max_ap:
            max_ap=frecventa[c]
            cuv_final=c
    return f"Cel mai frecvent cuvânt este '{cuv_final}' (apariții: {max_ap})."

def este_isograma(text: str):
    text_mic=text.lower().replace(" ", "")
    vazute=[]
    for litera in text_mic:
        if litera in vazute:
            return f"'{text}' NU este isogramă."
        vazute.append(litera)
    return f"'{text}' este isogramă."

def numere_distincte(lista: list[int]):
    if not lista:
        return "Lista este goală."
    vazute=[]
    for x in lista:
        if x in vazute:
            return "Lista conține elemente care se repetă."
        vazute.append(x)
    return "Toate numerele din listă sunt distincte."

def timp_in_format(secunde: int):
    if secunde<0:
        return "Eroare: numărul de secunde trebuie să fie nenegativ."
    ore=int(secunde/3600)
    rest=secunde%3600
    minute=int(rest/60)
    sec=rest%60
    h=str(ore) if ore>=10 else "0"+str(ore)
    m=str(minute) if minute>=10 else "0"+str(minute)
    s=str(sec) if sec>=10 else "0"+str(sec)
    return f"{secunde} secunde înseamnă {h}:{m}:{s}."

def parola_valida(parola: str):
    if len(parola)<8:
        return "Parola este prea scurtă"
    are_litera=False
    are_cifra=False
    for c in parola:
        if c.isalpha():
            are_litera=True
        if c.isdigit():
            are_cifra=True
    if are_litera and are_cifra:
        return "Parola este validă"
    return "Invalidă: trebuie să conțină litere și cifre"

def in_binar(n: int):
    if n<0:
        return "Număr negativ"
    if n==0:
        return "Reprezentarea în baza 2 a lui 0 este 0"
    copie_n=n
    binar=""
    while n>0:
        binar=str(n%2)+binar
        n=int(n/2)
    return f"Reprezentarea în baza 2 a lui {copie_n} este {binar}"

def numar_unic(lista: list[int]):
    for x in lista:
        count=0
        for y in lista:
            if x==y:
                count=count+1
        if count==1:
            return f"{x}"
    return "Eroare, nicio valoare unică"

def sunt_anagrame(a: str, b: str):
    s1=sorted(a.lower().replace(" ", ""))
    s2=sorted(b.lower().replace(" ", ""))
    if s1==s2:
        return f"'{a}' și '{b}' sunt anagrame"
    return f"'{a}' și '{b}' nu sunt anagrame"

