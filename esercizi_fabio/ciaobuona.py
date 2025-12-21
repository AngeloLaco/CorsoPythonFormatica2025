import random
from datetime import datetime

# 1. Definizione di una funzione
def calcola_anno_nascita(eta):
    anno_corrente = datetime.now().year
    return anno_corrente - eta

# 2. Liste e Variabili
saluti = ["Ciao", "Salve", "Benvenuto", "Ehilà"]
emoji = ["🚀", "💻", "🐍", "🔥"]

# 3. Inizio del programma principale
print("--- TEST CONNESSIONE GITHUB ---")

# Scelgo un saluto e una emoji a caso dalla lista
saluto_random = random.choice(saluti)
emoji_random = random.choice(emoji)

print(f"{saluto_random}! Questo script Python funziona correttamente {emoji_random}")

# 4. Input dell'utente (Interazione)
try:
    nome = input("\nCome ti chiami? ")
    eta_str = input("Quanti anni hai? ")
    
    # Converto la stringa in numero intero
    eta = int(eta_str)

    # 5. Logica condizionale (If/Else)
    if eta < 18:
        print(f"Sei giovanissimo, {nome}!")
    else:
        print(f"Grande {nome}, sei un adulto!")

    # Richiamo la funzione creata sopra
    anno_nascita = calcola_anno_nascita(eta)
    print(f"Probabilmente sei nato nel {anno_nascita}.")

except ValueError:
    # Gestione errori se l'utente scrive lettere al posto dei numeri
    print("Attenzione: devi inserire un numero valido per l'età!")

print("\n--- FINE DEL TEST ---")