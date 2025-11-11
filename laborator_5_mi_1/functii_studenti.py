def suma_cifrelor(n: int) -> str:
    if n < 0 or not isinstance(n, int):
        return "Eroare: numarul nu este un numar intreg pozitiv!"

    sn = str(n)
    suma = 0

    for cifra in sn:
        suma = suma + int(cifra)
    return f"Suma cifrelor lui {n} este {suma}."
