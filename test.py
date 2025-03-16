#  Copyright (c) 2025. Diese Python Skripte wurden von mir erstellt und können als Referenz von anderen genutzt und gelesen werden.
#from auswahl import clear_screen


def weihnachtsbaum(name, dusie):
    #import menu from auswahl
    print(f"Hallo {name},\nschön dass {dusie} hier {'bist' if dusie == 'du' else 'sind'}\nIch habe eine Weihnachtsbaum für {'dich' if dusie == 'du' else 'Sie'}.")
    grösse = int(input("Wie groß soll der Weihnachtsbaum werden? (1-99) "))
    if name[-1] == 's':
        print(f"Hier ist {name}' Weihnachtsbaum:")
    else:
        print(f"Hier ist {name}'s Weihnachtsbaum:")

    for i in range(1, grösse):
        x = 2 * i - 1
        y = len(range(1, grösse)) - i
        print(y * " " + x * "*")
    y = len(range(1, grösse)) -1
    print(y * " " + "*")

weihnachtsbaum("Simon", "du")