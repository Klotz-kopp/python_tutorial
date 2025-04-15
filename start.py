#  Copyright (c) 2025. Diese Python Skripte wurden von mir erstellt und können als Referenz von anderen genutzt und gelesen werden.
from funktionen import printf, Farben


def start_program():
    #Aufgabe der Funktion ist das setzen der 2 Variablen 'Name' und 'dusie' für die weitere verwendung im Programmablauf
    name = input("Hallo,\nwie ist dein Name? ")
    printf(f"Hallo {Farben['Cyan'}{name}{Farben['Reset'],\n")

    # Gültigkeitsprüfung für 'dusie'
    while True:
        dusie = input("Soll ich 'du' oder 'Sie' sagen? ").strip()
        if dusie.lower() in ["du", "sie"]:
            break  # Gültige Eingabe -> Schleife verlassen
        printf("Bitte gib nur 'du' oder 'Sie' ein.")

    return name, dusie



