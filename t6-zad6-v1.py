'''
    (*) Zadanie 6
    Napisz program, który dla podanego wyrazu wyświetli jego zapis wspak 
    (od ostatniej do pierwszej litery).
'''

w = input("Podaj wyraz: ")
rw = ""
for i in w:
    rw = i + rw
print(rw)
