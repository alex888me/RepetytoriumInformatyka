class Dzielniki():
    def __init__(self):
        self._lista_liczb = []
        self._lista_dzielnikow_liczb_tuple = []
        self._lista_dzielnikow_liczb_set = []
        self._lista_pary_liczb_wzglednie_pierwszych = []
        self._lista_liczb_z_dokladnie_dziewiec_unikalnych_dzielnikow = []
        self._lista_liczb_doskonalych = []

    def dostac_liste_liczb(self):
        if not self._lista_liczb:
            with open('liczby16.txt', 'r') as file:
                for line in file:
                    line.strip()
                    self._lista_liczb.append(int(line))

        return self._lista_liczb

    def dostac_liste_dzielnikow_liczb_tuple(self):
        if not self._lista_dzielnikow_liczb_tuple:
            for liczba in self.dostac_liste_liczb():
                dzielniki_liczby = [1, liczba]
                for i in range(liczba // 2, 1, -1):
                    if liczba % i == 0:
                        dzielniki_liczby.append(i)

                self._lista_dzielnikow_liczb_tuple.append(tuple(dzielniki_liczby))
                self._lista_dzielnikow_liczb_set.append(set(dzielniki_liczby))


        return self._lista_dzielnikow_liczb_tuple

    def dostac_liste_dzielnikow_liczb_set(self):
        if not self._lista_dzielnikow_liczb_set:
            self.dostac_liste_dzielnikow_liczb_tuple()

        return self._lista_dzielnikow_liczb_set

    def dostac_liste_liczb_wzglednie_pierwszych(self):
        set_one = set([1])
        if not self._lista_pary_liczb_wzglednie_pierwszych:
            lista_liczb = self.dostac_liste_liczb()
            lista_dzielnikow_liczb_set = self.dostac_liste_dzielnikow_liczb_set()

            for i in range(len(lista_liczb) - 1):
                for j in range(i + 1, len(lista_liczb)):
                    a = lista_dzielnikow_liczb_set[i].difference(set_one)
                    b = lista_dzielnikow_liczb_set[j].difference(set_one)
                    if not len(a.intersection(b)):
                        self._lista_pary_liczb_wzglednie_pierwszych.append((self._lista_liczb[i], self._lista_liczb[j]))

        return  self._lista_pary_liczb_wzglednie_pierwszych

    def dostac_liste_liczb_z_dokladnie_dziewiec_unikalnych_dzielnikow(self):
        if not self._lista_liczb_z_dokladnie_dziewiec_unikalnych_dzielnikow:
            for i in range(len(self.dostac_liste_liczb())):
                if len(self.dostac_liste_dzielnikow_liczb_set()[i]) == 9:
                    self._lista_liczb_z_dokladnie_dziewiec_unikalnych_dzielnikow.append(self.dostac_liste_liczb()[i])

        return self._lista_liczb_z_dokladnie_dziewiec_unikalnych_dzielnikow

    def dostac_liste_liczb_doskonalych(self):
        if not self._lista_liczb_doskonalych:
            for i in range(len(self.dostac_liste_liczb())):
                suma = 0
                for cyfra in self.dostac_liste_dzielnikow_liczb_tuple()[i]:
                    if cyfra != self.dostac_liste_liczb()[i]:
                        suma += cyfra

                if suma == self.dostac_liste_liczb()[i]:
                    self._lista_liczb_doskonalych.append(self.dostac_liste_liczb()[i])

        return self._lista_liczb_doskonalych





dzielniki_klasa = Dzielniki()

print(f"Zadanie 16.1 | ilosc par wzglednie pierwszych to {len(dzielniki_klasa.dostac_liste_liczb_wzglednie_pierwszych())}")
print(f"Zadanie 16.2 | {dzielniki_klasa.dostac_liste_liczb_z_dokladnie_dziewiec_unikalnych_dzielnikow()}")
print(f"Zadanie 16.3 | lista liczb doskonalych to {dzielniki_klasa.dostac_liste_liczb_doskonalych()}")