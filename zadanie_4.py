"""
Dany jest algorytm, który wyznacza wartość x^n dla zadanych wartosci x >= 0 oraz n >= 0 rekurencycjna metoda szybkiego potegowania.
funkcja oblicz(x, n)
    jeżeli n = 0
        zwróć 1
    jeżeli n = 1
        zwróć x
    jeżeli n mod 2 = 0
        temp ← oblicz(x, n div 2)
        zwróć temp * temp
    w przeciwnym przypadku
        temp ← oblicz(x, (n − 1) div 2)
        zwróć x * temp * temp

Zadanie 4.1. Ile razy? (0–1 pkt)
Dla podanych poniżej wartości wyznacz liczbę wywołań funkcji oblicz.

Zadanie 4.2. Dokonaj modyfikacji (0–3 pkt)
Napisz algorytm w postaci pseudokodu lub w wybranym języku programowania, który powyższą funkcję rekurencyjną zastąpi iteracją.
Podpowiedź: Metoda szybkiego potęgowania iteracyjnego jest nazywana również potęgowaniem binarnym.
"""