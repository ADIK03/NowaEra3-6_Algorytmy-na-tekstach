'''
    (***) Zadanie 17
    Napisz program, który poda liczbę wystąpień każdej litery alfabetu
    łacińskiego w tekście wprowadzonym do stałej globalnej o nazwie TEKST.
    Program nie powinien rozróżniać wielkości liter.
'''

TEKST = "Napisz program, ktory poda liczbe wystapien kazdej litery"

litery = []
for i in range(26):
    litery.append(0)

for i in range(len(TEKST)):
    if TEKST[i] >= "A" and TEKST[i] <= "Z":
        ind = ord(TEKST[i])-ord("A")
        litery[ind] = litery[ind]+1
    elif TEKST[i] >= "a" and TEKST[i] <= "z":
        ind = ord(TEKST[i])-ord("a")
        litery[ind] = litery[ind]+1

for i in range(26):
    print(chr(i+ord("A")), end="")
    print(":", litery[i])
    #lub: print(chr(i+ord("A")) + ": " + str(litery[i]))
    #lub: print(chr(i+ord("A")), ": ", litery[i], sep="")
