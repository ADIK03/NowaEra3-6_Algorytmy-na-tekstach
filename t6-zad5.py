'''
    (*) Zadanie 5
    Napisz program, który wczyta wyraz wzorzec, a następnie będzie wczytywać 
    kolejne wyrazy aż do pojawienia się ciągu znaków ***. Następnie program 
    powinien wyświetlić liczbę powtórzeń wzorca pośród wczytanych wyrazów.
'''

l = 0 # liczba wystąpień wzorca pośród wpisywanych wyrazów

wzorzec = input("Podaj wzorzec: ")
print("Podaj kolejne wyrazy:")
wyraz = input()
while wyraz != "***":
    if wyraz == wzorzec:
        l = l+1;
    wyraz = input()
print("Liczba powtórzeń wzorca: ", l);
