#  Copyright (c) 2025. Diese Python Skripte wurden von mir erstellt und können als Referenz von anderen genutzt und gelesen werden.
from funktionen import printf, Farben


def start_program():
    # Aufgabe der Funktion ist das setzen der 2 Variablen 'Name' und 'pronomen' für die weitere verwendung im Programmablauf
    name = input("Hallo,\nwie ist dein Name? ")
    name = f"{Farben['Cyan']}{name}{Farben['Reset']}"
    printf(f"Hallo {name},\n")

    # Gültigkeitsprüfung für 'pronomen'
    while True:
        pronomen = input("Soll ich 'du' oder 'Sie' sagen? ").strip()
        if pronomen.lower() in ["du", "sie"]:
            break  # Gültige Eingabe --> Schleife verlassen
        printf("Bitte gib nur 'du' oder 'Sie' ein.")

    return name, pronomen
