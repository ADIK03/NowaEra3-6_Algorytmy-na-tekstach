'''
    (***) Zadanie 18
    Napisz program, który zapisze podane przez użytkownika zdanie (w języku
    angielskim) w kodzie Morse’a. Oprócz liter program powinien też kodować
    cyfry i kropkę.
'''

kody = [
    "    ",        # spacja
    ". _ . _ . _", # .
    "_ _ _ _ _",   # 0
    ". _ _ _ _",   # 1
    ". . _ _ _",   # 2
    ". . . _ _",   # 3
    ". . . . _",   # 4
    ". . . . .",   # 5
    "_ . . . .",   # 6
    "_ _ . . .",   # 7
    "_ _ _ . .",   # 8
    "_ _ _ _ .",   # 9
    ". _",         # A
    "_ . . .",     # B
    "_ . _ .",     # C
    "_ . .",       # D
    ".",           # E
    ". . _ .",     # F
    "_ _ .",       # G
    ". . . .",     # H
    ". .",         # I
    ". _ _ _",     # J
    "_ . _",       # K
    ". _ . .",     # L
    "_ _",         # M
    "_ .",         # N
    "_ _ _",       # O
    ". _ _ .",     # P
    "_ _ . _",     # Q
    ". _ .",       # R
    ". . .",       # S
    "_",           # T
    ". . _",       # U
    ". . . _",     # V
    ". _ _",       # W
    "_ . . _",     # X
    "_ . _ _",     # Y
    "_ _ . ."      # Z
]


zdanie = input("Podaj zdanie: ")
for i in range(len(zdanie)):
    ind = ord(zdanie[i])
    if ind == ord(" "):
        ind = ind - ord(" ")
    elif ind == ord("."):
        ind = ind - ord(".")+1
    elif ind <= ord("9"):
        ind = ind - ord("0")+2
    elif ind <= ord("Z"):
        ind = ind - ord("A")+12
    elif ind <= ord("z"):
        ind = ind - ord("a")+12
    print(kody[ind], end="   ")
