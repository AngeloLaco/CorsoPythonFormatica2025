import random

nome = input("Hei tu, come ti chiami? ")
risposta = input(f"Ciao {nome}, vuoi fare un gioco con me? (si/no): ").lower()

if risposta == "si":
    print("Fantastico! Ho scelto un numero tra 1 e 100. Azzeccalo!")
    segreto = random.randint(1, 100)
    while True:
        tentativo = int(input("Spara un numero!: "))
        if tentativo < segreto:
            print("Troppo basso!")
        elif tentativo > segreto:
            print("Troppo alto!")
        else:
            print(f"Beccato {nome}, la terra è salva!")
            break
else:
    print(f"Peccato {nome}! Non sai che ti perdi.")
