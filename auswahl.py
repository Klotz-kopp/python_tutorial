#  Copyright (c) 2025. Diese Python Skripte wurden von mir erstellt und können als Referenz von anderen genutzt und gelesen werden.
from programme import fahrpreis_berechnen, bools, verkehrsmittel, waehrungsrechner, kinoticket, einkaufszettel, \
    kinoticket2

import os
import inspect
import programme

def clear_screen():
    # Überprüfen, ob das Betriebssystem Windows oder Unix ist
    if os.name == 'nt':  # nt ist Windows
        os.system('cls')
    else:  # für Unix-basierte Systeme wie Linux oder macOS
        os.system('clear')


def menu(name, dusie):
    while True:  # Solange der Benutzer keine gültige Eingabe macht, wiederhole den Loop
        try:
            # Versuche, die Eingabe in eine ganze Zahl umzuwandeln
            wahl = int(input(
                f"Hallo {name},\nes stehen verschiedene Programme zur Verfügung, bitte wähle eines aus:\n1.) für den Taxameter welcher dir den Preis für eine Taxifahrt berechnet.\n2.) für eine Wahrheitsprüfung von hardcodierten variablen\n3.) für eine empfehlung welche Verkehrsmittel du nutzen möchtest \n4.) für einen Währungsrechner von Euro in Thailändische Baht\n5.) Für unser Kinoticket verkauf\n6.) einen Einkaufszettel erstellen\n7.) unseren alten Kinoticket Automaten\n99.) um das Programm zu beenden\nbitte wähle jetzt aus den oben genannten Nummern dein Programm."))

            # Verarbeite die Eingabe basierend auf der Auswahl
            if wahl == 1:
                clear_screen()
                fahrpreis_berechnen(name, dusie)
            elif wahl == 2:
                clear_screen()
                bools(name, dusie)
            elif wahl == 3:
                clear_screen()
                verkehrsmittel(name, dusie)
            elif wahl == 4:
                clear_screen()
                waehrungsrechner(name, dusie)
            elif wahl == 5:
                clear_screen()
                kinoticket2(name, dusie)
            elif wahl == 6:
                clear_screen()
                einkaufszettel(name, dusie)
            elif wahl == 7:
                clear_screen()
                kinoticket(name,dusie)
            elif wahl == 99:
                print("Das Programm wird beendet.")
                exit()  # Beende die Schleife und somit das Programm
            elif wahl == 'Kartoffel':
                print("Herzlichen Glückwunsch, du hast 100,-€ im Quiz des RTL Mittagsmagazins gewonnen.")
            else:
                print(f"Leider war deine Eingabe von {wahl} nicht gültig.\nBitte wähle eine der oben genannten Nummern aus.")
        except ValueError:
            # Wenn der Benutzer keine gültige Zahl eingibt, wird dieser Fehler abgefangen
            print("Ungültige Eingabe! Bitte gib eine Zahl ein.")


def menu_neu(name, dusie):
    class Menue:
        def __init__(self, auswahl, programm, beschreibung):
            self.auswahl = auswahl
            self.programm = programm
            self.beschreibung = beschreibung

    # Dynamisch alle Funktionen aus programme.py mit Beschreibungen laden
    optionen = []
    for index, (name, func) in enumerate(inspect.getmembers(programme, inspect.isfunction), start=1):
        # Versuche die erste Zeile des Funktionscodes als Beschreibung zu nutzen
        doc = inspect.getsource(func).split("\n")[0].strip()
        if doc.startswith("#beschreibung: "):
            beschreibung = doc.replace("#beschreibung: ", "")
        else:
            beschreibung = "Keine Beschreibung verfügbar"

        optionen.append(Menue(index, func, beschreibung))

    # Option zum Beenden hinzufügen
    optionen.append(Menue(99, exit, "um das Programm zu beenden"))

    # Begrüßung
    print(
        f"Hallo {name},\nes stehen verschiedene Programme zur Verfügung, bitte {'wähle' if dusie == 'du' else 'wählen Sie'} eines aus:")

    # Menüoptionen ausgeben
    for eintrag in optionen:
        print(f"{eintrag.auswahl}.) {eintrag.beschreibung}")

    # Benutzereingabe abfragen
    try:
        option = int(input("Welches Programm möchtest du nutzen? "))
        for eintrag in optionen:
            if eintrag.auswahl == option:
                if eintrag.programm == exit:
                    print("Das Programm wird beendet.")
                    exit()
                else:
                    clear_screen()
                    eintrag.programm(name, dusie)
                return
        print("Ungültige Auswahl, bitte erneut versuchen.")
        menu_neu(name, dusie)
    except ValueError:
        print("Bitte eine Zahl eingeben!")
        menu_neu(name, dusie)
