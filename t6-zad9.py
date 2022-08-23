'''
    (**) Zadanie 9
    Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu
    to nazwa jednego ze wzgórz w Nowej Zelandii i jedna z najdłuższych nazw
    geograficznych na świecie. Korzystając z pliku, który przekaże ci nauczyciel
    (np. wzgorze.txt), sprawdź:
    a. długość tej nazwy,
    b. liczbę występujących w niej liter: a, e, i, o, u, y,
    c. czy w nazwie występuje fraza „eaturip”.

'''

TEKST = "Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu";

def Porownaj(wzorzec):
    n = len(TEKST)
    m = len(wzorzec)

    for poz in range(n-m+1):
        j = 0;
        while j < m and TEKST[poz+j] == wzorzec[j]: j = j +1
        if j == m: return poz
    return -1

dl = len(TEKST)
ile_samoglosek = [0, 0, 0, 0, 0, 0] # kolejno: a, e, i, o, u, y

print("Dlugość nazwy: ", dl)

for litera in TEKST:
    if litera == 'a': ile_samoglosek[0] += 1
    elif litera == 'e': ile_samoglosek[1] += 1 #elif jest skróconą formą konstrukcji else if - pozwala ona zapisać tęinstrukcję w jendym wierszu
    elif litera == 'i': ile_samoglosek[2] += 1
    elif litera == 'o': ile_samoglosek[3] += 1
    elif litera == 'u': ile_samoglosek[4] += 1
    elif litera == 'y': ile_samoglosek[5] += 1

print("Liczba samogłosek (a, e, i, o, u, y): ", end="")
for i in ile_samoglosek:
    print(i, end=" ")
print()

print("Nazwa zawiera frazę 'eaturip': ", end="")

if Porownaj("eaturip") != -1:
    print("TAK")
else:
    print("NIE")

