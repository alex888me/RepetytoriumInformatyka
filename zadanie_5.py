"""
Dany jest algorytm, który wykonuje analizę dwóch ciągów znakowych. Dokonaj analizy algorytmu i rozwiąż poniższe zadania.

Dane:
s1, s2 – ciągi znakowe
m, n – zmienne przechowujące ilość znaków, odpowiednio, ciągów s1 i s2
maxi – długość podciągu
t[r][r] – dwuwymiarowa tablica pomocnicza o rozmiarze r = max(n, m)

Algorytm:
wczytaj s1, s2
m = długość ciągu s1
n = długość ciągu s2
maxi = 0, ind = 0
r = max(n, m)
dla i = 0,1,2 do r − 1
    t[0][i] = t[i][0] = 0
dla i = 1,2,3 do m
    dla j = 1,2,3 do n
        jeżeli s1[i−1] != s2[j−1]
            t[i][j] = 0
        w przeciwnym przypadku
            t[i][j] = t[i−1][j−1] + 1
            jeżeli t[i][j] > maxi
                maxi = t[i][j]
                ind = i;
wypisz maxi
jeżeli maxi != 0
    dla i = 0,1,2 do maxi − 1
        wypisz bez zmiany wiersza s1[ind + i − maxi]


Zadanie 5.1. Wynik działania (0–2 pkt)
Przeanalizuj algorytm i uzupełnij poniższą tabelę.

Dane wejściowe	| maxi |	Wypisany ciąg znaków
----------------|------|-------------------------
s1 = hdjdusyhd  |      |
s2 = aosjdusyaa |      |
----------------|------|-------------------------
s1 = opona      |      |
s2 = piasek     |      |


Zadanie 5.2. Ile razy? (0–1 pkt)
Określ, ile razy wykona się instrukcja jeżeli s1[i−1] != s2[j−1].


Zadanie 5.3. Złożoność (0–1 pkt)
Określ złożoność pamięciową algorytmu.
"""

def algorytm(s1: str, s2: str):
    m = len(s1)
    n = len(s2)
    wypisane = ''
    maxi = ind = 0
    r = max(n, m)
    t = [[0 for x in range(r)] for i in range(r)]
    for i in range(0, r-1):
        t[0][i] = t[i][0] = 0
    for i in range(m):
        for j in range(n):
            if s1[i-1] != s2[j-1]:
                t[i][j] = 0
            else:
                t[i][j] = t[i-1][j-1] + 1
                if t[i][j] > maxi:
                    maxi = t[i][j]
                    ind = i

    if maxi != 0:
        for i in range(maxi):
            wypisane += s1[ind+i-maxi]

    return (maxi, wypisane)
if __name__ == '__main__':
    pass
    assert algorytm('hdjdusyhd', 'aosjdusyaa') == (5, 'jdusy')
    assert algorytm('opona', 'pisaek') == (1, 'a')