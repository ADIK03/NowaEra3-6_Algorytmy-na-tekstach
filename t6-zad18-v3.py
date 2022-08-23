'''
    (***) Zadanie 18
    Napisz program, który zapisze podane przez użytkownika zdanie (w języku 
    angielskim) w kodzie Morse’a. Oprócz liter program powinien też kodować 
    cyfry i kropkę.
'''

kody = {
'a' : ". _", 
'b' : "_ . . .", 
'c' : "_ . _ .", 
'd' : "_ . .", 
'e' : ".", 
'f' : ". . _ .", 
'g' : "_ _ .", 
'h' : ". . . .", 
'i' : ". .", 
'j' : ". _ _ _", 
'k' : "_ . _", 
'l' : ". _ . .", 
'm' : "_ _", 
'n' : "_ .", 
'o' : "_ _ _", 
'p' : ". _ _ .", 
'q' : "_ _ . _", 
'r' : ". _ .", 
's' : ". . .", 
't' : "_", 
'u' : ". . _", 
'v' : ". . . _", 
'w' : ". _ _", 
'x' : "_ . . _", 
'y' : "_ . _ _", 
'z' : "_ _ . .", 
'1' : ". _ _ _ _", 
'2' : ". . _ _ _", 
'3' : ". . . _ _", 
'4' : ". . . . _", 
'5' : ". . . . .", 
'6' : "_ . . . .", 
'7' : "_ _ . . .", 
'8' : "_ _ _ . .", 
'9' : "_ _ _ _ .", 
'0' : "_ _ _ _ _", 
'.' : ". _ . _ . _", 
' ' : "    "
}

zdanie = input("Podaj zdanie: ")
for znak in zdanie:
    print(kody[znak.lower()], end="   ")
