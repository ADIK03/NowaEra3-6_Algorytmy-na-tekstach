'''
    (*) Zadanie 3
    Napisz program, który wczyta 10 imion osób z twojej klasy i wypisze je 
    w postaci tzw. trójkąta Floyda. Oznacza to, że w pierwszym wierszu będzie 
    jedno imię, a w kolejnych odpowiednio dwa, trzy i cztery.  
    1
    2   3
    4   5   6
    7   8   9   10
'''

N = 10
imiona = []

for i in range(N):
    imiona.append(input())

k = 1
i = 0
while i < N: 
    for j in range(k):
        print(imiona[i+j], end="\t")
    print()
    i = i+k
    k = k+1
