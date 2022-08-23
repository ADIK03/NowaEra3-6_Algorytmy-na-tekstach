'''
    (**) Zadanie 10
    Napisz program, który wyświetli litery występujące jednocześnie w dwóch
    słowach wpisanych z klawiatury. Na przykład dla słów ARKA i BARAK program
    powinien wypisać litery A, K i R.

'''

def Sprawdz(napis, znak):
    for i in napis:
        if i == znak: return True;
    return False

napis1 = input("Podaj pierwsze słowo: ")
napis2 = input("Podaj drugie słowo: ")

for i in range(ord('A'), ord('z')+1):
     znak=chr(i);
     if Sprawdz(napis1, znak) and Sprawdz(napis2, znak):
        print(znak, end=" ")

