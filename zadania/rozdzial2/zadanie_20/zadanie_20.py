"""
Zadanie 20 – Anagramy
Anagram to wyraz powstaly przez przestawienie liter innego wyrazu. W pliku sa rozne wyrazy, trzeba wykonac zadania
dotyczace anagramow.

Zadanie 20.1 – Pary
Znalezc pary wyrazow z pliku, ktore sa anagramami.

Zadanie 20.2 – Zamien jedna litere
Dla wyrazow, ktore nie sa anagramami, sprawdzic, czy zamiana jednej litery wystarczy, by jeden wyraz mogl stac sie
anagramem drugiego. Okreslic, ktora litere nalezy zamienic.

Zadanie 20.3 – Przekombinowana bura
Zmodyfikowac wyraz "bura" tak, aby stal sie anagramem innego z pliku, zgodnie z zasadami podanymi w zadaniu.

Zadanie 20.4 – Wszystkie anagramy
Dla kazdego wyrazu z pliku wypisac wszystkie mozliwe anagramy uzyskane z jego liter. Unikac powtorzen i bledow.
"""

class Slowa():
    def __init__(self):
        self._lista_par_anagramow = []
        self._lista_nie_anagramow = []

        self._lista_wyrazow = []

    def dostac_liste_par_anagramow(self):
        if not self._lista_par_anagramow:
            with open('anagramy.txt', 'r') as file:
                for line in file:
                    line = line.strip().split()
                    self._lista_par_anagramow.append((line[0], line[1]))

        return self._lista_par_anagramow

    def policzyc_pary_anagramow(self):
        ilosc_par_anagramow = 0

        for para in self.dostac_liste_par_anagramow():
            if not len(para[0]) == len(para[1]):
                continue

            nie_jest_anagramem = False

            for i in set(para[0]):
                if para[0].count(i) != para[1].count(i):
                    nie_jest_anagramem = True
                    break

            if not nie_jest_anagramem:
                ilosc_par_anagramow += 1


        return ilosc_par_anagramow

    def pary_nie_anagramow(self):
        if not self._lista_nie_anagramow:
            for para in self.dostac_liste_par_anagramow():
                if not len(para[0]) == len(para[1]):
                    self._lista_nie_anagramow.append(para)
                    continue

                nie_jest_anagramem = False

                for i in set(para[0]):
                    if para[0].count(i) != para[1].count(i):
                        self._lista_nie_anagramow.append(para)
                        break

                if nie_jest_anagramem:
                    self._lista_nie_anagramow.append(para)

        return self._lista_nie_anagramow

    def przekombinowana_buraz(self) -> list:
        lista_liter = list('burza')

        #
        #
        #




slowa_klasa = Slowa()

print(slowa_klasa.dostac_liste_par_anagramow())

print(f"\n\nZadanie 20.1\n"
      f"Par anagramow jest {slowa_klasa.policzyc_pary_anagramow()}"
      f"\n-------\n"
      f"")

print(len(slowa_klasa.pary_nie_anagramow()))