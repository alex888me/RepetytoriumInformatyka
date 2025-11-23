"""
Zadanie 13. Systemy liczbowe
W pliku tekstowym liczby13.txt znajduje się 2000 liczb z zakresu od 1 do 100000, po jednej w każdym wierszu. Napisz program (lub programy), który odpowie na poniższe zadania.

Zadanie 13.1. System binarny (0-2 pkt)
Podaj liczbę, która w zapisie binarnym ma taką samą liczbę zer i jedynek.

Zadanie 13.2. System piątkowy, siódemkowy i trzynastkowy (0-3 pkt)
Każdy system liczbowy ma cyfrę o największej wartości, np. w systemie dwójkowym to 1, w systemie czwórkowym to 3 itd.
Podaj, które liczby w systemie piątkowym, siódemkowym i trzynastkowym mają największą liczbę cyfr o największej wartości.

Zadanie 13.3. Symetryczne liczby szesnastkowe (0-2 pkt)
Liczby symetryczne to są liczby o napisie dwukierunkowym, które są symetryczne względem swojego środka, np. FDAF, ADDA, B12321B.
Wypisz liczby, które w zapisie szesnastkowym będą liczbami symetrycznymi.
"""

from pathlib import Path

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def to_base(num, base):
    if not (2 <= base <= 36):
        raise ValueError("Base musi byc miedzy 2 a 36.")

    if num == 0:
        return "0"

    result = ""
    sign = "-" if num < 0 else ""
    num = abs(num)

    while num > 0:
        result = digits[num % base] + result
        num //= base
    return sign + result


counter = 0


# Zadanie 13.1
with open(Path(__file__).parent.joinpath('liczby13.txt'), 'r') as file:
    for line in file:
        line = line.strip()

        w_systemie_dwojkowym = to_base(int(line), 2)
        if w_systemie_dwojkowym.count('0') == w_systemie_dwojkowym.count('1'):
            counter += 1

# Zadanie 13.2
def najwiecej_najwiekszych_cyfr(base: int) -> list:
    najwieksza_cyfra = to_base(base - 1, base)

    najwieksza_ilosc_najwiekszych_cyfr = 0
    potrzebne_cyfry = []

    with open(Path(__file__).parent.joinpath('liczby13.txt'), 'r') as file:

        for line in file:
            line = line.strip()

            ilosc_najwiekszych_cyfr = to_base(int(line), base).count(najwieksza_cyfra)

            potrzebne_cyfry.append((ilosc_najwiekszych_cyfr, line))
            if ilosc_najwiekszych_cyfr > najwieksza_ilosc_najwiekszych_cyfr:
                najwieksza_ilosc_najwiekszych_cyfr = ilosc_najwiekszych_cyfr

    with open(Path(__file__).parent.joinpath('liczby13.txt'), 'r') as file:
        for line in file:
            line = line.strip()

            if to_base(int(line), base).count(najwieksza_cyfra) == najwieksza_ilosc_najwiekszych_cyfr:
                print(line)


# najwiecej_najwiekszych_cyfr(5)
# print('----------------------')
# najwiecej_najwiekszych_cyfr(7)
# print('------------------------')
# najwiecej_najwiekszych_cyfr(13)

kaunt = 0

with open(Path(__file__).parent.joinpath('liczby13.txt'), 'r') as file:
    for line in file:
        line = line.strip()

        liczba_w_systemie = to_base(int(line), 16)
        if len(liczba_w_systemie) % 2 == 0:
            pierwsza_polowa = liczba_w_systemie[:(len(liczba_w_systemie) // 2)]
            druga_polowa = liczba_w_systemie[len(liczba_w_systemie) // 2:]

            if pierwsza_polowa == druga_polowa[::-1]:
                print(line)
        else:
            pierwsza_polowa = liczba_w_systemie[:(len(liczba_w_systemie) // 2)]
            druga_polowa = liczba_w_systemie[len(liczba_w_systemie) // 2 + 1:]

            if pierwsza_polowa == druga_polowa[::-1]:
                print(line)
