def cmmdc(a, b):
    if a == 0 and b == 0:
        return "Eroare:CMMDC(0, 0) nu este definit."
    while b!= 0:
        a, b = b, a % b
    return abs(a)
print(f"CMMDC(12, 18) = {cmmdc(12, 18)}")
print( cmmdc(0, 0,))

