voto1 = float(input("Inserisci il primo voto (0-10): "))
voto2 = float(input("Inserisci il secodno vodo (0-10): "))
voto3 = float(input("inserisci il terzo voto (0-10): "))
media = (voto1 + voto2 + voto3) / 3
if media >= 9:
   giudizio = "Eccellente "
elif media >= 7:
   giudizio = "Buono "
elif media >= 6:
   giudizio = "sufficiente "
else:
   giudizio = "insufficiente"
if voto1 >= 8 and voto2 >= 8 and voto3 >= 8:
   giudizio += "con Lode"
print(f"\nLa tua media è {media:.2f}")
print(f"Giudizio finale {giudizio}")
