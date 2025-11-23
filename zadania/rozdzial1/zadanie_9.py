"""
Zadanie 9. Ciąg arytmetyczny

Ciągiem arytmetycznym nazywamy ciąg liczbowy, w którym każdy wyraz jest sumą wyrazu bezpośrednio go poprzedzającego oraz
ustalonej liczby, zwanej różnicą ciągu.

Ciąg arytmetyczny można również uzależnić od pierwszego elementu i wtedy wzór wyznaczający n-ty wyraz ciągu wygląda
następująco:

an = a1 + (n-1)  * r

Zadanie 9.1. Znajdź ciąg (0–2 pkt)

Z podanych elementów wybierz bez zmieniania ich kolejności te, które utworzą najdłuższy możliwy podciąg, będący ciągiem
arytmetycznym.

 Ciąg                              Wynik        
 --------------------------------  ------------ 
 1 3 4 5 6 7 9 10 11               1 3 5 7 9 11 
 4 7 9 11 14 16 19 20 22 24 27 29               
 2 3 4 6 7 8 9 11 12 13 15

Zadanie 9.2. Wyszukaj najdłuższy (0–4 pkt)

Napisz algorytm w postaci pseudokodu lub w wybranym języku programowania, który w posortowanym rosnąco ciągu liczbowym
wyszuka najdłuższy podciąg tworzący ciąg arytmetyczny.
"""

def dostac_najwieksza_roznice(ciag: list) -> int:
    return ciag[-1] - ciag[0]

def dostac_najmniejsza_roznice(ciag: list) -> int:
    najmniejsza_roznica = ciag[-1]

    dlugosc_ciagu = len(ciag)
    i = dlugosc_ciagu - 1

    while i > 0:
        if (ciag[i] - ciag[i - 1]) < najmniejsza_roznica:
            najmniejsza_roznica = abs(ciag[i] - ciag[i - 1])
        i -= 1

    return najmniejsza_roznica

def znalezienie_najdluzszego_podciagu(ciag: list) -> list:
    i = dostac_najmniejsza_roznice(ciag)
    dlugosc_ciagu = len(ciag)

    wszystkie_ciagi = []

    # i to jest roznica w ciagu
    # j to jest poczatek ciagu
    # k to jest sprawdzenie ciagu

    while i <= dostac_najwieksza_roznice(ciag):
        j = 0
        while j < dlugosc_ciagu - 1:
            k = j + 1
            element = ciag[j]
            nastepny_element = element + i
            nowy_ciag = [ciag[j]]
            while k < dlugosc_ciagu:
                # print(f"Pierwszy element : {element}; Drugi element {nastepny_element} ; Krok {i}")
                if ciag[k] == nastepny_element:
                    nowy_ciag.append(nastepny_element)
                    nastepny_element = nastepny_element + i
                elif ciag[k] > nastepny_element:
                    break
                k += 1
            if len(nowy_ciag) > 1:
                wszystkie_ciagi.append(nowy_ciag)
            j += 1
        i += 1

    # print(wszystkie_ciagi)

    najdluzszy_ciag = []
    indeks_najdluzszego_ciagu = 0
    i = 0
    while i < len(wszystkie_ciagi):
        if len(wszystkie_ciagi[i]) > len(najdluzszy_ciag):
            indeks_najdluzszego_ciagu = i
            najdluzszy_ciag = wszystkie_ciagi[i]
        i += 1
    print(najdluzszy_ciag)

    return najdluzszy_ciag

ciag1 = [1, 3, 4, 5, 6, 7, 9, 10, 11]
ciag2 = [4, 7, 9, 11, 14, 16, 19, 20, 22, 24, 27, 29]
ciag3 = [2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 15]

if __name__ == '__main__':
    assert znalezienie_najdluzszego_podciagu(ciag1) == [1, 3, 5, 7, 9, 11]
    assert znalezienie_najdluzszego_podciagu(ciag2) == [4, 9, 14, 19, 24, 29]
    assert znalezienie_najdluzszego_podciagu(ciag3) == [7, 9, 11, 13, 15]