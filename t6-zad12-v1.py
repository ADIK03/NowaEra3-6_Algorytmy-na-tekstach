'''
    (**) Zadanie 12
    Napisz program, który z łańcucha znaków będzie usuwał wszystkie
    samogłoski i zastępował je znakiem podkreślenia (_).

'''

def CzySamogloska(lit):
    if lit >= 'a':
        lit = chr(ord(lit)-32)
    if lit=='A' or lit=='E' or lit=='I' or lit=='O' or lit=='U' or lit=='Y':
        return True
    return False

tekst = input("Podaj tekst: ")
nowy = ""
for i in range(len(tekst)):
    if CzySamogloska(tekst[i]):
        nowy = nowy + '_'
    else:
        nowy = nowy + tekst[i]
print(nowy)
