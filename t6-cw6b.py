'''
    Ćwiczenie 6
    b. Zapisz pełny kod źródłowy programu Sprawdzenie adresu i uruchom program. 
       Sprawdź jego działanie dla różnych danych.
'''

def CzyPoprawnyAdres(adres):
    dl = len(adres)

    i = 0  # etap 1
    while adres[i] != "@" and i < dl-1:
        i = i + 1
    if adres[i] != "@" or i < 2:
        return False

    j = dl - 1  # etap 2
    while adres[j] != "@":
        j = j - 1
    if i != j:
        return False

    k = dl - 1  # etap 3
    while adres[k] != "." and k > 0:
        k = k - 1
    if adres[k] != "." or not (k == dl-3 or k == dl-4):
        return False

    if k - i <= 1:  # etap 4
        return False

    return True


INF_OK = "Hasło do serwisu wysłaliśmy na adres "
INF_ROZNE_ADRESY = "Podane adresy e-mail są różne!"
INF_BLAD_ADRESU = "Podany adres e-mail nie jest poprawny!"

imie = input("Podaj imię: ")
nazwisko = input("Podaj nazwisko: ")
adres_1 = input("Podaj adres e-mail: ")

if CzyPoprawnyAdres(adres_1):
    adres_2 = input("Powtórz adres e-mail: ")
    print()
    if adres_1 == adres_2:
        print(INF_OK + adres_1)
    else:
        print(INF_ROZNE_ADRESY)
else:
    print(INF_BLAD_ADRESU)
    