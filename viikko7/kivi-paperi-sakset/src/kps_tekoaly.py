from tuomari import Tuomari
from tekoaly import Tekoaly

EKA = 0

class KPSTekoaly:
    def __init__(self):
        self.tekoaly = Tekoaly()

    def siirra1(self):
        ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        EKA = ekan_siirto
        return ekan_siirto

    def siirra2(self):
        tokan_siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        self.tekoaly.aseta_siirto(EKA)
        return tokan_siirto