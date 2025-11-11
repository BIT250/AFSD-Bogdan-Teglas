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

