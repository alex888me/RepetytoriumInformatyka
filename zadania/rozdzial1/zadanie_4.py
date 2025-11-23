"""
Dany jest algorytm, który wyznacza wartość x^n dla zadanych wartosci x >= 0 oraz n >= 0
rekurencycjna metoda szybkiego potegowania.
funkcja oblicz(x, n)
    jeżeli n = 0
        zwróć 1
    jeżeli n = 1
        zwróć x
    jeżeli n mod 2 = 0
        temp ← oblicz(x, n div 2)
        zwróć temp * temp
    w przeciwnym przypadku
        temp ← oblicz(x, (n − 1) div 2)
        zwróć x * temp * temp

Zadanie 4.1. Ile razy? (0–1 pkt)
Dla podanych poniżej wartości wyznacz liczbę wywołań funkcji oblicz.
x | n
2 | 10
7 | 13
4 | 16
3 | 35

Zadanie 4.2. Dokonaj modyfikacji (0–3 pkt)
Napisz algorytm w postaci pseudokodu lub w wybranym języku programowania,
który powyższą funkcję rekurencyjną zastąpi iteracją.
Podpowiedź: Metoda szybkiego potęgowania iteracyjnego jest nazywana również potęgowaniem binarnym.
"""


# liczba_wywolan = 0


def obliczenie_wylowan(x, n) -> int:
    liczba_wywolan = 0

    def oblicz(x, n):
        nonlocal liczba_wywolan
        liczba_wywolan += 1
        if n == 0:
            return 1
        if n == 1:
            return x

        if n % 2 == 0:
            temp = oblicz(x, n // 2)
            return temp * temp
        else:
            temp = oblicz(x, (n - 1) // 2)
            return x * temp * temp

    oblicz(x, n)
    return liczba_wywolan


def oblicz_iteracja(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x

    temp = 1
    for i in range(n):
        temp *= x

    return temp


def oblicz_iteracja_2(x, n):
    w = 1
    while n > 0:
        if n % 2 == 1:
            w *= x
        x *= x
        n //= 2
    return w


if __name__ == '__main__':
    podane_wartosci = {
        (2, 10): 4,
        (7, 13): 4,
        (4, 16): 5,
        (3, 35): 6,
    }

    for k, v in podane_wartosci.items():
        assert obliczenie_wylowan(k[0], k[1]) == v
    assert oblicz_iteracja(2, 10) == 1024
    assert oblicz_iteracja_2(2, 10) == 1024
