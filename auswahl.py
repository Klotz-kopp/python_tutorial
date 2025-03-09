#  Copyright (c) 2025. Diese Python Skripte wurden von mir erstellt und können als Referenz von anderen genutzt und gelesen werden.
from programme import fahrpreis_berechnen, bools, verkehrsmittel, waehrungsrechner
import os

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
                f"Hallo {name},\nes stehen verschiedene Programme zur Verfügung, bitte wähle eines aus:\n1.) für den Taxameter welcher dir den Preis für eine Taxifahrt berechnet.\n2.) für eine Wahrheitsprüfung von hardcodierten variablen\n3.) für eine empfehlung welche Verkehrsmittel du nutzen möchtest oder\n4.) für einen Währungsrechner von Euro in Thailändische Baht\n99.) um das Programm zu beenden\nbitte wähle jetzt aus den oben genannten Nummern dein Programm."))

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
