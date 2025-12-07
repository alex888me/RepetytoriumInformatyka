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
        ilosc_par_nie_anagramow = 0

        for para in self.dostac_liste_par_anagramow():
            if not len(para[0]) == len(para[1]):
                continue

            different_letters = 0

            letters_0 = {x : para[0].count(x) for x in set(para[0])}
            letters_1 = {x : para[1].count(x) for x in set(para[1])}
            letters_union = set(letters_0.keys())
            letters_union.update(letters_1.keys())

            if para[0] == 'MVUJIRJPGXSWJJCESMNGOBEIZMSOYAZZYET':
                print('AAAA')
                print(sorted(letters_union))
                print([(i, letters_0[i]) for i in sorted(letters_0)])
                print([(i, letters_1[i]) for i in sorted(letters_1)])

            for letter in letters_union:
                if letter in letters_0 and letter in letters_1:
                    different_letters += abs(letters_0[letter] - letters_1[letter])
                elif letter in letters_0:
                    different_letters += letters_0[letter]
                else:
                    different_letters += letters_1[letter]

            if different_letters == 2:
                letter_to_change = ''
                index_from_left = None

                if len(letters_0.keys()) == len(letters_union) and len(letters_1.keys()) == len(letters_union):
                    for letter in letters_1.keys():
                        if letters_1[letter] - letters_0[letter] == 1:
                            for i in range(len(para[1])):
                                if para[1][i] == letter:
                                    if not index_from_left:
                                        index_from_left = i
                                        letter_to_change = letter
                                        print(para, index_from_left, letter)

                # if len(letters_0.keys()) == len(letters_1.keys()):
                #     for letter in letters_1.keys():
                #         if letters_1[letter] - letters_0[letter]:
                #             if not letter_to_change:
                #                 letter_to_change = letter
                #
                #                 for i in range(len(para[1])):
                #                     if para[1][i] == letter_to_change:
                #                         index_from_left = i
                #                         print(para, letter_to_change, i)

                # print(para)


            # if para[0] == 'MVUJIRJPGXSWJJCESMNGOBEIZMSOYAZZYET':
            #     print(different_letters)

            # print(different_letters)


            # print(para)
            # print(letters_0, letters_1)

            # for key in letters_0.keys():
            #     if key not in letters_1:
            #         different_letters += letters_0[key]
            #     else:
            #         different_letters += abs(letters_0[key] - letters_1[key])

            # for key in letters_1.keys():
            #     if key not in letters_0:
            #         different_letters += letters_1[key]

            # if different_letters == 1:

        return

    def przekombinowana_buraz(self) -> list:
        lista_liter = list('bura')
        lista_permutacji = []
        for i in range(4):
            for j in range(4):
                if i == j:
                    continue
                for k in range(4):
                    if k == i or k == j:
                        continue
                    for l in range(4):
                        if l == k or l == j or l == i:
                            continue
                        lista_permutacji.append(f"{lista_liter[i]}{lista_liter[j]}{lista_liter[k]}{lista_liter[l]}")
        return lista_permutacji




slowa_klasa = Slowa()

# print(slowa_klasa.dostac_liste_par_anagramow())
#
# print(f"\n\nZadanie 20.1\n"
#       f"Par anagramow jest {slowa_klasa.policzyc_pary_anagramow()}"
#       f"\n-------\n"
#       f"")
print(slowa_klasa.pary_nie_anagramow())
#
# print(slowa_klasa.przekombinowana_buraz())
