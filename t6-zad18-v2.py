'''
    (***) Zadanie 18
    Napisz program, który zapisze podane przez użytkownika zdanie (w języku 
    angielskim) w kodzie Morse’a. Oprócz liter program powinien też kodować 
    cyfry i kropkę.
'''

kody = {} # słownik 

kody['a'] = kody['A'] = ". _";
kody['b'] = kody['B'] = "_ . . .";
kody['c'] = kody['C'] = "_ . _ .";
kody['d'] = kody['D'] = "_ . .";
kody['e'] = kody['E'] = ".";
kody['f'] = kody['F'] = ". . _ .";
kody['g'] = kody['G'] = "_ _ .";
kody['h'] = kody['H'] = ". . . .";
kody['i'] = kody['I'] = ". .";
kody['j'] = kody['J'] = ". _ _ _";
kody['k'] = kody['K'] = "_ . _";
kody['l'] = kody['L'] = ". _ . .";
kody['m'] = kody['M'] = "_ _";
kody['n'] = kody['N'] = "_ .";
kody['o'] = kody['O'] = "_ _ _";
kody['p'] = kody['P'] = ". _ _ .";
kody['q'] = kody['Q'] = "_ _ . _";
kody['r'] = kody['R'] = ". _ .";
kody['s'] = kody['S'] = ". . .";
kody['t'] = kody['T'] = "_";
kody['u'] = kody['U'] = ". . _";
kody['v'] = kody['V'] = ". . . _";
kody['w'] = kody['W'] = ". _ _";
kody['x'] = kody['X'] = "_ . . _";
kody['y'] = kody['Y'] = "_ . _ _";
kody['z'] = kody['Z'] = "_ _ . .";
kody['1'] = ". _ _ _ _";
kody['2'] = ". . _ _ _";
kody['3'] = ". . . _ _";
kody['4'] = ". . . . _";
kody['5'] = ". . . . .";
kody['6'] = "_ . . . .";
kody['7'] = "_ _ . . .";
kody['8'] = "_ _ _ . .";
kody['9'] = "_ _ _ _ .";
kody['0'] = "_ _ _ _ _";
kody['.'] = ". _ . _ . _";
kody[' '] = "    ";


zdanie = input("Podaj zdanie: ")
for i in range(len(zdanie)):
    print(kody[zdanie[i]], end="   ")
