'''
    Ćwiczenie 4
    a. Zapisz kod źródłowy powyższego programu pod nazwą znaki2.py i sprawdź 
       działanie programu.
'''

znak = " "
kod = ord(znak)
kod2 = ord("~")

while kod <= kod2:
    print(znak, end=" ")
    if kod % 16 == 15:
        print()
    kod = kod + 1
    znak = chr(kod)
print()