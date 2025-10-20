def przestaw_rekurecnja(n: int):
    r = n % 100
    a = r // 10
    b = r % 10
    n = n // 100

    if n > 0:
        w = a + 10 * b + 100 * przestaw_rekurecnja(n)
    else:
        if a > 0:
            w = a + 10 * b
        else:
            w = b
    return w

def przestwa_bez_rekurencji(n: int):
    w = 0
    ilosc_iteracji = 0
    while n > 0:
        r = n % 100
        a = r // 10
        b = r % 10


        if n >= 10:
            w = (b * 10 + a) * (100 ** ilosc_iteracji) + w
        else:
            w = (b * 10 + a) * (100 ** ilosc_iteracji //10) + w

        n = n // 100

        ilosc_iteracji += 1
    return w


if __name__ == '__main__':
    assert przestwa_bez_rekurencji(316498) == 134689
    assert przestwa_bez_rekurencji(43657688) == 34566788
    assert przestwa_bez_rekurencji(154005710) == 145007501
    assert przestwa_bez_rekurencji(998877665544321) == 989786756453412

