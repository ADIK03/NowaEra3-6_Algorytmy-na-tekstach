'''
    Ćwiczenie 2
    Zapisz kod źródłowy programu w pliku znaki.py i sprawdź działanie programu.
'''

for i in range(32, 127):
    znak = chr(i)
    print(znak, end=" ")
    if i % 16 == 15:
        print()
print()
