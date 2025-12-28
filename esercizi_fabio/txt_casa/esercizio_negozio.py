prezzo_mele_kg=2.50
prezzo_banane_kg=1.80
prezzo_arance_kg=3.00
prezzo_mele_pz=0.50
prezzo_banane_pz=0.30
prezzo_arance_pz=0.60
iva=22/100
while True:
    print("Benvenuto nel negozio di frutta!")   
    tipo_acquisto=input("Vuoi acquistare la frutta al kg, a pezzi o grammi? (kg/pezzi/grammi): ")
    if tipo_acquisto=="kg":
        qta_mele=float(input("Inserisci la quantità di mele in kg: "))
        qta_banane=float(input("Inserisci la quantità di banane in kg: "))
        qta_arance=float(input("Inserisci la quantità di arance in kg: "))
        totale_prezzo=(prezzo_mele_kg * qta_mele) + (prezzo_banane_kg * qta_banane) + (prezzo_arance_kg * qta_arance)
    elif tipo_acquisto=="pezzi":
        qta_mele=int(input("Inserisci la quantità di mele in pezzi: "))
        qta_banane=int(input("Inserisci la quantità di banane in pezzi: "))
        qta_arance=int(input("Inserisci la quantità di arance in pezzi: "))
        totale_prezzo=(prezzo_mele_pz * qta_mele) + (prezzo_banane_pz * qta_banane) + (prezzo_arance_pz * qta_arance)
    elif tipo_acquisto== "grammi":
        qta_mele_grammi=float(input("Inserisci la quantità di mele in grammi: "))
        qta_banane_grammi=float(input("Inserisci la quantità di banane in grammi: "))
        qta_arance_grammi=float(input("Inserisci la quantità di arance in grammi: "))
        qta_mele=qta_mele_grammi/1000   
        qta_banane=qta_banane_grammi/1000
        qta_arance=qta_arance_grammi/1000
        totale_prezzo=(prezzo_mele_kg * qta_mele) + (prezzo_banane_kg * qta_banane) + (prezzo_arance_kg * qta_arance)

    else:
        print("Tipo di acquisto non valido.")
        continue
    totale_con_iva=totale_prezzo + (totale_prezzo * iva)
    print("Il totale da pagare, IVA inclusa, è: €", round(totale_con_iva,2))
    print("il totale senza IVA è: €", round(totale_prezzo,2))
    print("l'IVA è di: €", round(totale_prezzo * iva,2))
    exit()
    
    

                                                        