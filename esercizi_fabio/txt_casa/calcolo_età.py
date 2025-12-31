anno_corrente = 2024
anno_nascita = int(input("In che anno sei nato/a? "))
mese_nascita = input("In che mese sei nato/a? ")
compiuti = input("Li hai già compiuti quest anno? (si/no) ").lower()
eta = anno_corrente - anno_nascita
if compiuti == "no":
    eta -= 1
print(f"Ricapitoliamo! Sei nato/a a {mese_nascita} del {anno_nascita}, oggi hai {eta} anni")
