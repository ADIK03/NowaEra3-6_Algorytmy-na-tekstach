# Pętla wykonuje się dla wartości `i` od 32 do 126 (włącznie).
for i in range(32, 127):
    # Konwertujemy aktualną wartość `i` na odpowiadający jej znak ASCII.
    znak = chr(i)
    # Wyświetlamy znak ASCII, z jednym spacją jako separatorem.
    print(znak, end=" ")

    # Sprawdzamy, czy aktualna wartość `i` jest ostatnią wartością w rzędzie (co 16 znaków).
    if i % 16 == 15:
        # Jeśli jesteśmy na końcu rzędu, przechodzimy do nowej linii.
        print()
