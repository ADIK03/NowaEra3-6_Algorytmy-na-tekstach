'''
    (**) Zadanie 12
    Napisz program, który z łańcucha znaków będzie usuwał wszystkie
    samogłoski i zastępował je znakiem podkreślenia (_).
'''

samogloski = "aeiouy"
tekst = input("Podaj tekst: ")
nowy = ""

for i in tekst:
    if i.lower() in samogloski:
        nowy += '_'
    else:
        nowy += i

print(nowy)
