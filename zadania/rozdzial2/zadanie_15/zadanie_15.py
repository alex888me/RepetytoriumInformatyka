"""
Zadanie 15. Liczby pierwsze
Matematycy badali liczby i odkryli, ze niektore sa podzielne jedynie przez 1 lub przez siebie. Nazwali je pierwszymi.

Zadanie 15.1. Ile liczb pierwszych? (0–2 pkt)
Podaj, ile liczb zawartych w pliku jest pierwszymi.

Zadanie 15.2. Liczby B-superpierwsze (0–4 pkt)
Liczby superpierwsze to liczby, ktore sa pierwsze i ktorych suma cyfr jest liczba pierwsza.
Liczby B-superpierwsze to liczby, ktore w zapisie binarnym maja liczbe jedynek rowna liczbie pierwszej.
Wypisz liczby posortowane rosnaco.

Zadanie 15.3 Liczby bliznacze
Liczby blizniace, to takie dwie liczby piwersze, ktorych roznica wynosi 2. Podaj pary liczb bliznaczych znajdujacych sie w pliku.
"""

class LiczbyPierwsze():
    def __init__(self):
        self._input_numbers = []

    def get_input_numbers(self):
        if not self._input_numbers:
            with open('liczby15.txt', 'r') as file:
                for line in file:
                    line = line.strip()
                    self._input_numbers.append(int(line))

        return self._input_numbers

    @staticmethod
    def is_prime_fast(n: int) -> bool:
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False

        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6

        return True

    def ile_pierwszych(self):
        self.ilosc_liczb_pierwszych = 0

        for i in self.get_input_numbers():
            if self.is_prime_fast(i):
                self.ilosc_liczb_pierwszych += 1

        return self.ilosc_liczb_pierwszych

    def suma_cyfr(self, liczba) -> int:
        liczba_jako_str = str(liczba)
        suma_cyfr = 0

        for cyfra in liczba_jako_str:
            suma_cyfr += int(cyfra)

        return suma_cyfr

    def to_base(self, n: int, base: int) -> str:
        if n == 0:
            return 0
        if n == 1:
            return 1

        digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        result = ''
        sign = '-' if n < 0 else ''
        n = abs(n)

        while n > 0:
            result = digits[n % base] + result
            n //= base

        return result

    def liczby_superpierwsze(self):
        self.lista_liczb_superpierwszych = []

        for i in self.get_input_numbers():
            if self.is_prime_fast(i):
                if self.is_prime_fast(self.suma_cyfr(i)):
                    if self.is_prime_fast(self.suma_cyfr(self.to_base(i, 2))):
                        self.lista_liczb_superpierwszych.append(i)

        return sorted(self.lista_liczb_superpierwszych)

    def liczby_bliznacze(self):
        litsa_liczb_bliznaczych = []
        lokalna_lista_liczb_pierwszych = []

        for i in self.get_input_numbers():
            if self.is_prime_fast(i):
                lokalna_lista_liczb_pierwszych.append(i)

        lokalna_lista_liczb_pierwszych = sorted(list(set(lokalna_lista_liczb_pierwszych)))

        for i in range(len(lokalna_lista_liczb_pierwszych) - 1):
            if lokalna_lista_liczb_pierwszych[i+1] - 2 == lokalna_lista_liczb_pierwszych[i]:
                litsa_liczb_bliznaczych.append((lokalna_lista_liczb_pierwszych[i], lokalna_lista_liczb_pierwszych[i+1]))

        return litsa_liczb_bliznaczych

liczby_pierwsze = LiczbyPierwsze()

# Zadanie 15.1

print(f"Zadanie 15.1\n"
      f"Liczb pierwszych jest {liczby_pierwsze.ile_pierwszych()}\n\n--------")

print(f"Zadaine 15.2\n"
      f"Liczby superpierwsze to {liczby_pierwsze.liczby_superpierwsze()}\n\n--------")

print(f"Zadanie 15.3\n"
      f"Liczby bliznacze to {liczby_pierwsze.liczby_bliznacze()}")