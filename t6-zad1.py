'''
    (*) Zadanie 1
    Napisz program, który wczyta z klawiatury nazwę miejscowości (bez spacji) 
    i wypisze co drugą jej literę. Litery powinny być rozdzielone spacjami.
'''

miejscowosc = input("Podaj nazwę miejscowości: ")

# pętla while
i = 1
while i < len(miejscowosc):
    print(miejscowosc[i], end=" ")
    i = i + 2

# pętla for

miejscowosc = input("Podaj nazwę miejscowości: ")

for i in range(1, len(miejscowosc), 2):
    print(miejscowosc[i], end=" ")

