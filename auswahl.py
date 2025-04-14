#  Copyright (c) 2025. Diese Python Skripte wurden von mir erstellt und können als Referenz von anderen genutzt und gelesen werden.

""" Diese Datei erzeugt das Hauptmenü des Programms """

from programme import fahrpreis_berechnen, bools, verkehrsmittel, waehrungsrechner, kinoticket, einkaufszettel, \
    kinoticket2
from funktionen import printf
import os
import inspect
import programme

menu_angezeigt = False

def clear_screen():
    """ Betriebssystemabhänge Methode die Konsole zu löschen """
    # Überprüfen, ob das Betriebssystem Windows oder Unix ist
    if os.name == 'nt':  # nt ist Windows
        os.system('cls')
    else:  # für Unix-basierte Systeme wie Linux oder macOS
        os.system('clear')


def menu(name, dusie):
    """ Das 'alte' oder zuerst erstellte Menü, es musste manuell jedes neue Programm eingepflegt werden,
     wurde im laufe der Zeit durch menu_neu abgelöst"""
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
                printf("Das Programm wird beendet.")
                exit()  # Beende die Schleife und somit das Programm
            elif wahl == 'Kartoffel':
                printf("Herzlichen Glückwunsch, du hast 100,-€ im Quiz des RTL Mittagsmagazins gewonnen.")
            else:
                printf(f"Leider war deine Eingabe von {wahl} nicht gültig.\nBitte wähle eine der oben genannten Nummern aus.")
        except ValueError:
            # Wenn der Benutzer keine gültige Zahl eingibt, wird dieser Fehler abgefangen
            printf("Ungültige Eingabe! Bitte gib eine Zahl ein.")


def menu_neu(name, dusie):
    """Automatisiertes Menü: Sucht automatisch Programme und Beschreibungen aus programme.py"""

    global menu_angezeigt  # Auf die globale Variable zugreifen

    if menu_angezeigt:
        # Menü bereits angezeigt, einfach ausgeben
        printf(f"Hallo {name},\nes stehen verschiedene Programme zur Verfügung, bitte {'wähle' if dusie == 'du' else 'wählen Sie'} eines aus:")
        for eintrag in optionen:
            printf(f"{eintrag.auswahl}.) {eintrag.beschreibung}")
        return

    class Menue:
        def __init__(self, auswahl, programm, beschreibung):
            self.auswahl = auswahl
            self.programm = programm
            self.beschreibung = beschreibung

    optionen = []

    for index, (func_name, func) in enumerate(inspect.getmembers(programme, inspect.isfunction), start=1):
        try:
            beschreibung = "Keine Beschreibung verfügbar"
            with open("programme.py", "r", encoding="utf-8") as file:
                for line_number, line in enumerate(file, start=1):
                    if line_number == func.__code__.co_firstlineno:  # Funktionsdefinition gefunden
                        # Nächste Zeile explizit einlesen
                        next_line = next(file, "").strip()

                        if next_line.lstrip().startswith("#beschreibung: ") or next_line.lstrip().startswith(
                                "# beschreibung: "):
                            beschreibung = next_line.lstrip().replace("#beschreibung: ", "").replace("# beschreibung: ",
                                                                                                     "").strip()

                        break  # Nach dem Lesen der nächsten Zeile aufhören

        except Exception as e:
            beschreibung = f"Fehler beim Lesen: {e}"

        optionen.append(Menue(index, func, beschreibung))

    # Option zum Beenden hinzufügen
    optionen.append(Menue(99, exit, "um das Programm zu beenden"))

    # Begrüßung
    printf(f"Hallo {name},\nes stehen verschiedene Programme zur Verfügung, bitte {'wähle' if dusie == 'du' else 'wählen Sie'} eines aus:")

    for eintrag in optionen:
        printf(f"{eintrag.auswahl}.) {eintrag.beschreibung}")

    try:
        option = int(input("Welches Programm möchtest du nutzen? "))
        for eintrag in optionen:
            if eintrag.auswahl == option:
                if eintrag.programm == exit:
                    printf("Das Programm wird beendet.")
                    exit()
                else:
                    clear_screen()
                    eintrag.programm(name, dusie)
                return
        printf("Ungültige Auswahl, bitte erneut versuchen.")
        menu_neu(name, dusie)
    except ValueError:
        printf("Bitte eine Zahl eingeben!")
        menu_neu(name, dusie)

    # Menü als angezeigt markieren
    menu_angezeigt = True