"""
Zadanie 14. Liczby Fibonacciego
Ciag liczb Fibonacciego to ciag liczb, w ktorym kolejna wartosc powstaje przez dodanie dwoch poprzedzajacych ja wartosci:
F0 = 0
F1 = 1
Fn = Fn–1 + Fn–2

Zadanie 14.1. Ile liczb? (0–2 pkt)
Ile jest liczb bedacych elementami ciagu Fibonacciego?

Zadanie 14.2. Liczby bliskie (0–3 pkt)
Liczby bliskie Fibonacciego to takie liczby nienalezace do ciagu liczb Fibonacciego, ktore sa polozone w poblizu liczby z tego ciagu.
Dzielimy te liczby na trzy kategorie ±1, ±2 i ±3.
Wypisz liczby posortowane niemalejaco, ktore naleza do poszczegolnych kategorii.

Zadanie 14.3. Pierwsze liczby z ciagu Fibonacciego (0–3 pkt)
Wypisz wszystkie liczby z pliku, ktore sa liczbami pierwszymi nalezacymi do ciagu liczb Fibonacciego. Wartosci posortuj niemalejaco.
"""
from time import process_time
from typing import List


class FibPrime:
    MAX_NUMBER = 10 ** 9

    def __init__(self):
        self.fibbonaci_list = [1, 1]
        while self.fibbonaci_list[-1] < self.MAX_NUMBER:
            self.fibbonaci_list.append(self.fibbonaci_list[-1] + self.fibbonaci_list[-2])

        self.fibbonaci_set = set(self.fibbonaci_list)
        self._input_numbers = []

    def get_input_numbers(self) -> List[int]:
        if not self._input_numbers:
            with open('liczby14.txt', 'r') as file:
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

    def dostac_liczby_w_liscie_i_fibbonaci(self):
        self.liczby_w_liscie_i_fibbonaci = [x for x in self.get_input_numbers() if x in self.fibbonaci_set]

        return self.liczby_w_liscie_i_fibbonaci

    def ile_fibbonaci(self):
        return len(self.liczby_w_liscie_i_fibbonaci)

    def liczby_bliskie(self):
        self.liczby_bliskie_z1 = []
        self.liczby_bliskie_z2 = []
        self.liczby_bliskie_z3 = []

        for i in self.get_input_numbers():
            if (i + 1) in self.fibbonaci_set or (i - 1) in self.fibbonaci_set:
                self.liczby_bliskie_z1.append(i)

            if (i + 2) in self.fibbonaci_set or (i - 2) in self.fibbonaci_set:
                self.liczby_bliskie_z2.append(i)

            if (i + 3) in self.fibbonaci_set or (i - 3) in self.fibbonaci_set:
                self.liczby_bliskie_z3.append(i)

    def liczba_fibbonaci_i_pierwsza(self):
        self.lista_liczb_fibbonaci_i_pierwszych = []
        for i in self.dostac_liczby_w_liscie_i_fibbonaci():
            if self.is_prime_fast(i):
                self.lista_liczb_fibbonaci_i_pierwszych.append(i)

        return self.lista_liczb_fibbonaci_i_pierwszych


fib_primes = FibPrime()

# Zadanie 14.1
fib_primes.dostac_liczby_w_liscie_i_fibbonaci()
print(f"Zadanie 14.1\nIlosc liczb znajdujacych sie w ciagu fibbonaci to {fib_primes.ile_fibbonaci()}\n")

# Zadanie 14.2
fib_primes.liczby_bliskie()
print(f"Zadanie 14.2 opwoiedz\nLiczby w zakresie +- 1: {fib_primes.liczby_bliskie_z1}\nLiczby w zakresie +- 2: {fib_primes.liczby_bliskie_z2}\nLiczby w zakresie +- 3: {fib_primes.liczby_bliskie_z3}\n")

# Zadanie 14.3
print(f"Zadanie 14.3\n{sorted(fib_primes.liczba_fibbonaci_i_pierwsza())}")