elevi = ["Ana", "Bogdan", "Carmen", "Darius", "Elena"]
note  = [9,       7,        10,       4,        8]

elev_nou        = "Felix"
nota_elev_nou   = 6
elev_de_sters   = "Darius"

interogari_nume = ["Ana", "Mara", "Elena", "stop"]

absente = [1, 0, 2, 3, 0]


#Listează elevii cu notele lor
for i in range(len(elevi)):
    print(f"{elevi[i]} are nota {note[i]}")

len(elevi) #Află câți elevi sunt în listă (aici sunt 5)
range(len(elevi))  #Accesează pozițiile pe care se află elementele din șir

for i in #bucla ea pe rând valorile lui i (0 - 4)

elevi[i] #ia numele de pe poziția i
nota[i]  #ia nota de pe poziția i

print(f" ") #f-string (format string): inserează valorile direct în text

#A2. Nota maximă și minimă + numele elevilor corespunzători.
max(note) #Caută cea mai mare notă din listă
min(note) #Caută cea mai mică notă din listă

