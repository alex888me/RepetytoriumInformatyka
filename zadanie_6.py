"""
Zadanie 6. Ciąg liczbowy
Ciąg Fibonacciego to ciąg liczb, w których dwie pierwsze wartości są równe 1, a kolejne oblicza się ze
wzoru F[i−2] + F[i−1]. Oznacza to, że każdy następny wyraz ciągu jest sumą dwóch poprzednich.

Tabela przykładowych wartości (F₁ … F₁₀):
1, 1, 2, 3, 5, 8, 13, 21, 34, 55

Bardzo często do obliczeń wykorzystuje się wartość 0 jako wartość początkową F₀,
wtedy ciąg liczb Fibonacciego definiuje się wzorem rekurencyjnym:

     0           dla 𝑥=0
𝐹𝑥={ 1           dla 𝑥=1
     𝐹𝑥−1 + 𝐹𝑥−2 dla 𝑥 ≥2


Zadanie 6.1. Czy należy do ciągu? (0–3 pkt)
Na podstawie definicji ciągu Fibonacciego napisz algorytm (np. w postaci listy kroków, w pseudokodzie lub w
wybranym języku programowania), który sprawdzi, czy podana przez użytkownika liczba należy do ciągu liczb Fibonacciego.
Jako wynik powinien pojawić się komunikat TAK, jeśli liczba należy do ciągu liczb Fibonacciego, lub NIE,
jeśli nie należy. Pamiętaj o zapisaniu specyfikacji do zadania.

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