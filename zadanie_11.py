from os import linesep


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

if __name__ == '__main__':
    kostka = Kostka()
    kostka.obracanie_kostki('LLGPPD') == 6

    kostka = Kostka()
    kostka.obracanie_kostki('DLDLDPP') == 3

    kostka = Kostka()
    kostka.obracanie_kostki('DDPPDDLG') == 2