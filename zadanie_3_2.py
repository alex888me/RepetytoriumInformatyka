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

Zadanie 3.2. Odpowiedz na pytania (0–1 pkt)
Zaznacz odpowiednio P – prawda lub F – fałsz.
Nr	Treść zdania	P	F
1	Wartość p zmienia się tyle samo razy, ile powtórzeń wykonuje główna pętla.
2	Zmienna k wskazuje liczbę dzielników całkowitych zmiennej n.
3	Napis TAK jest wypisywany, jeśli n ma parzystą liczbę różnych czynników w rozkładzie na czynniki pierwsze.
4	Napis NIE jest wypisywany, jeśli n ma nieparzystą liczbę czynników w rozkładzie na czynniki pierwsze.
"""