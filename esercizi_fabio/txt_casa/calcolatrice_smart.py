import math
while True:
    print("\n" + "="*30)
    print("       CALCOLATRICE SMART")
    print("="*30)
    print("1. Addizione")
    print("2. Sottrazione")
    print("3. Moltiplicazione")
    print("4. Divisione")
    print("5. Potenza")
    print("6. Radicre Quadrata")
    print("0. Esci")
    print("-"*30)
    scelta = input("Scdegli un operazione (0-6): ")
    if scelta == "0":
       print("Chiusura calcolatrice. Ciao!")
       break
    if scelta in ["1", "2", "3", "4", "5"]:
       n1 = float(input("Inserire il primo numero: "))
       n2 = float(input("Inserire il secondo numero: "))
       if scelta == "1":
          print(f"Risultato:  {n1 + n2}")
       elif scelta == "2":
          print(f"Risultato: {n1 - n2}")
       elif scelta == "3":
          print(f"Risultato: {n1 * n2}")
       elif scelta == "4":
            if n2 != 0:
               print(f"Risultato: {n1 / n2}")
            else:
               print("Errore: impossibile dividere per zero!")
    elif scelta == "5":
           print(f"Risultato: {n1 ** n2}")
    elif scelta =="6":
       n = float(input("Inserire il numero per la radice: "))
       if n >= 0:
          print(f"Risultato: {math.sqrt(n)}")
       else:
          print("Errore: Non si puo fare la radeice di un numero negativo!")
    else :

      print("Operazione non valida!")
