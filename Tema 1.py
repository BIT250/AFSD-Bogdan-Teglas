# 1. Declaram un sir (textul poate fi copiat de pe un site de siruri)
text = """Ministrul Sănătăţii a anunţat astăzi că începând de luna viitoare va fi lansată o campanie naţională de vaccinare împotriva gripei sezoniere. Obiectivul este de a reduce semnificativ numărul de spitalizări în rândul persoanelor vârstnice şi cu afecţiuni cronice. De asemenea, se urmăreşte creşterea gradului de acoperire vaccinală cu 20 % faţă de sezonul precedent."""

# 2. Împărțim textul în două părți egale
lungime = len(text)
jumatate = lungime // 2     # împărțire întreagă
prima_parte = text[:jumatate]
a_doua_parte = text[jumatate:]

# 3. Operații pe prima parte.
prima_parte = prima_parte.upper()       #toate literele majuscule
prima_parte = prima_parte.strip()       #eliminăm spaţiile de la începutul şi finalul şirului.

# 4. Operații pe a doua parte.
a_doua_parte = a_doua_parte[::-1]           #inversăm ordinea caracterelor
a_doua_parte = a_doua_parte.capitalize()    #prima literă devine majusculă

# elimină semnele de punctuație.
for semn in [".", ",", ":", ";", "!", "?"]:
    a_doua_parte = a_doua_parte.replace(semn, "")

# 5. Combinăm cele două părți
rezultat = prima_parte + " " + a_doua_parte

# 6. Afișăm rezultatul final
print("Rezultatul final este:\n")
print(rezultat)