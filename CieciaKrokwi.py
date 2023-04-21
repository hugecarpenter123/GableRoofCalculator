import math
import os

class CieciaNaKrokwach():
    def __init__(self, arg):
        if 'kat_dachu' in arg.keys():
            self.kat_dachu = arg['kat_dachu']
            self.d = arg['d']
            self.h = self.h_oblicz()
        else:
            self.h = arg['h']
            self.d = arg['d']
            self.kat_dachu = 2 * round(math.degrees(math.atan((0.5 * self.d) / self.h)), 2)

        self.p = arg['p']
        self.krokiew_poza_dachem = self.oblicz_kpd()
        # self.krokiew_poza_dachem = arg['krokiew_poza_dachem']
        self.h_krokwi = arg['h_krokwi']
        self.kat_zaciecia = self.z_oblicz()
        self.d_k_w = round((0.5 * self.d) / math.sin(math.radians(0.5 * self.kat_dachu)), 2)
        self.d_k_x = self.x_oblicz()
        self.d_krokwi_calkowita = round(self.d_k_x + self.d_k_w + self.krokiew_poza_dachem, 2)
        self.depka = self.depka_oblicz()
        self.s_zaciecia = round(self.s_z_oblicz(), 2)

        if 'op' in arg.keys():
            self.op = arg['op']
            self.hp = round(self.hp_oblicz(), 2)
            self.d_k_mp = self.dkmp_oblicz() #długość na krokwi od murłaty do płatwy
            self.d_k_gp = self.dkgp_oblicz() #długość na krokwi od góry krokwi do płatwy
            self.opp = self.d - (2 * self.op) # odległość od płatwy do płatwy po zewnętrznych stronach

        if 'hj' in arg.keys():
            self.hj = arg['hj']
            self.d_j_x = self.djx_oblicz()
            self.d_j_w = self.djw_oblicz()
            self.d_j_c = round(self.d_j_w + (2 * self.d_j_x), 2)
            self.d_j_kk = self.djkk_oblicz()# rysowanie spodu jętki od końca krokwy

    def h_oblicz(self):
        h = 0.5 * ( self.d / math.tan(math.radians(self.kat_dachu * 0.5)) )
        return round(h, 2)

    def z_oblicz(self):
        z = (360 - 2 * self.kat_dachu) / 2
        return round(z, 2)

    def x_oblicz(self):
        if self.kat_dachu <= 90:
            x = self.h_krokwi / math.tan(math.radians(0.5 * self.kat_dachu))
        else:
            x = self.h_krokwi / math.sin(math.radians(180 - self.kat_dachu))
        return round(x,2)

    def depka_oblicz(self):
        odleglosc = round(self.d_k_x + self.d_k_w, 2)
        kat = 0.5 * self.kat_dachu + self.kat_zaciecia
        kat = round(kat, 2)
        kat2 = round(90 - 0.5 * self.kat_dachu, 2)
        return {"odległość": odleglosc, "kąt": round(kat, 2), "kąt2": kat2}

    def s_z_oblicz(self):
        s_zaciecia = None
        if self.kat_dachu <= 90:
            kat_xD = 90 - self.kat_dachu
            c = math.tan(math.radians(kat_xD)) * self.h_krokwi
            s_zaciecia = self.d_k_x - c
            self.dkc = round(c, 2)
        else:
            s_zaciecia = self.d_k_x
            kat_z = 180 - self.kat_dachu
            kat_w = 90 - kat_z
            self.dkc = round(math.tan(math.radians(kat_w)) * self.h_krokwi, 2)
        return s_zaciecia

    def oblicz_kpd(self):
        kat = (180 - self.kat_dachu) / 2
        kpd = self.p / math.cos(math.radians(kat))
        return kpd


    def hp_oblicz(self):
        """
        Funkcja oblicza długość słupka z płatwią od wysokości murłaty do styku krokwi.
        Obliczenia prowadzone ze względu na podaną odległość od murłaty do słupka płatwi.
        :return:
        """
        hp = math.tan(math.radians((180 - self.kat_dachu) / 2)) * self.op
        return hp

    def dkmp_oblicz(self):
        """
        Funkcja liczy długość krokwi od murłaty do płatwy
        :return: dkmp
        """
        dkmp = self.op / math.cos(math.radians((180 - self.kat_dachu) / 2))
        return dkmp

    def djx_oblicz(self):
        """
        Funkcja zwraca długość jętki nachodzącej na krokwiew (równolegle do ziemi)

        :var kat_d: kąt pomiędzy prostą prostopadłą do krokwi przechodzącą przez punkt przecięcia spodu jętki z krokwią
                    , a jętką nachodzącą na krokwiew
        :var djx: długość jętki nachodzącej na krokiew
        :return:
        """
        kat_d = 90 - ((180 - self.kat_dachu) / 2)
        djx = self.h_krokwi / math.cos(math.radians(kat_d))
        return djx

    def djw_oblicz(self):
        """
        Funkcja obliczająca długość jętki wewnętrznej (bez nachodzenia na krokwy)
        :param
        :xd: zmienna przechowująca odległość od murłaty do prostej prostopadłej przechodzącej przez
             przecięcie jętki z krokwią
        :return:
        """
        xd = self.hj / math.tan(math.radians((180 - self.kat_dachu) / 2))
        djw = (0.5 * self.d - xd) * 2
        return djw

    def djkk_oblicz(self):
        """
        Funkcja zwracająca długość od końca krokwi do punktu przecięcia ze spodem jętki
        :return:
        """
        xd = self.hj / math.tan(math.radians((180 - self.kat_dachu) / 2))
        kjw = math.sqrt(xd*xd + self.hj * self.hj) # długość na krokwi od jętki do murłaty
        djkk = self.krokiew_poza_dachem + kjw # długość od jętki do końca krokwi
        return round(djkk, 2)

    def dkgp_oblicz(self):
        return round(self.d_k_x + (self.d_k_w - self.d_k_mp), 2)
    def podsumowanie(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f"{'Odległość między murłatami (po zewnętrzych stronach):':54s} {round(self.d, 2)}cm\n"
              f"{'Kąt rozwarcia dachu:':54s} {round(self.kat_dachu, 2)}\N{DEGREE SIGN}\n"
              f"{'Wysokość do spodu krokwi:':54s} {self.h}cm\n"
              f"{'Długość krokwi poza murłatą:':54s} {round(self.krokiew_poza_dachem,2)}cm\n"
              f"{'-' * 54}\n"
              f"{'Kąt zacięcia krokwi:':28s} {self.kat_zaciecia}\N{DEGREE SIGN}\n"
              f"{'Szerokość zacięcia:':28s} {self.s_zaciecia}cm\n"
              # f"Długość krokwi 'x': {round(self.d_k_x,2)}\n"
              f"{'Całkowita długość krokwi:':28s} {round(self.d_krokwi_calkowita,2)}cm\n"
              f"{'Długość krokwi wewnętrznej:':28s} {self.d_k_w}cm  (od zacięcia do depki)\n"
              f"Depka {'-' * 48}\n"
              f"{'-> rysowanie od góry:':28s} {self.depka['odległość']}cm\n"
              # f"{'  /od zacięcia:':28s} {round(self.d_k_w, 2)}cm\n"
              f"{'-> kąt (prostopadły):':28s} {self.depka['kąt']}\N{DEGREE SIGN}\n"
              f"{'-> kąt (równoległy):':28s} {self.depka['kąt2']}\N{DEGREE SIGN}\n"
              f"{'-' * 54}\n")

# data = {'h': 250, 'd': 900, 'p': 35, 'h_krokwi': 8, 'op': 200}
# data = {'kat_dachu': 80, 'd': 400, 'p': 35, 'h_krokwi': 8}
# dach1 = CieciaNaKrokwach(data)
# dach1.podsumowanie()