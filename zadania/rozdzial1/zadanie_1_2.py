"""
Zadanie 1.2. Scalanie unikatów (0–3 pkt)
Napisz algorytm (np. w postaci listy kroków, w pseudokodzie lub w wybranym języku programowania),
który scali dwa dowolne ciągi liczb całkowitych w jeden ciąg zawierający tylko unikalne (niepowtarzające się)
wartości. Pamiętaj o zapisaniu specyfikacji do zadania.

Write an algorithm (e.g., in the form of a step-by-step list, pseudocode, or in a programming language of your choice)
that merges two arbitrary sequences of integers into a single sequence containing only unique (non-repeating) values.
 Remember to include a specification for the task."
"""
from typing import List, Callable


def scalanie_bez_dublikatow_1(ciag1: List[int], ciag2: List[int]):
    ciag3 = []

    for element in ciag1:
        if element not in ciag3:
            ciag3.append(element)

    for element in ciag2:
        if element not in ciag3:
            ciag3.append(element)

    return ciag3


def scalanie_bez_dublikatow_2(ciag1: List[int], ciag2: List[int]) -> List[int]:
    return list(set(ciag1 + ciag2))


def scalanie_bez_dublikatow_3(ciag1: List[int], ciag2: List[int]):
    ciag3 = []

    for element in ciag1:
        is_element_in_list = False
        for x in ciag3:
            if element == x:
                is_element_in_list = True
        if not is_element_in_list:
            ciag3.append(element)

    for element in ciag2:
        is_element_in_list = False
        for x in ciag3:
            if element == x:
                is_element_in_list = True
        if not is_element_in_list:
            ciag3.append(element)

    return ciag3


def scalanie_bez_dublikatow_4(tab1: List[int], tab2: List[int]):
    """Rekomendowane rozwiazanie z pesudokodu"""
    tab1.sort()
    tab2.sort()

    n = len(tab1)
    m = len(tab2)

    scalenie = [None for i in range(n + m)]

    i = j = k = 1
    while (k <= n + m) and (i <= n) and (j <= m):
        if tab1[i - 1] == tab2[j - 1]:
            scalenie[k - 1] = tab1[i - 1]
            while (i <= n) and (tab1[i - 1] == scalenie[k - 1]):
                i += 1
            while (j <= m) and (tab2[j - 1] == scalenie[k - 1]):
                j += 1
            k += 1
        else:
            if tab1[i - 1] < tab2[j - 1]:
                scalenie[k - 1] = tab1[i - 1]
                i += 1
            else:
                scalenie[k - 1] = tab2[j - 1]
                j += 1
            k += 1
    if k <= n + m:
        if j <= m:
            scalenie[k - 1] = tab2[j - 1]
            j += 1
            k += 1
        else:
            while i <= n:
                if scalenie[k - 2] != tab1[i - 1]:
                    scalenie[k - 1] = tab1[i - 1]
                i += 1
                k += 1

    return [element for element in scalenie if element is not None]

def scalanie_bez_dublikatow_4(tab1: List[int], tab2: List[int]):


def test_scalanie_bez_dublikatow(func_to_test: Callable):
    assert sorted(func_to_test([4, 3, 1, 2, 2, 3, 4], [2, 3, 3])) == [1, 2, 3, 4]


if __name__ == '__main__':
    for merge_lists in [
        scalanie_bez_dublikatow_1,
        scalanie_bez_dublikatow_2,
        scalanie_bez_dublikatow_3,
        scalanie_bez_dublikatow_4,
    ]:
        test_scalanie_bez_dublikatow(merge_lists)

# print(scalanie_bez_dublikatow_1([4, 3, 1, 2, 2, 3, 4], [2, 3, 3]))
