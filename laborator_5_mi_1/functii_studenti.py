text = input("Introdu textul: ")

frecvente = {}

for caracter in text:
    if caracter != " ":
        if caracter in frecvente:
            frecvente[caracter] = frecvente[caracter] + 1
        else:
            frecvente[caracter] = 1

if len(frecvente) == 0:
    print("Nu există caractere (fără spații) în șir.")
else:
    for c in frecvente:
        print("'", c, "':", frecvente[c])
