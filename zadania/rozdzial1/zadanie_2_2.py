"""
Zadanie 2. Liczby pierwsze
Liczbą pierwszą nazywamy liczbę, która ma dokładnie dwa dzielniki całkowite, 1 i siebie samą.
Liczbą B-superpierwszą nazywamy taką liczbę pierwszą, w której suma cyfr zapisu dziesiętnego
jest również liczbą pierwszą.

Zadanie 2.2. B-superpierwsze w zakresie (0–3 pkt)
Wykorzystaj funkcję z zadania 2.1. i napisz algorytm (np. w postaci listy kroków, w pseudokodzie
lub w wybranym języku programowania), który wypisze wszystkie liczby B-superpierwsze w zakresie od 1 do 100000.
Pamiętaj o zapisaniu specyfikacji zadania.

Using the function from Task 2.1, write an algorithm (e.g., in the form of a step-by-step list, pseudocode,
or in a programming language of your choice) that outputs all B-superprime numbers in the range from 1 to 100,000.
Remember to include a specification for the task.
"""
from typing import List
from math import trunc
from math import ceil

liczba = 123123


def is_prime(x: int) -> bool:
    if x < 1:
        raise ValueError('Ta liczba nie jest naturalna lub jest mniejsza od 2.')
    for i in range(x // 2, 1, -1):
        if x % i == 0:
            return False
    return True


def to_digits(liczba: int):
    lista_cyfr = []
    while liczba > 10:
        czesc_dziesietna = trunc(liczba / 10)
        ostatnia_cyfra_liczby = liczba - czesc_dziesietna * 10

        lista_cyfr.append(ostatnia_cyfra_liczby)
        liczba = czesc_dziesietna
    lista_cyfr.append(liczba)

    return lista_cyfr


def sum_digits(liczba: list):
    lista_cyfr = to_digits(liczba)
    x = 0
    for i in lista_cyfr:
        x += i
    return x


def wypisac_superpierwsze():
    for i in range(2, 10001):
        if is_prime(i) and is_prime(sum_digits(i)):
            print(i)


wypisac_superpierwsze()

if __name__ == '__main__':
    assert is_prime(13)
    assert not is_prime(22)
    try:
        is_prime(0)
        raise Exception('Test failed')
    except ValueError as error:
        pass

    assert sum_digits(123123) == 12
    assert to_digits(4321) == [1, 2, 3, 4]
