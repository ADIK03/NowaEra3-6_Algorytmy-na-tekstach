'''
    (*) Zadanie 6
    Napisz program, który dla podanego wyrazu wyświetli jego zapis wspak 
    (od ostatniej do pierwszej litery).
'''

w = input("Podaj wyraz: ")
for i in range(len(w)-1, -1, -1):
    print(w[i], end="")
