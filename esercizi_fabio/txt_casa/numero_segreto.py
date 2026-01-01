numero_segreto = 7
tentativi = 0

while True:
    tentativo = int(input("Indovina il numero (1-10):"))
    tentativi += 1

    if tentativo == numero_segreto:
 
     if tentativo == numero_segreto:
        if tentativi == 1:
           print("Bravo! Hai azzeccato al primo colpo!")
        else:
           print(f"Finalmente! Hai indovinato al tentetivo numero {tentativi}!")
        break
    elif tentativo < numero_segreto:
        print("Troppo basso! Riprova!")
    else:
        print("Troppo alto! Riprova!")
