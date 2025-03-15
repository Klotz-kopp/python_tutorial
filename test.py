#  Copyright (c) 2025. Diese Python Skripte wurden von mir erstellt und können als Referenz von anderen genutzt und gelesen werden.
def menu_neu(name, dusie):
    class Menue:
        def __init__(self, auswahl, programm, beschreibung, variablen='name,dusie'):
            self.auswahl = auswahl
            self.programm = programm  # Speichert nur die Referenz zur Funktion
            self.beschreibung = beschreibung
            self.variablen = variablen

    # Menüoptionen als Liste speichern
    optionen = [
        Menue(1, fahrpreis_berechnen, 'für den Taxameter welcher dir den Preis für eine Taxifahrt berechnet'),
        Menue(2, bools, 'für die Wahrheitsprüfung einer hardcodierten variable'),
        Menue(3, verkehrsmittel, 'für eine Empfehlung welches Verkehrsmittel genutzt werden sollte'),
        Menue(4, waehrungsrechner, 'für einen Währungsrechner von Euro in Thailändische Baht'),
        Menue(5, kinoticket2, 'für unseren neuen Kinoticket Verkaufsautomaten'),
        Menue(6, einkaufszettel, 'um einen Einkaufszettel zu erstellen'),
        Menue(7, kinoticket, 'für unseren alten Kinoticket Automaten')]

    if dusie == "du":
        print(f"Hallo {name},\nes stehen verschiedene Programme zur Verfügung, bitte wähle eines aus:")
    else:
        print(f"Hallo {name},\nes stehen verschiedene Programme zur Verfügung, bitte wählen Sie eines aus:")
    for eintrag in optionen:
        print(f"{eintrag.auswahl}.){eintrag.beschreibung}")
    option = input("Welches Programm möchtest du nutzen?")

menu_neu("simon", "du")