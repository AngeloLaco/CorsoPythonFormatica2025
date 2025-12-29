import math
gradi = float(input('Inserisci l\'angolo in gradi: '))
radianti = math.radians(gradi)
print(f'Radianti: {radianti}')
print(f'Seno: {round(math.sin(radianti), 2)}')
print(f'Coseno: {round(math.cos(radianti), 2)}')