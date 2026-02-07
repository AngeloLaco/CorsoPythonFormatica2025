from abc import ABC, abstractmethod

class Eroe(ABC):
    def __init__(self, nome, livello, punti_vita):
        self.nome = nome
        self.livello = livello
        self.punti_vita = punti_vita

    @abstractmethod
    def attacco(self):
        pass 
    def difesa(self):
        return f"{self.nome} si difende con {self.punti_vita} punti vita."
    def contro_attacco(self):
        return f"{self.nome} contro-attacca con forza!"   

    def statistiche(self):
        print(f"---{self.nome}(Livello: {self.livello})---")
        print(f"PV: {self.punti_vita}")
    
class Guerriero(Eroe):
    def __init__(self, nome, livello, punti_vita, scudo):
        super().__init__(nome, livello, punti_vita)
        self.scudo = scudo

    def attacco(self):
        print(f"{self.nome} attacca con la spada!")

    def difesa(self):
        print(f"{self.nome} si difende con lo scudo {self.scudo} e {self.punti_vita} punti vita.")

    def contro_attacco(self):
        print(f"{self.nome} contro-attacca con la forza del guerriero!")

    def grido_battaglia(self):
        self.punti_vita +=20
        print(f"{self.nome} grida: 'Per la gloria!'")

class Mago(Eroe):
    def __init__(self, nome, livello, punti_vita, meditazione):
        super().__init__(nome, livello, punti_vita)
        self.meditazione = meditazione

    def attacco(self):
        print(f"{self.nome} lancia un incantesimo!")

    def difesa(self):
        print(f"{self.nome} si difende con la magia e {self.punti_vita} punti vita.")

    def contro_attacco(self):
        print(f"{self.nome} contro-attacca con un potente incantesimo!")

    def rigenerazione_meditazione(self):
        self.meditazione += 10
        print(f"{self.nome} rigenera meditazione. Meditazione attuale: {self.meditazione}")

class Supremo(Eroe):
     def __init__(self, nome, livello, punti_vita, potere_supremo):
            super().__init__(nome, livello, punti_vita)
            self.potere_supremo = potere_supremo

     def attacco(self):
            print(f"{self.nome} utilizza il potere supremo: {self.potere_supremo}!")

     def difesa(self):
            print(f"{self.nome} si difende con il potere supremo {self.potere_supremo} e {self.punti_vita} punti vita.")

     def contro_attacco(self):
            print(f"{self.nome} contro-attacca con il potere supremo {self.potere_supremo}!")

     def potere_finale(self):
            print(f"{self.nome} scatena il potere finale: {self.potere_supremo * 2}!")

# Esempio di utilizzo
party = [
    Guerriero("Nino",15, 150, 50),
    Mago("Pino", 12, 80, 50),
    Supremo("Tino", 50, 200, 150)
]

print("=== INIZIO BATTAGLIA ===\n")

for eroe in party:
    eroe.statistiche()
    eroe.attacco()
    eroe.difesa()
    eroe.contro_attacco()

    if isinstance(eroe, Guerriero):
        eroe.grido_battaglia()
    elif isinstance(eroe, Mago):
        eroe.rigenerazione_meditazione()
    elif isinstance(eroe, Supremo):
        eroe.potere_finale()
    print("-" * 25)
    