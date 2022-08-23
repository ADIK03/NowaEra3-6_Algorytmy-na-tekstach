'''
    (**) Zadanie 16
    Napisz funkcję, która kompresuje tekst prostą metodą opartą na zliczaniu 
    powtarzających się liter (jedna litera może się powtarzać maksymalnie 9 
    razy). Na przykład wynikiem dla łańcucha aaabbcaa będzie a3b2c1a2. Jeśli 
    wynik miałby być łańcuchem dłuższym niż ten dany na wejściu, to funkcja 
    powinna zwracać pierwotny łańcuch znaków.
'''

def kompresuj(s):
    i = 0
    s2 = ""
    dl = len(s)
    while i < dl:
        s2 = s2 + s[i]
        j = 1
        while i+j<dl and s[i] == s[i+j]:
            j = j + 1
        i = i + j
        s2 = s2 + chr(j+ord('0'))
    if len(s2) > len(s):
        return s
    return s2

print(kompresuj("aaabbcaa"))
