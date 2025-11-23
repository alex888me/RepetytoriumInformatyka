"""
Dany jest ciag liczbowy an liczb naturalnych. Ciag bn liczb naturalnych jest tworzony w nastepujacy sposob:
b1 = 1
Jezeli an + bn > bn + 1, to bn+1 = bn + 1, w przeciwnym wypadku bn+1 = 1

Przyklad
 n  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20 
 -  -  -  -  -  -  -  -  -  -  --  --  --  --  --  --  --  --  --  --  -- 
 a  2  3  1  4  5  2  7  8  3  2   5   7   3   8   9   5   2   6   7   1  
 b  1  2  3  1  4  1  2  3  4  1   5   1   4   5   1   2   1   2   1   2  


/_______________________________________________________________________________/
/_______________________________________________________________________________/


Zadanie 10.1 Brakujace wyrazy ciagu (0-1 pkt)

Dla ciagu an uzupelnij brakujace  wyrazy ciagu bn

 n  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20 
 -  -  -  -  -  -  -  -  -  -  --  --  --  --  --  --  --  --  --  --  -- 
 a  2  3  1  4  5  2  7  8  3  2   5   7   3   8   9   5   2   6   7   1  
 b  1  2  3  1  4  1  2  3  4  1   5   1   4   5   1   2   1   2   1   2  


/_______________________________________________________________________________/
/_______________________________________________________________________________/


Zadanie 10.2 Najdluzszy ciag (0-2 pkt)
Znajdz podciag ciagu an ktorego kolejne wyrazy sa rosnace tzn. an < ak+1

Uzupelnij tabele:

 Ciąg (aₙ)             Liczba wyrazów najdłuższego podciągu  Wyrazy podciągu 
 --------------------  ------------------------------------  --------------- 
 2, 3, 3, 5, 7, 8, 4   4                                     3, 5, 7, 8      
 1, 5, 6, 5, 8, 10, 3                                                        
 2, 2, 4, 3, 2, 3, 3


/_______________________________________________________________________________/
/_______________________________________________________________________________/


Zadanie 10.3. Algorytm (0–2 pkt)

Napisz algorytm w postaci pseudokodu lub w wybranym języku programowania, który w zadanym ciągu liczb całkowitych (A[1..n]) znajduje najdłuższy podciąg kolejnych elementów, w którym każdy kolejny wyraz jest większy od poprzedniego (czyli spełnia warunek aₖ < aₖ₊₁).
Można założyć, że jest jeden taki podciąg. Algorytm powinien zwracać indeks pierwszego i ostatniego wyrazu podciągu.

Uwaga:
Twój algorytm może używać wyłącznie zmiennych przechowujących liczby całkowite oraz operować wyłącznie na liczbach całkowitych. W zapisie możesz wykorzystać tylko operacje arytmetyczne: dodawanie, odejmowanie, mnożenie, dzielenie, resztę z dzielenia oraz porównywanie liczb, instrukcje sterujące, przypisania i zbiory funkcji oraz operatorów innych niż wymienione nie wymienione. Zabronione jest używanie funkcji gotowych oraz operatorów innych niż wymienione.

Specyfikacja:

Dane wejściowe:
A[1..n] – tablica liczb naturalnych

Dane wyjściowe:
a – liczba naturalna, indeks pierwszego wyrazu podciągu
k – liczba naturalna, długość najdłuższego rosnącego podciągu

 Wejście                        Wyjście 
 -----------------------------  ------- 
 5 4 7 9 10 13 2 3 6 8 8 2 3 1  2 5
"""

ciag_an = [3, 5, 1, 2, 4, 7, 8, 9, 2, 2, 2, 3, 6, 1, 6, 8, 2, 5, 7, 7]

def brakujace_wyrazy_bn(ciag):
    i = 0
    ciag_b = [1]

    for i in range(len(ciag) - 1):
        if ciag[i + 1] >  ciag[i]:
            ciag_b.append(ciag_b[i] + 1)
        else:
            ciag_b.append(1)

    print(ciag, '\n', ciag_b, sep='')

def algorytm(ciag):
    i = 0
    czy_to_jest_poczatek = 0

    tymczasowy_indeks_pocateku_ciagu = 0
    tymczasowa_dlugosc_ciagu = 0

    poczatkowy_indeks_najluzszego_ciagu = 0
    dlugosc_najdluszego_ciagu = 0

    while i < len(ciag) - 1:
        teraz_to = ciag[i]
        nastepny_wyraz = ciag[i + 1]
        if ciag[i] < ciag[i + 1]:
            if czy_to_jest_poczatek == 0:
                czy_to_jest_poczatek = 1
                tymczasowy_indeks_pocateku_ciagu = i
                tymczasowa_dlugosc_ciagu += 1
            else:
                tymczasowa_dlugosc_ciagu += 1
        else:
            czy_to_jest_poczatek = 0
            if tymczasowa_dlugosc_ciagu > dlugosc_najdluszego_ciagu:
                poczatkowy_indeks_najluzszego_ciagu = tymczasowy_indeks_pocateku_ciagu
                dlugosc_najdluszego_ciagu = tymczasowa_dlugosc_ciagu
            tymczasowy_indeks_pocateku_ciagu = 0
            tymczasowa_dlugosc_ciagu = 0

        i += 1

    return (poczatkowy_indeks_najluzszego_ciagu + 1, dlugosc_najdluszego_ciagu + 1)


brakujace_wyrazy_bn(ciag_an)

if __name__ == '__main__':
    assert algorytm([5, 4, 7, 9, 10, 13, 2, 3, 6, 8, 8, 2, 3, 1]) == (2, 5)