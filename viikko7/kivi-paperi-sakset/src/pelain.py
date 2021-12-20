from tuomari import Tuomari
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
#from siirtaja import Siirtaja

class Pelain:

    def __init__(self, Peli):
#        self.siirtaja = siirtaja()
        self.tuomari = Tuomari()
        self.peli = Peli()

    def pelaa(self):

        ekan_siirto = self.peli.siirra1()
        tokan_siirto = self.peli.siirra2()


        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            self.tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(self.tuomari)

            ekan_siirto = self.peli.siirra1()
            tokan_siirto = self.peli.siirra2()


        print("Kiitos!")
        print(self.tuomari)


    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
