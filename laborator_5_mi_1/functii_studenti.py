def cmmmc(a: int, b: int) -> str:
    if a==0 or b==0:
        return "Eroare: Numerele trebuie sa fie nenule"
    def cmmdc(x,y):
        while y!=0:
            x,y=y ,x%y
        return x
    cmmmc_val= abs(a*b) // cmmdc(a,b)
    return f"cmmmc({a},{b})={cmmmc_val}"
