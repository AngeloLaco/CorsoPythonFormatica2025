import random
lanci = 1000
somme_sette = 0
for _ in range(lanci):
     dado1 = random.randint(1, 6)
     dado2 = random.randint(1, 6)
     if dado1 + dado2 == 7:
         somme_sette += 1
percentuale = (somme_sette / lanci) * 100
print(f"Simulazione di {lanci} lanci completata.") 
print(f"Il numero 7 è uscito {somme_sette} volte.")
print(f"Percentuale: {percentuale}%")