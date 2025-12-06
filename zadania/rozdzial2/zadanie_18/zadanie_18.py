"""
Zadanie 18 – Systemy liczbowe
W pliku znajduje sie 100 wierszy po trzy liczby zapisane w systemach: binarnym, osemkowym i szesnastkowym. Znaki tworza
liczby z zakresu do 2^24. Trzeba wykonac wskazane obliczenia.

Zadanie 18.1 – Jaki system?
Dla kazdej liczby ustalic, w jakim systemie jest zapisana. Podac liczbe wystapien kazdego systemu.

Zadanie 18.2 – Max i min
Dla liczb z zadania 18.1 wyznaczyc najwieksza i najmniejsza liczbe po przeliczeniu na dziesietny.

Zadanie 18.3 – Ile znakow?
Zliczyc czestosc wystepowania kazdego znaku od 0 do A we wszystkich liczbach z pliku i podac ja w procentach.
"""


from logging import setLogRecordFactory


class Suma():
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __init__(self):
        self._lista_liczb = []
        self._ile_razy_wystapil_system_liczbowy = None
        self._czestotliwosc_wystepowania_znakow = None
        self.najmniejsza_wartosc = 2**64 - 1
        self.najwieksza_wartosc = 0

    def dostac_liste_liczb(self):
        if not self._lista_liczb:
            with open('trzyliczby.txt', 'r') as file:
                for line in file:
                    self._lista_liczb.append(line.strip().split())

        return self._lista_liczb


    # def to_base(self, number: int, base: int) -> str:
    #     result = ''
    #     sign = '-' if number < 0 else ''
    #
    #     number = abs(number)
    #
    #     while number > 0:
    #         result = self.digits[number % base] + result
    #         number //= base
    #
    #     return sign + result

    def to_num(self, number: str, base: int) -> int:
        number = number[::-1]
        in_decimal = 0

        for i in range(len(number)):
            in_decimal += (base ** i) * self.digits.index(number[i])

        return in_decimal

    def odkad_zaczynac(self, number: str) -> int:
        return self.digits.index(max(number)) + 1

    def policzyc_ile_razy_co_wystapilo(self):
        if not self._ile_razy_wystapil_system_liczbowy:
            self._ile_razy_wystapil_system_liczbowy = {j : 0 for j in range(2, 17)}
            self._najwieksza_liczba_w_kazdym_systemie_liczbowym = {j : 0 for j in range(2, 17)}


            for zbior_liczb in self.dostac_liste_liczb():
                zaczac_od = max([self.odkad_zaczynac(i) for i in zbior_liczb])

                for j in range(zaczac_od, 17):

                    liczba_1 = self.to_num(zbior_liczb[0], j)
                    liczba_2 = self.to_num(zbior_liczb[1], j)
                    liczba_3 = self.to_num(zbior_liczb[2], j)

                    if liczba_1 + liczba_2 == liczba_3:
                        self._ile_razy_wystapil_system_liczbowy[j] += 1

                        if max(liczba_1, liczba_2, liczba_3) > self.najwieksza_wartosc:
                            self.najwieksza_wartosc = max(liczba_1, liczba_2, liczba_3)

                        if min(liczba_1, liczba_2, liczba_3) < 2**64 - 1:
                            self.najmniejsza_wartosc = min(liczba_1, liczba_2, liczba_3)



                        # if j == 15 or j == 16:
                        #     print(j, ' - ', zbior_liczb,
                        #           self.to_num(zbior_liczb[0], j),  self.to_num(zbior_liczb[1], j), self.to_num(zbior_liczb[2], j))
                        break

        return self._ile_razy_wystapil_system_liczbowy

    def policzyc_czestotliwosc_wystepowania_znakow(self):
        if not self._czestotliwosc_wystepowania_znakow:
            self._czestotliwosc_wystepowania_znakow = {self.digits[i] : 0 for i in range(11)}
            potrzebne_znaki = self.digits[:11]
            ogolna_ilosc_wystepowania = 0

            with open('trzyliczby.txt', 'r') as file:
                ciag_tekstowy = file.read().replace('\n', '').replace(' ', '')

            for element in potrzebne_znaki:
                self._czestotliwosc_wystepowania_znakow[element] = ciag_tekstowy.count(element)
                ogolna_ilosc_wystepowania += ciag_tekstowy.count(element)

        for element in self._czestotliwosc_wystepowania_znakow.keys():
            print(f"{element} wystapilo w {round(ciag_tekstowy.count(element) / ogolna_ilosc_wystepowania * 100, 2)}%")


        return self._czestotliwosc_wystepowania_znakow




suma_klasa = Suma()

print("Zadanie 18.1\n", suma_klasa.policzyc_ile_razy_co_wystapilo(), sep='')

print(f"\n\nZadanie 18.2\n"
      f"Najwieksza wartosc to {suma_klasa.najwieksza_wartosc}\n"
      f"Najmniejsza wartosc {suma_klasa.najmniejsza_wartosc}")

print('\n\nZadanie 18.3')
suma_klasa.policzyc_czestotliwosc_wystepowania_znakow()