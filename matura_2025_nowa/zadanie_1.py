'''
Dana jest rekurencyjna funkcja przestaw, której parametrem jest nieujemna liczba całkowita:

przestaw(n):
    r  n mod 100
    a  r div 10
    b  r mod 10
    n  n div 100
    jeżeli n > 0
        w  a + 10 * b + 100 * przestaw(n)
    w przeciwnym razie
        jeżeli a > 0
            w  a + 10 * b
        w przeciwnym razie
            w  b
    wynikiem jest w

Uwaga:
Operator mod oznacza resztę z dzielenia, natomiast div – część całkowitą z dzielenia.
'''

def przestaw_wrapper(n: int):
    liczba_wylowan = 0

    def przestaw(n: int):
        nonlocal liczba_wylowan
        liczba_wylowan += 1
        r = n % 100
        a = r // 10
        b = r % 10
        n = n // 100

        if n > 0:
            w = a + 10 * b + 100 * przestaw(n)
        else:
            if a > 0:
                w = a + 10 * b
            else:
                w = b
        return w

    return przestaw(n), liczba_wylowan


if __name__ == '__main__':
    assert przestaw_wrapper(316498) == (134689, 3)
    assert przestaw_wrapper(43657688) == (34566788, 4)
    assert przestaw_wrapper(154005710) == (145007501, 5)
    assert przestaw_wrapper(998877665544321) == (989786756453412, 8)