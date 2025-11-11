# main.py
# Aplicatie Tkinter care apeleaza functiile din functii_studenti.py
# In acelasi folder trebuie sa existe fisierul functii_studenti.py
# cu cele 20 de functii care returneaza string.

import tkinter as tk
from tkinter import ttk, messagebox
import functii_studenti as fs


def parse_int_list(text: str):
    # Lista de int din valori separate prin spatiu sau virgula
    text = text.strip()
    if not text:
        return []
    sep = ',' if ',' in text else ' '
    parts = [p.strip() for p in text.split(sep) if p.strip() != ""]
    return [int(p) for p in parts]


def parse_float_list(text: str):
    # Lista de float din valori separate prin spatiu sau virgula
    text = text.strip()
    if not text:
        return []
    sep = ',' if ',' in text else ' '
    parts = [p.strip() for p in text.split(sep) if p.strip() != ""]
    return [float(p) for p in parts]


def parse_matrix(text: str):
    """
    Matrice de int:
    - randurile separate cu ';'
    - elementele pe rand separate prin spatiu sau virgula
    Ex: "1 2 3;4 5 6;7 8 9"
    """
    text = text.strip()
    if not text:
        return []
    rows = [r.strip() for r in text.split(';') if r.strip() != ""]
    matrix = []
    for r in rows:
        # folosim parse_int_list pe fiecare rand
        sep = ',' if ',' in r else ' '
        parts = [p.strip() for p in r.split(sep) if p.strip() != ""]
        matrix.append([int(p) for p in parts])
    return matrix


def ruleaza():
    raw = entry_input.get()
    func_name = combo_functii.get().strip()

    if not func_name:
        messagebox.showerror("Eroare", "Selectați o funcție din listă.")
        return

    try:
        # match-case disponibil din Python 3.10
        match func_name:
            case "suma_cifrelor":
                n = int(raw)
                rezultat = fs.suma_cifrelor(n)

            case "cmmdc":
                # format input: "a,b" sau "a b"
                sep = ',' if ',' in raw else ' '
                a_str, b_str = [x.strip() for x in raw.split(sep)]
                a, b = int(a_str), int(b_str)
                rezultat = fs.cmmdc(a, b)

            case "cmmmc":
                # format input: "a,b" sau "a b"
                sep = ',' if ',' in raw else ' '
                a_str, b_str = [x.strip() for x in raw.split(sep)]
                a, b = int(a_str), int(b_str)
                rezultat = fs.cmmmc(a, b)

            case "numar_divizori":
                n = int(raw)
                rezultat = fs.numar_divizori(n)

            case "lista_prime_pana_la":
                n = int(raw)
                rezultat = fs.lista_prime_pana_la(n)

            case "filtreaza_pare":
                # ex: "1 2 3 4" sau "1,2,3,4"
                lista = parse_int_list(raw)
                rezultat = fs.filtreaza_pare(lista)

            case "produs_scalar":
                # format: "1 2 3 ; 4 5 6" sau cu virgule
                if ';' not in raw:
                    raise ValueError("Folositi formatul: lista1 ; lista2")
                left, right = raw.split(';', 1)
                v1 = parse_float_list(left)
                v2 = parse_float_list(right)
                rezultat = fs.produs_scalar(v1, v2)

            case "medie_ponderata":
                # format: "valori ; ponderi"
                if ';' not in raw:
                    raise ValueError("Folositi formatul: valori ; ponderi")
                left, right = raw.split(';', 1)
                valori = parse_float_list(left)
                ponderi = parse_float_list(right)
                rezultat = fs.medie_ponderata(valori, ponderi)

            case "rotire_dreapta":
                # format: "lista ; k"
                if ';' not in raw:
                    raise ValueError("Folositi formatul: lista ; k")
                left, right = raw.split(';', 1)
                lista = parse_int_list(left)
                k = int(right.strip())
                rezultat = fs.rotire_dreapta(lista, k)

            case "interclaseaza":
                # format: "lista1 ; lista2"
                if ';' not in raw:
                    raise ValueError("Folositi formatul: lista1 ; lista2")
                left, right = raw.split(';', 1)
                l1 = parse_int_list(left)
                l2 = parse_int_list(right)
                rezultat = fs.interclaseaza(l1, l2)

            case "elimina_duplicate":
                # format: "1 2 2 3" etc.
                lista = parse_int_list(raw)
                rezultat = fs.elimina_duplicate(lista)

            case "frecventa_litere":
                # orice text
                rezultat = fs.frecventa_litere(raw)

            case "cel_mai_frecvent_cuvant":
                rezultat = fs.cel_mai_frecvent_cuvant(raw)

            case "este_isograma":
                rezultat = fs.este_isograma(raw)

            case "timp_in_format":
                # format matrice: "1 2 3;4 5 6;7 8 9"
                matrice = int(raw)
                rezultat = fs.timp_in_format(matrice)

            case "numere_distincte":
                matrice = parse_matrix(raw)
                rezultat = fs.numere_distincte(matrice)

            case "parola_valida":
                rezultat = fs.parola_valida(raw)

            case "in_binar":
                n = int(raw)
                rezultat = fs.in_binar(n)

            case "numar_unic":
                lista = parse_int_list(raw)
                rezultat = fs.numar_unic(lista)

            case "sunt_anagrame":
                # format: "text1 ; text2"
                if ';' not in raw:
                    raise ValueError("Folositi formatul: text1 ; text2")
                a, b = raw.split(';', 1)
                rezultat = fs.sunt_anagrame(a.strip(), b.strip())

            case _:
                rezultat = "Funcție necunoscută."


        label_rezultat.config(text=rezultat)

    except ValueError as e:
        messagebox.showerror("Eroare de conversie", f"Verificați formatul datelor de intrare.\n{e}")
    except Exception as e:
        messagebox.showerror("Eroare", f"A apărut o eroare la rularea funcției.\n{e}")


# ================== UI ==================

root = tk.Tk()
root.title("Apelare functii - laborator")

# Combobox cu numele functiilor EXACT ca in functii_studenti.py
tk.Label(root, text="Alege funcția:").pack(anchor="w", padx=5, pady=(5, 0))

combo_functii = ttk.Combobox(
    root,
    values=[
        "suma_cifrelor",
        "cmmdc",
        "cmmmc",
        "numar_divizori",
        "lista_prime_pana_la",
        "filtreaza_pare",
        "produs_scalar",
        "medie_ponderata",
        "rotire_dreapta",
        "interclaseaza",
        "elimina_duplicate",
        "frecventa_litere",
        "cel_mai_frecvent_cuvant",
        "este_isograma",
        "numere_distincte",
        "timp_in_format",
        "parola_valida",
        "in_binar",
        "numar_unic",
        "sunt_anagrame",
    ],
    state="readonly",
    width=30
)
combo_functii.pack(fill="x", padx=5, pady=5)

# Camp input
tk.Label(root, text="Input (format în funcție de funcție):").pack(anchor="w", padx=5)
entry_input = tk.Entry(root, width=60)
entry_input.pack(fill="x", padx=5, pady=5)

# Buton ruleaza
btn_ruleaza = tk.Button(root, text="Rulează funcția", command=ruleaza)
btn_ruleaza.pack(pady=5)

# Label rezultat
tk.Label(root, text="Rezultat:").pack(anchor="w", padx=5)
label_rezultat = tk.Label(root, text="", wraplength=500, justify="left")
label_rezultat.pack(fill="x", padx=5, pady=(0, 10))

root.mainloop()
