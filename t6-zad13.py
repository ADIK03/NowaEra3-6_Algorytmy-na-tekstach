'''
    (**) Zadanie 12
    Napisz funkcję o nagłówku int ile(string wzorzec), która zwróci liczbę
    całkowitą oznaczającą liczbę wystąpień wzorca w tekście. Przyjmij, że tekst
    jest zapisany w stałej globalnej o nazwie  TEKST.

'''

TEKST = "nie zawsze to co się świeci to złoto"

def ile(wzorzec):
    ile = 0
    n = len(TEKST)
    m = len(wzorzec)

    for poz in range(0, n-m+1): # wystarczy range(n-m+1)
        j = 0
        while j < m and TEKST[poz+j] == wzorzec[j]:
            j = j + 1
        if j == m:
            ile = ile +1
    return ile

print(ile("to"))
