'''
    Ćwiczenie 4
    b. Napisz program, który wyświetli litery od A do Z w dwóch wierszach 
       w następujący sposób:
       ABCDEFGHIJKLM
       ZYXWVUTSRQPON
'''

znak = "A"
kod = ord(znak)
kod2 = ord("M")

while kod <= kod2:
    print(znak, end="")
    kod = kod + 1
    znak = chr(kod)
print()
znak = "Z"
kod = ord(znak)
kod2 = ord("N")
while kod >= kod2:
    print(znak, end="")
    kod = kod - 1
    znak = chr(kod)
print()