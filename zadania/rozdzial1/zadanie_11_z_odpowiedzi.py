import random

potencjalne_ruchy = 'LPGD'

def wylicz(przod: int, gora: int, prawa: int, ruchy: list):
    wynik = 0
    pomoc = 0

    for i in range(10):
        if ruchy[i] == 'P':
            wynik += gora
            pomoc = 7 - prawa
            prawa = przod
            przod = pomoc
        if ruchy[i] == 'L':
            wynik += gora
            pomoc = 7 - przod
            przod = prawa
            prawa = pomoc
        if ruchy[i] == 'D':
            wynik += 7 - przod
            pomoc = 7 - przod
            przod = gora
            gora = pomoc
        if ruchy[i] == 'G':
            wynik += przod
            pomoc = 7 - gora
            gora = przod
            przod = pomoc
        return wynik


tab = [0 for x in range(6)]

PRZOD = random.randint(1, 6)
tab[PRZOD - 1] = 1
tab[6 - PRZOD] = 1

GORA = random.randint(1,6)

while tab[GORA - 1] == 1 or tab[6 - GORA] == 1:
    GORA = random.randint(1,6)
tab[GORA - 1] = 1
tab[6-GORA] = 1

PRAWA = random.randint(1,6)
while tab[PRAWA - 1] == 1 or tab[6 - PRAWA] == 1:
    PRAWA = random.randint(1,6)
tab[PRAWA - 1] = 1
tab[6-PRAWA] = 1

sekwencja_gracza1 = [random.choice(potencjalne_ruchy) for i in range(10)]
sekwencja_gracza2 = [random.choice(potencjalne_ruchy) for i in range(10)]

wynik_gracza1 = wylicz(PRZOD, GORA, PRAWA, sekwencja_gracza1)
wynik_gracza2 = wylicz(PRZOD, GORA, PRAWA, sekwencja_gracza2)

if wynik_gracza1 == wynik_gracza2:
    print('REMIS')
elif wynik_gracza1 < wynik_gracza2:
    print('Gracz 1 wygral')
elif wynik_gracza2 < wynik_gracza1:
    print('Gracz 2 wygral')