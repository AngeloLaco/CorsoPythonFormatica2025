print("-" * 30)
print("    VENDITA BIGLIETTI")
print("-" * 30)
evento = input("Scegliere il tipo di evento (concerto/teatro/cinema): ").lower()
eta = int(input("Età del cliente: "))
giorno = input("Giorno della sewttimana: ").lower()
quantita = int(input("Numero di biglietti: "))
prezzi_base = {
    "concerto": 50,
    "teatro": 30,
    "cinema": 10
}
if evento not in prezzi_base:
   print("ERRORE: Evento non disponibile.")
else:
   prezzo_unitario = prezzi_base[evento]
   if eta < 12:
      prezzo_unitario *= 0.5
      print("-Sconto bambini applicato")
   elif eta > 65:
      prezzo_unitario *= 0.7
      print("-Sconto senior applicato")
   if evento == "cinema" and giorno == "mercoledi":
       prezzo_unitario -= 2
       print("-Sconto Mercoledi Cinema (-2€)")
   totale = prezzo_unitario * quantita
   if quantita >= 5:
       totale *= 0.9
       print("-Sconto Gruppo (-10%) applicato")
   print("-" * 30)
   print(f"Prezzo a biglietto: {prezzo_unitario:.2f}€")
   print(f"Quantità: {quantita}")
   print(f"TOTALE DA PAGARE: {totale:.2f}€")
   print("-" * 30)
