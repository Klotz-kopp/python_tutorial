#  Copyright (c) 2025. Diese Python Skripte wurden von mir erstellt und können als Referenz von anderen genutzt und gelesen werden.
from programme import fahrpreis_berechnen, bools, verkehrsmittel, waehrungsrechner, kinoticket, einkaufszettel, kinoticket2
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
        def __init__(self, auswahl, programm, variablen="name,dusie"):
            self.auswahl = auswahl
            self.programm = programm  # Speichert nur die Referenz zur Funktion
            self.variablen = variablen

    # Menüoptionen als Liste speichern
    optionen = [
        Menue(1, fahrpreis_berechnen),
        Menue(2, bools),
        Menue(3, verkehrsmittel),
        Menue(4, waehrungsrechner),
        Menue(5, kinoticket2),
        Menue(6, einkaufszettel),
        Menue(7, kinoticket)]
    #while true:

