'''
    (*) Zadanie 4
    Napisz program, który wczyta z klawiatury łańcuch znaków (składający się 
    z kombinacji cyfr oraz małych i wielkich liter) i wypisze tylko wielkie 
    litery, które pojawiły się w tekście.

'''

s = input("Podaj łańcuch znaków: ")

for i in range(len(s)):
    if s[i] >= 'A' and s[i] <= 'Z':
        print(s[i], end="")
