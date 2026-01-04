import random
import string
print("-" * 30)
print(" GENERATORE DI PASSWORD PRO ")
print("-" * 30)
lunghezza = int(input("Quanto deve essere lunga la password? "))
usa_maiuscole = input("Vuoi includere maiuscole? (si/no): ").lower() == "si"
usa_numeri = input("Vuoi includere numeri? (si/no): ").lower() == "si"
usa_simboli = input("Vuoi includere simboli? (si/no): ").lower() == "si"
caratteri_disponibili = string.ascii_lowercase
if usa_maiuscole:
    caratteri_disponibili += string.ascii_uppercase
if usa_numeri:
    caratteri_disponibili += string.digits
if usa_simboli:
    caratteri_disponibili += string.punctuation
password = "".join(random.choice(caratteri_disponibili) for _ in range(lunghezza))
print("-" * 30)
print(f"La tua nuova password è: {password}")
print("-" * 30)