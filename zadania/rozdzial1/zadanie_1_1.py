"""
Zadanie 1.1. Scalanie ciągów posortowanych (0–3 pkt)
Napisz algorytm (np. w postaci listy kroków, w pseudokodzie lub w wybranym języku programowania),
który scali dwa posortowane ciągi liczbowych w jeden posortowany ciąg. Pamiętaj o zapisaniu specyfikacji do zadania.

Write an algorithm (for example, in the form of a list of steps, pseudocode, or in a chosen programming language)
that merges two sorted numerical sequences into a single sorted sequence. Remember to include the task specification.

i=j=k=1
dopóki (k<=n+m oraz i<=n oraz j<=m)
    jeżeli tab1[i] < tab2[j]
        scalenie[k] = tab1[i]
        i=i+1
    w przeciwnym przypadku
        scalenie[k] = tab2[j]
        j=j+1
    k=k+1

jeżeli k<=n+m
    jeżeli j<=m
        dopóki j<=m
            scalenie[k] = tab2[j]
            j=j+1
            k=k+1
    w przeciwnym przypadku
        dopóki i<=n
            scalenie[k] = tab1[i]
            i=i+1
            k=k+1

wypisz scalenie
"""

from typing import List, Callable


def merge_sorted_numerical_lists_option1(list1: List[int], list2: List[int]) -> List[int]:
    """This is the shortest and the simplest implementation"""
    return sorted(list1 + list2)


def merge_sorted_numerical_lists_option2(tab1: List[int], tab2: List[int]) -> List[int]:
    """This is implemented based on pseudocode"""
    scalenie = []
    n = len(tab1)
    m = len(tab2)
    for index in range(n + m):  # it is trick to use scalenie[k] = ...
        scalenie.append(None)

    i = j = k = 1
    while (k <= n + m) and (i <= n) and (j <= m):
        if tab1[i - 1] < tab2[j - 1]:
            scalenie[k - 1] = tab1[i - 1]  # scalenie[k - 1] -1 is used as python list starts from 0 not 1
            i = i + 1
        else:
            scalenie[k - 1] = tab2[j - 1]
            j = j + 1
        k = k + 1

    if k <= n + m:
        if j <= m:
            while j <= m:
                scalenie[k - 1] = tab2[j - 1]
                j = j + 1
                k = k + 1
        else:
            while i <= n:
                scalenie[k - 1] = tab1[i - 1]
                i = i + 1
                k = k + 1

    return scalenie


def merge_sorted_numerical_lists_option3(list1: List[int], list2: List[int]) -> List[int]:
    """This is optimized implementation"""
    sorted_list = []
    list1_index = 0
    list2_index = 0
    list1_length = len(list1)
    list2_length = len(list2)
    while list1_index <= list1_length:
        if list1_index >= list1_length:
            if list2_index <= list2_length:
                sorted_list.extend(list2[list2_index:])

            break

        if list2_index >= list2_length:
            if list1_index <= list1_length:
                sorted_list.extend(list1[list1_index:])

            break

        if list1[list1_index] < list2[list2_index]:
            sorted_list.append(list1[list1_index])
            list1_index += 1
        elif list1[list1_index] == list2[list2_index]:
            sorted_list.append(list1[list1_index])
            sorted_list.append(list2[list2_index])
            list2_index += 1
            list1_index += 1
        else:
            sorted_list.append(list2[list2_index])
            list2_index += 1

    return sorted_list


def test_merge_sorted_lists(func_to_test: Callable):
    assert func_to_test([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert func_to_test([4, 5, 6], [1, 2, 3]) == [1, 2, 3, 4, 5, 6]
    assert func_to_test([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert func_to_test([1, 2, 6], [3, 4, 5]) == [1, 2, 3, 4, 5, 6]
    assert func_to_test([], [1, 2, 3]) == [1, 2, 3]
    assert func_to_test([1, 2, 3], []) == [1, 2, 3]
    assert func_to_test([], []) == []
    assert func_to_test([1, 2, 2, 3, 4], [2, 3]) == [1, 2, 2, 2, 3, 3, 4]


if __name__ == '__main__':
    for merge_lists in [
        merge_sorted_numerical_lists_option1,
        merge_sorted_numerical_lists_option2,
        merge_sorted_numerical_lists_option3,
    ]:
        test_merge_sorted_lists(merge_lists)
