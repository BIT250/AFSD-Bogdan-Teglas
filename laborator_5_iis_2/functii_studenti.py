def in_binar(n: int) -> str:
    res = ''  # binary result
    while n > 0:
        res = str(n & 1) + res
        n >>= 1
    return res

print(in_binar(145021))