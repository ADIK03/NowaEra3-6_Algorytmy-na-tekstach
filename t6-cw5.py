'''
    Ćwiczenie 5
    Zapisz kod źródłowy programu Porównanie adresów i sprawdź działanie programu
    dla takich samych oraz różnych adresów e-mail.
'''

INF_OK = "Hasło do serwisu wysłaliśmy na adres "
INF_BLAD = "Podane adresy e-mail są różne!"

imie = input("Podaj imię: ")
nazwisko = input("Podaj nazwisko: ")

adres_1 = input("Podaj adres e-mail: ")
adres_2 = input("Powtórz adres e-mail: ")

print()
if adres_1 == adres_2:
    print(INF_OK + adres_1)
else:
    print(INF_BLAD)