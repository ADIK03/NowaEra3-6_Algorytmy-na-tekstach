'''
    Ćwiczenie 11
    a.  W pliku otrzymanym od nauczyciela (np. wzorzec_w_tekscie.py) znajduje 
        się fragment programu Szukaj wzorca. Uzupełnij go o odpowiednie 
        instrukcje i uruchom program dla wzorców: AGA oraz ALBO.
'''

TEKST = "ALA ALBO ADA"

def Porownaj(wzorzec):
    n = len(TEKST)
    m = len(wzorzec)
    for poz in range(0, n-m+1):
        j = 0
        while j < m and TEKST[poz+j] == wzorzec[j]:
            j = j + 1
        if j == m:
            return poz
    return -1

print("Tekst:", TEKST)
print("Podaj wzorzec:", end=" ")
wzorzec = input()

print("Pozycja:", Porownaj(wzorzec))