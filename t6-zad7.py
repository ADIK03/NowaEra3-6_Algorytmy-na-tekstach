'''
    (*) Zadanie 7
    W pliku, który otrzymasz od nauczyciela (np. emoji.pdf) znajdują się emoji
    myszy oraz biedronki. Zmodyfikuj program Znaki 2 tak, aby wyświetlił znaki
    zawarte między tymi symbolami.
'''

znak = "🐁"
kod = ord(znak)
kod2 = ord("🐞")

while kod <= kod2:
    print(znak, end=" ")
    if kod % 16 == 15:
        print()
    kod = kod + 1
    znak = chr(kod)
print()

