"""
Zadanie 3. Analiza algorytmu
Ponizej zostal przedstawiony algorytm wypisujący dla zadanej wartości n ≥ 0 napis TAK lub NIE.

Algorytm
k ← 0
p ← 2
dopóki n > 1
    jeżeli n mod p = 0
    k ← k + 1
        dopóki n mod p = 0 i n > 1
            n ← n div p

    p ← p + 1
jeżeli k mod 2 = 0
    wypisz TAK
w przeciwnym przypadku
    wypisz NIE

Uwaga: mod oznacza resztę z dzielenia, div oznacza część całkowitą z dzielenia.

Zadanie 3.1. Domyśl się, co robi (0–1 pkt)
Przeanalizuj algorytm i uzupełnij tabelę dla podanych danych.
n	55	64	92	210	215
Wypisywana wartość

Zadanie 3.2. Odpowiedz na pytania (0–1 pkt)
Zaznacz odpowiednio P – prawda lub F – fałsz.
Nr	Treść zdania	P	F
1	Wartość p zmienia się tyle samo razy, ile powtórzeń wykonuje główna pętla.
2	Zmienna k wskazuje liczbę dzielników całkowitych zmiennej n.
3	Napis TAK jest wypisywany, jeśli n ma parzystą liczbę różnych czynników w rozkładzie na czynniki pierwsze.
4	Napis NIE jest wypisywany, jeśli n ma nieparzystą liczbę czynników w rozkładzie na czynniki pierwsze.


"""

petla_razy = 0
p_zmieniono = 0

def algorytm_3(n):
    if not (isinstance(n, int) or isinstance(n, float) and n >= 0):
        raise TypeError('Nie ten typ danych.')
    k = 0
    p = 2


    while n > 1:
        if n % p == 0:
            k = k + 1
            while n % p == 0 and n > 1:
                n = n // p
        p = p + 1
    if k % 2 == 0:
        return True
    else:
        return False


def algorytm_3_3(n):
    if not (isinstance(n, int) or isinstance(n, float) and n >= 0):
        raise TypeError('Nie ten typ danych.')
    k = 0
    p = 2
    liczba = n
    dzielniki = {}
    dominante_dzielniki = {}
    # Najwieksza ilosc wystepowania jednego lub wielu dzielnikow
    x = 0

    while n > 1:
        if n % p == 0:
            k = k + 1
            while n % p == 0 and n > 1:
                if p not in dzielniki.keys():
                    dzielniki[p] = 1
                else:
                    dzielniki[p] += 1
                n = n // p
        p = p + 1

    for k, v in dzielniki.items():
        if v >= x:
            dominante_dzielniki[k] = v

    if len(dominante_dzielniki) != 1:
        print(f"Dla n={liczba} wynik BRAK")
    else:
        dominantny_dzielnik = None
        for k in dominante_dzielniki.keys():
            print(k)
            dominante_dzielniki = k
        print(f"Dla n={liczba} wynik {k} {dzielniki[k]}")

for i in [64, 54, 15]:
    algorytm_3_3(i)

if __name__ == '__main__':
    expected_output = {
        55 : True,
        64 : False,
        92 : True,
        210 : True,
        215 : True,
    }

    for arg, output in expected_output.items():
        assert algorytm_3(arg) == output