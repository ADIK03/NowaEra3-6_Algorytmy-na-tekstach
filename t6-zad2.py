'''
    (*) Zadanie 2
    Napisz program, który wczyta z klawiatury 10 nazw kolorów i wypisze 
    najdłuższą z nich. Jeśli takich nazw jest więcej, to program powinien 
    wyświetlić nazwę podaną najpóźniej.
'''

N = 10

print("Podaj kolory:")
kolor1 = input()
for i in range(N-1):
    kolor2 = input()
    if len(kolor2) >= len(kolor1):
        kolor1 = kolor2

print("Najdłuższy wyraz:", kolor1)

