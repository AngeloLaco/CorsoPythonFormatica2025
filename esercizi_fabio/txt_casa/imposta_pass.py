 input("Inserisci una nuova password: ")
lunghezza_ok = len(password) >= 8
contiene_numero = any(chair.isdigit() for char in password)
non_banale = password not in ["password", "12345678"]
if lunghezza_ok and contiene_numero and non_banale:
   print("Password sicura! Registrazione completata!")
else:
    print("Password NON sicura. Controlla i criteri:")
    if not lunghezza_ok:
        print("Deve contenere almeno 8 caratteri:")
    if not contiene_numero:
        print("Deve contenere almeno un numero:")
    if not non_banale:
        print("Non puo essere una password troppo comune:")
