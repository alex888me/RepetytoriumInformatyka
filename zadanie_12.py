from pprint import pprint
from string import ascii_uppercase
from typing import Optional, List

litery = ascii_uppercase[:8]


def ile_bije(pozycja: str):
    ile_pozycji_moze_bic = 0
    pozycja = (litery.index(pozycja[0]), int(pozycja[1]) - 1)

    # w prawo i lewo
    ile_pozycji_moze_bic += (8 - (pozycja[0] + 1)) + ((pozycja[0] + 1) - 1)

    # w gore i dol
    ile_pozycji_moze_bic += (8 - (pozycja[1] + 1)) + ((pozycja[1] + 1) - 1)

    # w prawo gore
    ile_pozycji_moze_bic += min([(8 - (pozycja[0] + 1)), (8 - (pozycja[1] + 1))])

    # w prawo dol
    ile_pozycji_moze_bic += min([pozycja[0], (8 - (pozycja[1] + 1))])

    # w lewo gore
    ile_pozycji_moze_bic += min([(8 - (pozycja[0] + 1)), pozycja[1]])

    # w lewo dol
    ile_pozycji_moze_bic += min([pozycja[0], pozycja[1]])

    return ile_pozycji_moze_bic



class Szachowinca:
    def __init__(self, szachowinca_list: Optional[List] = None):
        if szachowinca_list:
            self.szachowinca_list = [row[:] for row in szachowinca_list]
        else:
            self.szachowinca_list = [[0 for i in range(8)] for j in range(8)]

    def set_komurka(self, x: int, y: int, value: int):
        qqq = self.szachowinca_list[x][y]
        if self.szachowinca_list[x][y] == 9:
            raise ValueError(f"bitaya {x}, {y}")

        self.szachowinca_list[x][y] = value

    def fill(self, x, y):
        self.set_komurka(x, y, 9)
        for k in range(8):
            if k != y:
                self.set_komurka(x, k, 1)
            if k != x:
                self.set_komurka(k, y, 2)

        if y >= x:
            start_1 = [0, y - x]
        else:
            start_1 = [x - y, 0]

        if y >= x:
            end_1 = [7 - (y - x), 7]
        else:
            end_1 = [7, 7 - (x - y)]


        krok_1 = start_1[0]
        for i in range(start_1[1], end_1[1] + 1):
            if krok_1 == x and i == y:
                krok_1 += 1
                continue
            self.set_komurka(krok_1, i, 3)
            krok_1 += 1

        if x + y >= 7:
            start_2 = [x + y - 7, 7]
        else:
            start_2 = [0, x + y]


        if x + y >= 7:
            end_2 = [7, x + y - 7]
        else:
            end_2 = [x + y, 0]

        krok_2 = start_2[0]
        for i in range(start_2[1], end_2[1] - 1, -1):
            if krok_2 == x and i == y:
                krok_2 += 1
                continue
            self.set_komurka(krok_2, i, 4)

            krok_2 += 1

# sh1 = Szachowinca()
# sh1.fill(6, 1)
# pprint(sh1.szachowinca_list)

counter = 0
for a in range(8):
    sh1 = Szachowinca()
    sh1.fill(0, a)

    for b in range(8):
        sh2 = Szachowinca(szachowinca_list=sh1.szachowinca_list)
        try:
            sh2.fill(1, b)
        except ValueError:
            continue

        for c in range(8):
            sh3 = Szachowinca(szachowinca_list=sh2.szachowinca_list)
            try:
                sh3.fill(2, c)
            except ValueError:
                continue
            for d in range(8):
                sh4 = Szachowinca(szachowinca_list=sh3.szachowinca_list)
                try:
                    sh4.fill(3, d)
                except ValueError:
                    continue
                for e in range(8):
                    sh5 = Szachowinca(szachowinca_list=sh4.szachowinca_list)
                    try:
                        sh5.fill(4, e)
                    except ValueError:
                        continue
                    for f in range(8):
                        sh6 = Szachowinca(szachowinca_list=sh5.szachowinca_list)
                        try:
                            sh6.fill(5, f)
                        except ValueError:
                            continue
                        for g in range(8):
                            sh7 = Szachowinca(szachowinca_list=sh6.szachowinca_list)
                            try:
                                sh7.fill(6, g)
                            except ValueError:
                                continue
                            for h in range(8):
                                sh8 = Szachowinca(szachowinca_list=sh7.szachowinca_list)
                                try:
                                    sh8.fill(7, h)
                                except ValueError:
                                    continue
                                pprint(sh8.szachowinca_list)
                                counter += 1


print(counter)