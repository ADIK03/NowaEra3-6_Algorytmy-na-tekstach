'''
    (**) Zadanie 11
    Wyrazy różniące się dowolną jedną literą nazywa się metagramami, np.: kasa
    i kara. Napisz program sprawdzający, czy podana para wyrazów to metagramy.
'''

def CzyMetagram(napis1, napis2):
    dl1 = len(napis1)
    dl2 = len(napis2)

    licznik = 0

    if napis1 != napis2 and dl1 == dl2:
        for i in range(dl1):
            if napis1[i] != napis2[i]:
                licznik = licznik + 1

    if licznik == 1:
        return True
    return False

napis1 = input("Podaj pierwszy wyraz: ")
napis2 = input("Podaj drugi wyraz: ")

if CzyMetagram(napis1, napis2):
    print("TAK")
else:
    print("NIE")

