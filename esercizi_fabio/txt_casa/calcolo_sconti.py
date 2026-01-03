totale_spesa = float(input("Inserire importo totale della spesa: "))
ha_tessera = input(" Hai la tessera? (si/no): ").lower()
giorno = int(input("Che giorno è oggi? (1-7, dove 2=martedi): "))
sconto_percentuale = 0
if totale_spesa > 100: 
   sconto_percentuale += 10
if ha_tessera == "si": 
    sconto_percentuale += 5 
if giorno == 2:
   sconto_percentuale += 3
importo_sconto = (totale_spesa * sconto_percentuale) / 100
totale_finale = totale_spesa - importo_sconto
print("-" * 30)
print(f"Totale originale: {totale_spesa:.2f}€")
print(f"Percentuale sconto: {sconto_percentuale}%")
print(f"Risparmio: {importo_sconto:.2f}€")
print(f"TOTALE FINALE: {totale_finale:.2f}€")
print("-" * 30)
