"""
Zadanie 7. Analiza algorytmu III

Dany jest algorytm, który wykonuje kompresję danych dla zadanego ciągu znakowego S, składającego się wyłącznie z dużych liter alfabetu angielskiego.
Polecenie wypisz nie powoduje zmiany wiersza, a wypisując zmienną tekstową i liczbową, nie wstawia znaku przerwy między nimi.


d = długość(S)
n = 1
dla i = 0, 1, 2, ..., d − 2
    jeżeli S[i] == S[i+1]
        n = n + 1
    w przeciwnym przypadku
        jeżeli n > 1
            wypisz S[i], n
        w przeciwnym wypadku
            wypisz S[i]
        n = 1
wypisz S[d−1], n


Zadanie 7.1. Wykonaj (0–1 pkt)

Przeanalizuj algorytm i uzupełnij tabelę dla podanych przykładów.
FFFFFFFAAACDMMMM
XXXDAZZZZZZZZZZKAPP

Zadanie 7.2. Co robi? (0–1 pkt)
Czy ten rodzaj jest kompresją stratną czy bezstratną? Odpowiedz i uzasadnij.

Zadanie 7.3. Dekompresja (0–3 pkt)
Wykorzystaj znajomość metody kompresji danych do napisania algorytmu (np. w postaci listy kroków, w pseudokodzie lub w wybranym języku programowania), który dla zadanego skompresowanego tekstu wypisze tekst zdekompresowany.
"""
from string import ascii_uppercase as alphabet
from string import digits

def kompresja(S: str):
    d = len(S)
    n = 1
    result = ''
    for i in range(0, d-1):
        if S[i] == S[i+1]:
            n += 1
        else:
            if n > 2:
                result += f"{S[i]}{n}"
            else:
                while n > 0:
                    result += f"{S[i]}"
                    n -= 1
            n = 1
    result += f"{S[d-1]}{n}"
    return result

def decompression(S: str):
    decompressed_text = ''

    index = 0
    spotted_number = ''
    first_index = 0

    string_length = len(S)
    while index < string_length - 1:
        if (S[index] not in digits) and (S[index + 1] in digits):
            found_letter = S[index]
            found_number = ''

            if index < string_length - 1:
                index += 1
                while S[index] in digits:
                    found_number += S[index]
                    if index < string_length - 1:
                        index += 1
                    else:
                        break
                index -= 1
            decompressed_text += found_letter * int(found_number)
        else:
            decompressed_text += S[index]
        index += 1

    if S[string_length - 1] not in digits:
        decompressed_text += S[string_length - 1]

    return decompressed_text

def is_number_1(S: str) -> bool:
    if 48 <= ord(S) <= 57:
        return True
    else:
        return False

if __name__ == '__main__':
    assert kompresja('FFFFFAAAACDMMMM') == 'F5A4CDM4'
    assert kompresja('XXXDAZZZZZZZZZKAPP') == 'X3DAZ9KAP2'
    assert decompression('A2XYZB3C11B') == 'AAXYZBBBCCCCCCCCCCCB'

    assert is_number_1('5')
    assert not is_number_1('H')