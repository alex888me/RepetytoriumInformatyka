"""
Zadanie 19 – Zestaw rakietowy
Rakiety sa w punkcie centralnym. Przeciwnicy sa rozmieszczeni w promieniu od -20 do 20. Nalezy wykonac okreslone
obliczenia dotyczace zniszczen.

Zadanie 19.1 – Jakie straty?
Rakieta ma minimalny zasieg 1 km i maksymalny 20 km. Oddzial przeciwnika zostaje zniszczony, jesli jego odleglosc miesci
sie w zasiegu. Trzeba okreslic liczbe zniszczonych oddzialow.

Zadanie 19.2 – Maksymalny zasieg
Jesli minimalny zasieg moze wynosic 0.1 km, nalezy znalezc najmniejszy maksymalny zasieg pozwalajacy zniszczyc wszystkie
oddzialy.

Zadanie 19.3 – Jeden strzal
Przy zasiegu niszczacym 2 km rakieta celuje w punkt o wspolrzednych calkowitych. Jesli oddzial znajduje sie w odleglosci
2 km, traci 25% stanu, a gdy blizej – zostaje zniszczony. Trzeba znalezc punkt, w ktory nalezy strzelic, by straty byly
maksymalne.
"""


import math

class ZestawRakietowy():
    ROZMIAR_ODDZIALU = 100
    MAKSYMALNY_ZASIEG = 20
    MINIMALNY_ZASIEG = 1

    def __init__(self):
        self._pozycje_oddzialow = []


    def dostac_pozycje_oddzialow(self):
        if not self._pozycje_oddzialow:
            with open('oddzialy.txt', 'r') as file:
                for line in file:
                    line = line.strip().split()
                    self._pozycje_oddzialow.append((int(line[0]), int(line[1])))

        return self._pozycje_oddzialow

    def obliczyc_dystans(self, pozycja_1: tuple, pozycja_2: tuple) -> float:
        return math.sqrt((pozycja_1[0] - pozycja_2[0]) ** 2 + (pozycja_1[1] - pozycja_2[1]) ** 2)

    def rakietowy_baraz(self):
        straty_przeciwnika = 0
        oddzialy_poza_zasiegiem = 0

        for pozycja_oddzialu in self.dostac_pozycje_oddzialow():
            dystans_do_panstwa = self.obliczyc_dystans((0, 0), pozycja_oddzialu)

            if self.MAKSYMALNY_ZASIEG > dystans_do_panstwa > self.MINIMALNY_ZASIEG:
                straty_przeciwnika += self.ROZMIAR_ODDZIALU
            elif dystans_do_panstwa == self.MINIMALNY_ZASIEG or dystans_do_panstwa == self.MAKSYMALNY_ZASIEG:
                straty_przeciwnika += self.ROZMIAR_ODDZIALU * 0.25
            else:
                oddzialy_poza_zasiegiem += 1

        return math.floor(straty_przeciwnika), oddzialy_poza_zasiegiem

    def maksymalny_zasieg_zeby_wszystkich_zabic(self):
        nowy_maksymalny_zasieg = 0.1

        for pozycja_oddzialu in self.dostac_pozycje_oddzialow():
            if self.obliczyc_dystans((0,0), pozycja_oddzialu) > nowy_maksymalny_zasieg:
                nowy_maksymalny_zasieg = self.obliczyc_dystans((0,0), pozycja_oddzialu)


        return nowy_maksymalny_zasieg

    def najlepszy_stral(self):
        wspolrzedne_najlepszego_strzalu = (0, 0)
        straty_od_najlepszego_strzalu = 0

        for x in range(-20, 21):
            for y in range(-20, 21):

                if self.obliczyc_dystans((x, y), (0, 0)) <= 2:
                    continue

                straty_od_danego_strzalu = 0

                for pozycja_oddzialu in self.dostac_pozycje_oddzialow():
                    if self.obliczyc_dystans((x, y), pozycja_oddzialu) < 2:
                        straty_od_danego_strzalu += self.ROZMIAR_ODDZIALU
                    elif self.obliczyc_dystans((x, y), pozycja_oddzialu) == 2:
                        straty_od_danego_strzalu += math.floor(self.ROZMIAR_ODDZIALU * 0.25)

                    if straty_od_danego_strzalu > straty_od_najlepszego_strzalu:
                        wspolrzedne_najlepszego_strzalu = (x, y)
                        straty_od_najlepszego_strzalu = straty_od_danego_strzalu



        return wspolrzedne_najlepszego_strzalu, straty_od_najlepszego_strzalu

zestaw_rakietowy = ZestawRakietowy()

print(zestaw_rakietowy.dostac_pozycje_oddzialow(), '\n\n------\n')

print(f"Zadanie 19.1\n - "
      f"Straty przeciwnika to {int(zestaw_rakietowy.rakietowy_baraz()[0])}, oddzialow poza zasiegiem {zestaw_rakietowy.rakietowy_baraz()[1]}\n\n------\n")

print(f"Zadanie 19.2\n"
      f"- Minimalny maksymalny zasieg to {round(zestaw_rakietowy.maksymalny_zasieg_zeby_wszystkich_zabic(), 3)} km\n\n------\n")

print(f"Zadanie 19.3\n"
      f"- Wspolrzedne najlepszego strzalu to {zestaw_rakietowy.najlepszy_stral()[0]}, straty jakie poniesie wrog to {zestaw_rakietowy.najlepszy_stral()[1]}")
