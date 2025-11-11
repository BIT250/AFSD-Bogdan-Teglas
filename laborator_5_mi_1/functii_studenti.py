def lista_prime_pana_la(n: int) -> str:
    if not isinstance(n, int) or n < 2:
        return "Eroare: introduceți un număr întreg mai mare sau egal cu 2."

    def este_prim(numar):
        if numar < 2:
            return False
        for i in range(2, int(numar ** 0.5) + 1):
            if numar % i == 0:
                return False
        return True
    prime = [str(i) for i in range(2, n + 1) if este_prim(i)]
    if prime:
        return f"Numere prime până la {n}: {', '.join(prime)}"
    else:
        return f"Nu există numere prime până la {n}."
print(lista_prime_pana_la(2))
print(lista_prime_pana_la(3))