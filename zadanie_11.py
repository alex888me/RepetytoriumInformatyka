"""
Zadanie 11. Kostka do gry

Kości do gry – niewielkie wielościany z umieszczonymi na poszczególnych bokach liczbami (oczkami) – wykorzystywane są w grach planszowych, fabularnych, bitewnych i hazardowych w celu generowania losowych wyników. Najczęściej spotykane są kostki sześcienne.
Tradycyjnie rozmieszczenie oczek (suma przeciwległych ścian równa 7) daje dwa możliwe typy kostek sześciennych – prawo- i lewoskrętne. Jeśli patrzymy na wierzchołek, na którym stykają się ściany oznaczone 1, 2, 3, rosnące wartości oznaczają kierunek. Na obrazku przedstawiono kostkę lewoskrętną.
Siatka takiej kostki wygląda następująco:

Zadanie 11.1. Schemat obrotu (0–2 pkt)
Przyjmijmy, że położenie startowe kostki jest następujące:
Kostkę możemy obracać w lewo – L, w prawo – P, w dół – D, w górę – G. Każdy obrót odbywa się o 90° w danym kierunku.
Podaj wartość, która będzie na przedniej ścianie po wykonaniu sekwencji ruchów.

| Sekwencja ruchów | Wartość na przedniej ścianie |
| ---------------- | ---------------------------- |
| LLGPPD           | 6                            |
| DLLDPP           |                              |
| DDDPPDDLG        |                              |

Zadanie 11.2. Automat obrotu (0–3 pkt)
Wymyśl, że komputer wykonuje następującą grę w kostkę, w której jedyną zasadą jest to, że suma oczek na przeciwległych ścianach zawsze wynosi 7. W układzie ścian przednia, górna i prawa (podobnie jak w zadaniu 11.1) następuje przeprowadzenie symulacji rozgrywki dwóch graczy.
Rozgrywka powinna być zapisana w formie funkcji wywoływanej oddzielnie dla każdego z graczy.

Zasady rozgrywki:

Każdy z graczy tworzy sekwencję 10 ruchów.

Każdy gracz zaczyna obroty kostką od takiego samego początkowego ustawienia.

Po wykonaniu pojedynczego obrotu gracz dolicza się taką liczbę punktów, jaka znajduje się na górnej ścianie kostki.

Wygrywa gracz, który zbierze najmniejszą liczbę punktów.
"""

import random
import time
from os import linesep

random.seed(time.time())

class Kostka:
    """
    0 - przedna sciana  1
    1 - dolna sciana    2
    2 - prawa sciana    3
    3 - lewa sciana     4
    4 - gorna sciana    5
    5 - tylna sciana    6
    """


    def __init__(self):
        self.kostka = [i + 1 for i in range(6)]

    def __str__(self):
        return (f"przedna sciana {self.kostka[0]}{linesep}"
                f"dolna sciana {self.kostka[1]}{linesep}"
                f"prawa sciana {self.kostka[2]}{linesep}"
                f"lewa sciana {self.kostka[3]}{linesep}"
                f"gorna sciana {self.kostka[4]}{linesep}"
                f"tylna sciana {self.kostka[5]}{linesep}")

    def lewo(self):
        self.kostka[0], self.kostka[2], self.kostka[3], self.kostka[5] = \
            self.kostka[2], self.kostka[5], self.kostka[0], self.kostka[3]

    def prawo(self):
        self.kostka[0], self.kostka[2], self.kostka[5], self.kostka[3] = \
            self.kostka[3], self.kostka[0], self.kostka[2], self.kostka[5]

    def gora(self):
        self.kostka[4], self.kostka[1], self.kostka[5], self.kostka[0] = \
            self.kostka[0], self.kostka[5], self.kostka[4], self.kostka[1]

    def dol(self):
        self.kostka[0], self.kostka[4], self.kostka[5], self.kostka[1] = \
            self.kostka[4], self.kostka[5], self.kostka[1], self.kostka[0]

    def obracanie_kostki(self, sekwencja: str) -> int:
        sekwencja.upper()

        for litera in sekwencja:
            if litera == 'L':
                self.lewo()
            elif litera == 'P':
                self.prawo()
            elif litera == 'G':
                self.gora()
            elif litera == 'D':
                self.dol()

        return self.kostka[0]

class Rozgrywka(Kostka):
    def obrocic_raz(self, ruch: str) -> int:
        if ruch == 'L':
            self.lewo()
        elif ruch == 'P':
            self.prawo()
        elif ruch == 'G':
            self.gora()
        elif ruch == 'D':
            self.dol()

    def pokrecic_kostke(self, ile_razy: int):
        ruchy = 'LDPG'

        for i in range(random.randint(1, ile_razy)):
            litera = random.choice(ruchy)
            self.obrocic_raz(litera)


    def rozpoczecie_zabawy(self, ilosc_graczy: int):
        punkty_graczow = [0 for gracz in range(ilosc_graczy)]

        stara_kostka = self.kostka[:]

        for gracz in range(ilosc_graczy):
            for ruch in range(10):
                self.pokrecic_kostke(1)
                punkty_graczow[gracz] += self.kostka[4]
            self.kostka = stara_kostka

        gracz_z_najmniejszymi_punktami = (0, punkty_graczow[0])

        for i in range(len(punkty_graczow)):
            if punkty_graczow[i] < gracz_z_najmniejszymi_punktami[1]:
                gracz_z_najmniejszymi_punktami = (i, punkty_graczow[i])

        ilosc_wygranych = 0
        for liczba_punktow in punkty_graczow:
            if liczba_punktow == gracz_z_najmniejszymi_punktami[1]:
                ilosc_wygranych += 1

        if ilosc_wygranych > 1:
            return 'Nikt nie wygrał'
        else:
            return f"Wygrał gracz nr.{gracz_z_najmniejszymi_punktami[0]+1} który miał {gracz_z_najmniejszymi_punktami[1]} punktów"



zabawa = Rozgrywka()
zabawa.pokrecic_kostke(100)
print(zabawa.rozpoczecie_zabawy(20))


if __name__ == '__main__':
    kostka = Kostka()
    kostka.obracanie_kostki('LLGPPD') == 6

    kostka = Kostka()
    kostka.obracanie_kostki('DLDLDPP') == 3

    kostka = Kostka()
    kostka.obracanie_kostki('DDPPDDLG') == 2