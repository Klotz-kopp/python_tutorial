#  Copyright (c) 2025. Diese Python Skripte wurden von mir erstellt und können als Referenz von anderen genutzt und gelesen werden.
from funktionen import printf

#Das erste Spiel, Tic Tac Toe

def erstelle_brett():
    # Spielbrett erstellen
    brett = []
    for i in range(3):
        zeile = [' ', ' ', ' ']
        brett.append(zeile)
    return brett


def drucke_brett(brett):
    # Spielbrett ausgeben
    for zeile in brett:
        printf("|".join(zeile))
        print("------")

def mache_zug(brett, aktueller_spieler, zeile, spalte):
    #Zug machen
    if brett[zeile][spalte] == ' ':
        brett[zeile][spalte] = aktueller_spieler
        return True
    else:
        return False


def pruefe_gewonnen(brett, aktueller_spieler):
    # Überprüfe ob die Siegbedingung erfüllt ist
    for zeile in range(3):
        if brett[zeile][0] == brett[zeile][1] == brett[zeile][2] == aktueller_spieler:
            return True

    for spalte in range(3):
        if brett[0][spalte] == brett[1][spalte] == brett[2][spalte] == aktueller_spieler:
            return True

    if brett[0][0] == brett[1][1] == brett[2][2] == aktueller_spieler or \
       brett[2][0] == brett[1][1] == brett[0][2] == aktueller_spieler:
        return True

def pruefe_unentschieden(brett):
    # Überprüfe ob Unentschieden
    for zeile in brett:
        if ' ' in zeile:
            return False
        else:
            return True

def spiele_tic_tac_toe(name, dusie):
    # beschreibung: Lust auf eine Runde Tic Tac Toe?
    from auswahl import menu_neu

    brett = erstelle_brett()
    aktueller_spieler = 'X'

    while True:
        drucke_brett(brett)
        zeile = int(input(f"Spieler {aktueller_spieler}, wähle deine Zeile (0-2)"))
        spalte = int(input(f"Spieler {aktueller_spieler}, wähle deine Spalte (0-2)"))

        if not mache_zug(brett, aktueller_spieler, zeile, spalte):
            printf("Ungültiger Zug, bitte versuche es erneut!")
            continue

        if pruefe_gewonnen(brett,aktueller_spieler):
            drucke_brett(brett)
            printf(f"Hey, du hast gewonnen, Spieler {aktueller_spieler}.")
            break
        elif pruefe_unentschieden(brett):
            drucke_brett(brett)
            printf(f"Das Spiel ist unentschieden ausgegangen")
        aktueller_spieler = 'O' if aktueller_spieler == 'X' else 'X'

    menu_neu(name, dusie)


