'''
    Ćwiczenie 8
    Zapisz kod źródłowy programu Usuwanie powtórzeń i sprawdź działanie programu
    dla różnych danych wejściowych.
'''

N = 20

wynik = []
i = 1
nowy = input()
wynik.append(nowy)

stary = nowy
nowy = input()

while nowy != "***" and i < N: 
    if nowy != stary:
        i = i + 1
        wynik.append(nowy)
    stary = nowy
    nowy = input()

for j in range(i):
    print(wynik[j])