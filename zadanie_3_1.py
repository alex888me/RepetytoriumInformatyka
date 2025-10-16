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
"""