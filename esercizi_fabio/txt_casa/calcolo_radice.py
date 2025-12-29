import math
numero = float(input("inserisci un numero per calcolare la radice quadrata: "))
if numero < 0:
    print("impossibile calcolare la radice quadrata di un numero negativo") 
else:
    radice_quadrata = math.sqrt(numero)
    print("la radice quadrata di", numero, "è", radice_quadrata)    
    