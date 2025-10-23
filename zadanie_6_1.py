"""
Zadanie 6. Ciąg liczbowy
Ciąg Fibonacciego to ciąg liczb, w których dwie pierwsze wartości są równe 1, a kolejne oblicza się ze
wzoru F[i−2] + F[i−1]. Oznacza to, że każdy następny wyraz ciągu jest sumą dwóch poprzednich.

Tabela przykładowych wartości (F₁ … F₁₀):
1, 1, 2, 3, 5, 8, 13, 21, 34, 55

Bardzo często do obliczeń wykorzystuje się wartość 0 jako wartość początkową F₀,
wtedy ciąg liczb Fibonacciego definiuje się wzorem rekurencyjnym:

     0           dla 𝑥=0
𝐹𝑥={ 1           dla 𝑥=1
     𝐹𝑥−1 + 𝐹𝑥−2 dla 𝑥 ≥2


Zadanie 6.1. Czy należy do ciągu? (0–3 pkt)
Na podstawie definicji ciągu Fibonacciego napisz algorytm (np. w postaci listy kroków, w pseudokodzie lub w
wybranym języku programowania), który sprawdzi, czy podana przez użytkownika liczba należy do ciągu liczb Fibonacciego.
Jako wynik powinien pojawić się komunikat TAK, jeśli liczba należy do ciągu liczb Fibonacciego, lub NIE,
jeśli nie należy. Pamiętaj o zapisaniu specyfikacji do zadania.
"""
from sys import maxsize


def fibbonaci_recursion(n: int):
    if not isinstance(n, int) or n < 0:
        raise ValueError('Liczba jest mniejsza od 0 lub nie jest typu int')
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    elif n >= 2:
        return fibbonaci_recursion(n - 1) + fibbonaci_recursion(n - 2)


def fibbonaci_loop(n: int):
    if not isinstance(n, int) or n < 0:
        raise ValueError('Liczba jest mniejsza od 0 lub nie jest typu int')
    elif n == 0:
        return 0
    elif n == 1:
        return 1

    fibbonaci_list = [0, 1]
    for x in range(2, n + 1):
        fibbonaci_list.append(fibbonaci_list[x - 1] + fibbonaci_list[x - 2])
    return fibbonaci_list


def is_fibbonaci(n: int):
    if not isinstance(n, int) or n < 0:
        raise ValueError('Liczba musi byc 0 lub wieksza, lub jest to nie typ int.')
    if n > 7540113804746346429:
        raise ValueError('Liczba jest za duza')
    fibbonaci_list = fibbonaci_loop(92)

    if n in fibbonaci_list:
        return True
    else:
        return False

if __name__ == '__main__':
    assert is_fibbonaci(5)
    assert is_fibbonaci(34)
    assert is_fibbonaci(55)
    assert is_fibbonaci(4660046610375530309)
    assert not is_fibbonaci(99194853094755491)
    assert not is_fibbonaci(10)
