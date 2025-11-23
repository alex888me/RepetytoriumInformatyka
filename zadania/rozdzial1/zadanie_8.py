"""
Zadanie 8. Liczby rzymskie

Rzymskim systemem zapisywania liczb opiera się na siedmiu podstawowych znakach: I, V, X, L, C, D, M, co odpowiada
wartościom 1, 5, 10, 50, 100, 500 i 1000. Wartości poszczególnych symboli powstają przez odpowiedni zapis znaków.
Jeśli znak o wartości mniejszej umieszczamy po prawej stronie znaku o wartości większej, oznacza to wartość większą:
VI to 6, XI to 11, DCC to 700. W odwrotnej sytuacji oznacza to wartość mniejszą: IV to 4, XL to 40, CD to 400.

1	2	3	4	5	6	7	8	9	10
I	II	III	IV	V	VI	VII	VIII	IX	X
11	12	13	14	15	16	17	18	19	20
XI	XII	XIII	XIV	XV	XVI	XVII	XVIII	XIX	XX
30	40	50	60	70	80	90	100	200	300
XXX	XL	L	LX	LXX	LXXX	XC	C	CC	CCC
400	500	600	700	800	900	1000	2000
CD	D	DC	DCC	DCCC	CM	M	MM
Zadanie 8.1. Konwerter liczb (0–3 pkt)

Zapis liczb rzymskich różni się bardzo od arabskiego, z tego względu bardzo często są popełniane błędy w przeliczeniach
tych zapisów. Napisz algorytm (np. w postaci listy kroków, w pseudokodzie lub w wybranym języku programowania), który
przetworzy liczbę z zapisu rzymskiego, nie większą niż MMM, na arabski. Pamiętaj o zapisaniu specyfikacji do zadania.

Zadanie 8.2. Konwerter odwrotny (0–2 pkt)

Napisz algorytm, np. w postaci listy kroków, w pseudokodzie lub w wybranym języku programowania, który zamieni liczbę z
zapisu arabskiego, nie większą niż 3000, na rzymski. Pamiętaj o zapisaniu specyfikacji do zadania.
"""

roman_to_decimal_numerals = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

decimal_to_roman = {v : k for k, v in roman_to_decimal_numerals.items()}


def roman_to_decimal(roman_numeral: str) -> int:
    i = 0

    decimal_number = 0
    string_length = len(roman_numeral)

    while i < len(roman_numeral) - 1:
        letter = roman_numeral[i].upper()

        if letter.upper() not in roman_to_decimal_numerals:
            raise ValueError('Nie ma takiego zapisu rzymskiego.')

        if roman_to_decimal_numerals[letter] < roman_to_decimal_numerals[roman_numeral[i + 1]]:
            decimal_number -= roman_to_decimal_numerals[letter]
        else:
            decimal_number += roman_to_decimal_numerals[letter]
        i += 1

    decimal_number += roman_to_decimal_numerals[roman_numeral[-1]]

    return decimal_number

def decimal_to_roman(number: int) -> str:
    roman_numeral = ''

    while number >= 1000:
        roman_numeral += 'M'
        number -= 1000

    if number >= 900:
        roman_numeral += 'CM'
        number -= 900

    if number >= 500:
        roman_numeral += 'D'
        number -= 500

    while number >= 100:
        roman_numeral += 'C'
        number -= 100

    if number >= 90:
        roman_numeral += 'XC'
        number -= 90

    if number >= 50:
        roman_numeral += 'L'
        number -= 50

    while number >= 10:
        roman_numeral += 'X'
        number -= 10

    if number >= 9:
        roman_numeral += 'IX'
        number -= 9

    if number >= 5:
        roman_numeral += 'V'
        number -= 5

    if number >= 4:
        roman_numeral += 'IV'
        number -= 4

    while number > 0:
        roman_numeral += 'I'
        number -= 1

    return roman_numeral


if __name__ == '__main__':
    assert roman_to_decimal('DLXVIII') == 568
    assert roman_to_decimal('XCIX') == 99
    assert roman_to_decimal('IV') == 4

    assert decimal_to_roman(568) == 'DLXVIII'
    assert decimal_to_roman(3000) == 'MMM'
    assert decimal_to_roman(5) == 'V'