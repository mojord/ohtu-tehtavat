from tuomari import Tuomari
#from siirtaja import Siirtaja

class KPSPelaajaVsPelaaja:
    

    def siirra1(self):
        ekan_siirto = input("Ensimmäisen pelaajan siirto: ")

        return ekan_siirto

    def siirra2(self):
        tokan_siirto = input("Toisen pelaajan siirto: ")

        return tokan_siirto

#        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
#            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
#            print(tuomari)

#            ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
#            tokan_siirto = input("Toisen pelaajan siirto: ")

#        print("Kiitos!")
#        print(tuomari)

#    def _onko_ok_siirto(self, siirto):
#        return siirto == "k" or siirto == "p" or siirto == "s"
