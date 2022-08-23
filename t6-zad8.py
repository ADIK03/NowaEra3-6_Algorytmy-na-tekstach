def CzySamogloska(lit):
    if ord(lit) >= ord('a'):
        lit = chr(ord(lit) - 32)
    if lit == 'A' or lit == 'E' or lit == 'I' or lit == 'O' or lit == 'U' or lit == 'Y':
        return True
    return False

tekst = input('Podaj tekst: ')
licznik = 0

for i in tekst:
    if(CzySamogloska(i)):
        licznik = licznik + 1
print(licznik)
