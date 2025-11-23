"""
Zadanie 6.2. Proste szyfrowanie (0–4 pkt)
Szyfrem podstawieniowym nazywamy taki szyfr, w którym literę tekstu jawnego zastępujemy inną literą lub ciągiem znaków.
Ciąg liczb Fibonacciego możemy wykorzystać jako klucz szyfrowania, który pozwoli nam na zmianę kolejnych liter na inne.
Nasze szyfrowanie będzie opierało się na zasadzie, zgodnie z którą kolejna litera tekstu zaszyfrowanego będzie
powstawała przez podstawienie za literę tekstu jawnego litery oddalonej od niej o kolejną wartość z ciągu Fibonacciego.
Ponieważ liter do zaszyfrowania może być bardzo dużo, a liczby z ciągu bardzo szybko rosną, dlatego do obliczania
kolejnych wartości będziemy wykorzystywać własności arytmetyki modularnej.

F(x)=(F(x−1)+F(x−2))modn

Przykład:
Tekst jawny: KATASTROFA
Klucz: Kolejne wartości ciągu Fibonacciego mod 13 (mod – reszta z dzielenia)
11 2 3 5 8 0 8 8 3
Tekst zaszyfrowany: LBVDXBRWND

Napisz algorytm (np. w postaci listy kroków, w pseudokodzie lub w wybranym języku programowania),
który dla podanego tekstu jawnego, składającego się tylko z dużych znaków alfabetu angielskiego,
i wartości n, dzielnika w arytmetyce modularnej, wyznaczy tekst zaszyfrowany. Wszystkie inne znaki
(spacje i znaki diakrytyczne) przy szyfrowaniu się pomija, a w wyniku otrzymujemy jedynie ciąg liter.
Pamiętaj o zapisaniu specyfikacji do zadania.

Zadanie 6.3. Szyfrowanie – analiza (0–1 pkt)
Dla podanej w zadaniu 6.2 metody szyfrowania uzupełnij poniższą tabelę poprawnymi rozwiązaniami.
Tekst jawny	                     | n  | Tekst zaszyfrowany
DOSTAWA W CZWARTEK               | 20 |
KURIER PRZYJEDZIE O SIEDEMNASTEJ | 17 |
"""
from string import ascii_uppercase as uppercase_alphabet


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


fibbonaci_list = fibbonaci_loop(len(uppercase_alphabet) + 1)


def fibbonaci(n: int):
    if not isinstance(n, int):
        raise TypeError
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibbonaci_list[n]


def zaszyfrowac_wiadomosc(message: str, n: int):
    if not isinstance(message, int) and not isinstance(n, int):
        raise TypeError('Nie ten typ wiadomosci lub n')

    wiadomosc_tylko_litery = ''
    wiadomosc_zaszyfromwana = ''

    # Usuniecie znakow
    for letter in message:
        if letter.upper() in uppercase_alphabet:
            wiadomosc_tylko_litery += letter.upper()

    for i in range(len(wiadomosc_tylko_litery)):
        jaki_fibbonaci = fibbonaci(i + 1) % n
        znak_zamieniony = ((uppercase_alphabet.index(wiadomosc_tylko_litery[i]) + jaki_fibbonaci)
                           % len(uppercase_alphabet))
        wiadomosc_zaszyfromwana += uppercase_alphabet[znak_zamieniony]
    return wiadomosc_zaszyfromwana


if __name__ == '__main__':
    assert zaszyfrowac_wiadomosc('KATASTROFA', 13) == 'LBVDXBRWND'
    assert zaszyfrowac_wiadomosc('DOSTAWA W CZWARTEK', 20) == 'EPUWFENXQOFEEKOR'
    assert zaszyfrowac_wiadomosc('KURIER PRZYLECI O SIEDEMNASTEJ', 17) == 'LVTLJZCVZCPMOLDTYETUBBMBXRJ'
