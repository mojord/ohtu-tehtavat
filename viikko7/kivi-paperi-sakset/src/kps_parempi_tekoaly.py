from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu

EKA = 0

class KPSParempiTekoaly:
    def __init__(self):
        self.tekoaly = TekoalyParannettu(10)
    
    def siirra1(self):
        ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        EKA = ekan_siirto
        return ekan_siirto

    def siirra2(self):
        tokan_siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        self.tekoaly.aseta_siirto(EKA)
        return tokan_siirto