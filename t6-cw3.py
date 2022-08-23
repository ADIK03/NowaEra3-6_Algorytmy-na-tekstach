'''
    Ćwiczenie 3
    Zmodyfikuj powyższy kod źródłowy tak, aby program wyświetlił znaki, które 
    w tablicy Unicode mają kody liczbowe między 128 000 a 128 287.
'''

for i in range(128000, 128288):
    znak = chr(i)
    print(znak, end=" ")
    if i % 16 == 15:
        print()
print()
