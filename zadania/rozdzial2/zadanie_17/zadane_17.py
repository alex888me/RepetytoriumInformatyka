"""
Zadanie 17 – PESEL
Opis ogolny numeru PESEL oraz sposob wyliczania cyfry kontrolnej.

Zadanie 17.1 – Liczba kobiet i mezczyzn
Na podstawie numerow PESEL okreslic, ile jest kobiet, a ile mezczyzn.

Zadanie 17.2 – Bledna cyfra kontrolna
Sprawdzic, ktore numery PESEL w pliku maja niepoprawna cyfre kontrolna i wypisac je.

Zadanie 17.3 – Podzial wedlug rocznika
Podzielic osoby na grupy wiekowe: 18 lat i mniej, 19–50, oraz powyzej 50 lat. Podac, ile osob nalezy do kazdej grupy.
"""

from datetime import datetime, timedelta


class IncorLen(ValueError):
    pass

class IncorKonrolNum(ValueError):
    pass


class Pesel:
    wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]

    def __init__(self, pesel_as_str: str):
        if not isinstance(pesel_as_str, str):
            raise TypeError('Nie ten typ PESELu')

        if len(pesel_as_str) != 11:
            raise IncorLen('Nie ta dlugosc peselu')

        try:
            int(pesel_as_str)
        except ValueError as e:
            raise ValueError('Pesel musi zawierac tylko cyfry') from e

        self._pesel_as_str = pesel_as_str

        self.rr = self._pesel_as_str[:2]
        self.mm = self._pesel_as_str[2:4]
        self.dd = self._pesel_as_str[4:6]
        self.pppp = self._pesel_as_str[6:10]
        self.k = self._pesel_as_str[-1]

    def __str__(self):
        return (f"{self.rr}-{self.mm}-{self.dd}-{self.pppp}-{self.k} "
                f"{self.urodziny()}"
        )

    @classmethod
    def _pomnozyc_przez_wagi(cls, num: int, wagi: int) -> int:
        return (num * wagi) % 10

    def sprawdzenie_cyfry_kontrolnej(self):
        suma_mnozen_przez_wagi = 0

        for i in range(10):
            suma_mnozen_przez_wagi += self._pomnozyc_przez_wagi(int(self._pesel_as_str[i]), self.wagi[i])

        if 10 - (suma_mnozen_przez_wagi % 10)  != int(self._pesel_as_str[-1]):
            raise IncorKonrolNum('Bledny numer kontrolny')

    def _jakie_stulecie(self) -> int:
        miesiac = int(self.mm)

        if miesiac - 80 > 0:
            return 1800
        elif miesiac - 60 > 0:
            return 2200
        elif miesiac - 40 > 0:
            return 2100
        elif miesiac - 20 > 0:
            return 2000
        else:
            return 1900

    def _jaki_miesiac(self):
        miesiac = int(self.mm)

        if miesiac - 80 > 0:
            return miesiac - 80
        elif miesiac - 60 > 0:
            return miesiac - 60
        elif miesiac - 40 > 0:
            return miesiac - 40
        elif miesiac - 20 > 0:
            return miesiac - 20
        else:
            return miesiac


    def is_man(self) -> bool:
        return int(self._pesel_as_str[-2]) % 2 == 1

    def is_woman(self) -> bool:
        return int(self._pesel_as_str[-2]) % 2 == 0

    def urodziny(self) -> datetime:
        return datetime(
            year=self._jakie_stulecie() + int(self.rr),
            month=int(self._jaki_miesiac()),
            day=int(self.dd),
        )

    def wiek(self) ->  timedelta:
        return datetime.now() - self.urodziny()

    def wiek_w_roku(self, date: datetime) -> int:
        return date.year - self.urodziny().year

class PeselsList:
    def __init__(self):
        self._lista_peselow_as_str = []
        self._lista_peselow = []
        self._lista_blednych_peselow = []

        self.ilosc_mezczyzn = 0
        self.ilosc_kobiet = 0

    def dostac_liste_peselow_as_str(self):
        if not self._lista_peselow_as_str:
            with open('pesel.txt', 'r') as file:
                for line in file:
                    self._lista_peselow_as_str.append(line.strip())

        return self._lista_peselow_as_str

    def dostac_liste_blednych_peselow(self):
        if not self._lista_blednych_peselow:
            for pesel_as_str in self.dostac_liste_peselow_as_str():
                try:
                    nowy_pesel = Pesel(pesel_as_str)
                    nowy_pesel.sprawdzenie_cyfry_kontrolnej()
                except Exception:
                    self._lista_blednych_peselow.append(pesel_as_str)

        return self._lista_blednych_peselow

    def policzyc_kobiety_i_mezczyzny(self):
        self.ilosc_kobiet, self.ilosc_mezczyzn = 0, 0

        for pesel_as_str in self.dostac_liste_peselow_as_str():
            if int(pesel_as_str[-2]) % 2 == 0:
                self.ilosc_kobiet += 1
            else:
                self.ilosc_mezczyzn += 1

    def grupy_wiekowe(self):
        ludzie_do_18 = 0
        ludzie_od_19_do_50 = 0
        ludzie_od_51_do_100 = 0
        ludzie_od_100 = 0

        for pesel_as_str in self.dostac_liste_peselow_as_str():
            pesel = Pesel(pesel_as_str)
            wiek = pesel.wiek_w_roku(datetime(2022, 1, 1))

            if wiek <= 18:
                ludzie_do_18 += 1
            elif wiek <= 50:
                ludzie_od_19_do_50 += 1
            elif wiek <= 100:
                ludzie_od_51_do_100 += 1
            else:
                ludzie_od_100 += 1

        return (ludzie_do_18, ludzie_od_19_do_50, ludzie_od_51_do_100, ludzie_od_100)

pesel_lista = PeselsList()
pesel_lista.policzyc_kobiety_i_mezczyzny()
grupy_wiekowe = pesel_lista.grupy_wiekowe()

print(f"Zadanie 17. 1\n"
      f"Ilosc kobiet to {pesel_lista.ilosc_kobiet} a mezczyzn jest {pesel_lista.ilosc_mezczyzn}"
      f"\n"
      f"\n"
      f"Zadanie 17.2"
      f"Lista blednych peselow to {pesel_lista.dostac_liste_blednych_peselow()}"
      f"\n"
      f"\n"
      f"Zadanie 17.3\n"
      f"Ludzie 0-18 {grupy_wiekowe[0]}; Ludzie 19-50 {grupy_wiekowe[1]}; "
      f"Ludzie 51-100 {grupy_wiekowe[2]}; Ludzie 100+ {grupy_wiekowe[3]}")







