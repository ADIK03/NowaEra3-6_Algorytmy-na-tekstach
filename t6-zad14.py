'''
    (**) Zadanie 14
    Napisz program, który w odpowiedzi na podaną datę urodzenia (dzień
    i miesiąc) wypisze odpowiadający jej znak zodiaku. Na przykład dla danych
    21.07 wynikiem będzie napis rak.
'''

dzien = int(input("Podaj dzień urodzenia (1-31): "))
miesiac = int(input("Podaj miesiąc urodzenia (1-12): "))
if miesiac == 1: # styczeń
    if dzien < 20: zodiak = "koziorożec"
    else: zodiak = "wodnik"
elif miesiac == 2: # luty
    if dzien < 19: zodiak = "wodnik"
    else: zodiak = "ryby"
elif miesiac == 3: # marzec
    if dzien < 21: zodiak = "ryby"
    else: zodiak = "baran"
elif miesiac == 4: # kwiecień
    if dzien < 20: zodiak = "baran"
    else: zodiak = "byk"
elif miesiac == 5: # maj
    if dzien < 23: zodiak = "byk"
    else: zodiak = "bliźnięta"
elif miesiac == 6: # czerwiec
    if dzien < 22: zodiak = "bliźnięta"
    else: zodiak = "rak"
elif miesiac == 7: # lipiec
    if dzien < 23: zodiak = "rak"
    else: zodiak = "lew"
elif miesiac == 8: # sierpień
    if dzien < 24: zodiak = "lew"
    else: zodiak = "panna"
elif miesiac == 9: # wrzesień
    if dzien < 23: zodiak = "panna"
    else: zodiak = "waga"
elif miesiac == 10: # październik
    if dzien < 23: zodiak = "waga"
    else: zodiak = "skorpion"
elif miesiac == 11: # listopad
    if dzien < 22: zodiak = "skorpion"
    else: zodiak = "strzelec"
else: # grudzień
    if dzien < 22: zodiak = "strzelec"
    else: zodiak = "koziorożec"

print("Znak zodiaku to " + zodiak)
