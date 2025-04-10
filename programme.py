#  Copyright (c) 2025. Diese Python Skripte wurden von mir erstellt und können als Referenz von anderen genutzt und gelesen werden.

""" Diese Datei enthält alle Mini Programme welche im Rahmen des / der Youtube Tutorials erstellt wurden.
Konventionen:   - alle Programme sind in einer eigenen Funktion
                - alle Programme werden mit der Übergabe der Variablen 'name' & 'dusie' gestartet, auch wenn nicht, benutzt
                - alle Programme haben in der ersten Zeile ein Kommentar welcher beginnt mit '# beschreibung: ' gefolgt von einer
                  Beschreibung des Programms welches später den entsprechenden Menüpunkt bildet, dies ist nötig damit
                  das Menü automatisch erstellt werden kann
                - alle Programme starten mit 'from auswahl import menu_neu' und enden mit 'menu_neu(name, dusie)' damit
                  beim Beenden das Menü erneut aufgerufen wird.
                Live Template progtemp"""

import requests
import xml.etree.ElementTree as ET

def fahrpreis_berechnen(name, dusie):
    # beschreibung: für den Taxameter welcher dir den Preis für eine Taxifahrt berechnet
    from auswahl import menu_neu
    print(f"Hallo {name},\nherzlich willkommen beim Taxameter.\nDer Taxameter soll den voraussichtlichen Fahrpreis für eine Taxifahrt ermitteln.\nFangen wir an.")
    while True:
        if dusie.lower() == 'sie':
            km = input("Wie viele Kilometer möchten Sie fahren? ")
        elif dusie.lower() == 'du':
            km = input("Wie viele Kilometer möchtest du fahren? ")
        else:
            print("Ungültige Eingabe, bitte 'du' oder 'Sie' wählen.")
            return

        basispreis = 2.5
        km_preis = 1.75

        # Leetspeak für eine spezielle Eingabe (1337)
        if km == "1337":
            print("Für j3m4nd3n d3r s0 l33t 1st w13 du, 1st d13 T0ur gr4t1s")
        else:
            try:
                km = float(km)
                fahrpreis = basispreis + (km * km_preis)
                print(f"Die gewählte Strecke von {km} Kilometern wird voraussichtlich {fahrpreis:.2f}€ kosten.")
            except ValueError:
                print("Ungültige Eingabe. Bitte eine gültige Zahl für die Kilometeranzahl eingeben.")
                continue  # Bei ungültiger Eingabe zurück zur Kilometerabfrage
        nochmal = "ja"
        # Nachfrage, ob eine neue Fahrt berechnet werden soll
        if dusie.lower() == 'sie':
            nochmal = input("Möchten Sie die Kosten für eine weitere Fahrt berechnet bekommen? (ja/nein) ")
        elif dusie.lower() == 'du':
            nochmal = input("Möchtest du die Kosten für eine weitere Fahrt berechnet bekommen? (ja/nein) ")

        if nochmal.lower() != 'ja':
            menu_neu(name, dusie)
            #print("Das Programm wird beendet.")
            #break # Beende das Programm, wenn die Antwort nicht 'ja' ist


def waehrungsrechner(name, dusie):
    # beschreibung: für einen Währungsrechner von Euro in Thailändische Baht
    from auswahl import menu_neu

    # URL der EZB für die aktuellen Wechselkurse
    url = 'https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml'

    try:
        # Herunterladen der XML-Daten
        response = requests.get(url)
        response.raise_for_status()  # Überprüfen auf HTTP-Fehler

        # Parsen der XML-Daten
        tree = ET.ElementTree(ET.fromstring(response.content))
        root = tree.getroot()

        # Namensraum der XML-Datei
        namespace = {'ns': 'http://www.ecb.int/vocabulary/2002-08-01/eurofxref'}

        # Suchen des Wechselkurses für den thailändischen Baht (THB)
        baht_kurs = None
        for cube in root.findall('.//ns:Cube/ns:Cube/ns:Cube', namespace):
            if cube.get('currency') == 'THB':
                baht_kurs = float(cube.get('rate'))
                break

        if baht_kurs is None:
            print("Der Wechselkurs für den thailändischen Baht konnte nicht gefunden werden.")
            return

        # Benutzerabfrage für den Euro-Betrag
        euro = float(input("Wie viel Euro möchten Sie umrechnen? "))
        baht = euro * baht_kurs
        print(f"Ihre {euro:.2f} € sind {baht:.2f} Baht wert (Wechselkurs: 1 € = {baht_kurs:.2f} THB).")

    except requests.RequestException as e:
        print(f"Fehler beim Abrufen der Wechselkurse: {e}")
    except ET.ParseError:
        print("Fehler beim Verarbeiten der XML-Daten.")
    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")

    # Rückkehr zum Hauptmenü
    menu_neu(name, dusie)


def bools(name,dusie):
    # beschreibung: für die Wahrheitsprüfung einer hard codierte Variable
    from auswahl import menu_neu
    var1 = 40+2
    var2 = 42
    if var1 > var2:
        print(f"Variable 1 ({var1}) ist größer als Variable 2 ({var2})")
    elif var1 < var2:
        print(f"Variable 1 ({var1}) ist kleiner als Variable 2 ({var2}).")
    elif var1 == var2:
        print(f"Beide Variablen ({var1}) sind gleich.")
    menu_neu(name, dusie)


def verkehrsmittel(name,dusie):
    # beschreibung: für eine Empfehlung welches Verkehrsmittel genutzt werden sollte
    from auswahl import menu_neu
    strecke = int(input(f"Wie weit ist deine Strecke in Kilometer?"))
    if strecke < 3:
        print(f"Deine {strecke} km lange Strecke kannst du zu Fuß gehen")
    elif 3 < strecke < 20:
        print(f"Deine {strecke} km lange Strecke kannst du mit dem Fahrrad zurück legen.")
    elif strecke == 3:
        print(f"Deine {strecke} km lange Strecke kannst du sowohl mit dem Fahrrad als auch zu Fuß zurücklegen,\nganz nach belieben.")
    elif strecke ==42:
        print("Schnapp dir dein Handtuch und halt den Daumen raus.")
    elif strecke > 20:
        print(f"Deine {strecke} km lange Strecke solltest du mit den Öfis oder dem Auto zurück legen.")
    menu_neu(name, dusie)


def kinoticket(name, dusie):
    # beschreibung: für unseren alten Kinoticket Automaten
    from auswahl import menu_neu

    # Ticketpreise für jede Kategorie
    kind = 5.00
    erwachsen = 10.00
    senior = 7.50
    preis = 0
    # Eingabe des Alters
    try:
        alter = int(input(f"Hallo {name},\nwir bieten in unserem Kino drei Preiskategorien an.\n1.) Kind\n2.) Erwachsene\n3.) Senioren\nBitte gib das Alter der Kinobesucher an: "))
    except ValueError:
        print("Bitte gib ein gültiges Alter ein.")
        return

    # Zuweisung der Preiskategorie basierend auf dem Alter
    if alter < 18:
        kategorie = "kind"
    elif 18 <= alter < 65:
        kategorie = "erwachsen"
    else:
        kategorie = "senior"

    # Eingabe der Ticketanzahl
    try:
        menge = int(input(f"Wie viele Tickets der Kategorie {kategorie} möchtest du erwerben?"))
        if menge <= 0:
            print("Die Anzahl der Tickets muss größer als 0 sein.")
            return
    except ValueError:
        print("Bitte gib eine gültige Anzahl an Tickets ein.")
        return

    # Berechnung des Preises basierend auf der Kategorie
    if kategorie == "kind":
        preis = menge * kind
    elif kategorie == "erwachsen":
        preis = menge * erwachsen
    elif kategorie == "senior":
        preis = menge * senior

    # Ausgabe der Rechnung
    if dusie == 'du':
        print(f"Die {menge} Kinotickets in der Kategorie {kategorie} kosten dich {preis:.2f}€. Bitte an Schalter 2 bezahlen.\nVielen Dank für deinen Besuch in unserem Kino.")
    else:
        print(f"Die {menge} Kinotickets in der Kategorie {kategorie} kosten Sie {preis:.2f}€. Bitte zahlen Sie an Schalter 3.\nWir danken Ihnen für Ihren Besuch in unserem Kino.")

    # Zurück zum Menü
    menu_neu(name, dusie)


def einkaufszettel(name, dusie):
    # beschreibung: um einen Einkaufszettel zu erstellen
    from auswahl import menu_neu
    einkaufszettel = []
    print(f"Hallo {name},\nlass uns einen Einkaufszettel schreiben.\nAktuell ist dein Einkaufszettel leer.")

    while True:
        auswahl = input("Möchtest du etwas hinzufügen, entfernen, ansehen oder beenden? ").strip().lower()

        if auswahl == 'hinzufügen':
            item = input("Was möchtest du hinzufügen? ").strip()
            einkaufszettel.append(item)
            print(f"{item} wurde hinzugefügt.")

        elif auswahl == 'entfernen':
            item = input("Was möchtest du entfernen? ").strip()
            if item in einkaufszettel:
                einkaufszettel.remove(item)
                print(f"{item} wurde entfernt.")
            else:
                print(f"{item} ist nicht auf dem Einkaufszettel.")

        elif auswahl == 'ansehen':
            if not einkaufszettel:
                print("Dein Einkaufszettel ist noch leer.")
            else:
                print("Aktueller Einkaufszettel:")
                for index, item in enumerate(einkaufszettel, start=1):
                    print(f"{index}. {item}")

        elif auswahl == 'beenden':
            print("Auf Wiedersehen!")
            break

        else:
            print("Ungültige Auswahl. Bitte wähle 'hinzufügen', 'entfernen', 'ansehen' oder 'beenden'.")

    # Zurück zum Menü
    menu_neu(name, dusie)


def kinoticket2 (name, dusie):
    # beschreibung: für unseren neuen Kinoticket Verkaufsautomaten
    from auswahl import menu_neu

    class Ticket:
        def __init__(self, kategorie, alter_start, alter_ende, preis):
            self.kategorie = kategorie
            self.alter_start = alter_start
            self.alter_ende = alter_ende
            self.preis = preis

    kind = Ticket('Kind', 0, 17, 5)
    erwachsener = Ticket('Erwachsener', 18, 64, 10)
    senior = Ticket ('Senior', 65,120,7.5)
    anzahl = int(input(f"Hallo {name},\nWillkommen an unserem Kinoticket Verkaufsautomaten.\nWie viele Personen möchten gerne ins Kino?"))
    i = 0
    gesamtpreis = 0
    while i < anzahl:
        alter = int(input(f"Wie alt ist Person Nummer {i+1}?"))
        if kind.alter_start <= alter <= kind.alter_ende:
            gesamtpreis += kind.preis
        elif erwachsener.alter_start <= alter <= erwachsener.alter_ende:
            gesamtpreis += erwachsener.preis
        elif senior.alter_start <= alter <= senior.alter_ende:
            gesamtpreis += senior.preis
        else:
            gesamtpreis += 0
            print("Freiticket!")
        i += 1
    print (f"Der Kinobesuch kostet eure {anzahl} köpfige Besuchergruppe: {gesamtpreis:.2f} €\nWir wünschen euch viel Spaß.")

    # Zurück zum Menü
    menu_neu(name, dusie)


def weihnachtsbaum(name, dusie):
    # beschreibung: um einen schönen Weihnachtsbaum zu bekommen
    from auswahl import menu_neu

    print(f"Hallo {name},\nschön dass {dusie} hier {'bist' if dusie == 'du' else 'sind'}\nIch habe eine Weihnachtsbaum für {'dich' if dusie == 'du' else 'Sie'}.")
    grösse = int(input("Wie groß soll der Weihnachtsbaum werden? (1-99) "))
    grösse += 1
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
    if input("Möchtest du einen weiteren Weihnachtsbaum? (ja/nein)") == "ja":
        weihnachtsbaum(name, dusie)
    else:
        menu_neu(name, dusie)


def tiere_raten(name, dusie):
    # beschreibung: ein Tierkategoriesierer
    from auswahl import menu_neu
    tier = input("Bitte nenne ein Tier: ").capitalize()
    match tier:
        case "Hund" | "Katze" | "Goldfisch":
            print(f"{tier} ist ein Haustier.")
        case "Fliege" | "Biene" | "Wespe":
            print(f"{tier} ist ein Fliegevieh.")
        case "Reh" | "Hirsch" | "Wildschwein":
            print(f"{tier} ist ein Wildtier.")
        case "Kuh" | "Schwein" | "Schaf":
            print(f"{tier} ist ein Nutztier.")
        case "Berta":
            print(f"{tier} ist der süßeste Hunde den von wo gibt!")
        case "Mücke" | "Schabe" | "Maulwurf":
            print(f"Ich fragte nach einem Tier\n{tier} ist ein Untier (vgl. Kraut und Unkraut)")
        case _ if tier == name:
            print("Das ist mein süßer Schatz")
        case _:
            print(f"{tier} kenne ich leider nicht, ich bin ja auch nur ein dummer Computer.")

    menu_neu(name, dusie)
    
    
def zählen(name, dusie):
    # beschreibung: Ich kann dir was vorzählen, glaube ich
    from auswahl import menu_neu

    nochmal = True  # Startwert für Schleife
    while nochmal:
        counter = 1  # Zähler zurücksetzen

        # Eingabe der Obergrenze
        limit = int(input("Wie weit soll ich zählen? "))

        # Zählschleife
        while counter <= limit:
            match counter:
                case 0:
                    print("Null")
                case 1:
                    print("Eins")
                case 2:
                    print("Zwei")
                case 3:
                    print("Drei")
                case 4:
                    print("Vier")
                case 5:
                    print("Fünf")
                case 42:
                    print("Dies ist die Antwort auf die Frage nach dem Leben, dem Univerum und dem ganzen Rest.")
                case _:
                    print("Ich glaube ich habe mich verzählt!")
            counter += 1

        print("Das wars...")

        # Nachfrage für Wiederholung
        nochmal = input("Nochmal zählen? (j/n): ").lower() == "j"

    # Rückkehr zum Menü
    menu_neu(name, dusie)


def zahlen_raten(name, dusie):
    # beschreibung: Das Zahlenrate Spiel
    from auswahl import menu_neu
    from random import randint
    zahl = randint(1, 100)
    tipp = 0
    counter = 0
    if dusie == 'du':
        regeln_ansehen = input(f"Hallo {name},\nWillkommen beim Zahlen rate Spiel.\nMöchtest du die Spielregel sehen? (j/n) ")
        if regeln_ansehen == 'j':
            print("Alles klar, die Regeln sind sehr einfach. Ich denke mir eine Zahl aus, und du musst versuchen diese Zahl zu erraten.\nKeine Angst, ich nehme nur Zahlen zwischen 1 und 100.\nUnd ich bin nett, immer wenn deine Antwort nicht richtig ist, gebe ich dir einen Hinweis, ob meine Zahl größer oder kleiner ist. Legen wir los...")
        else:
            print("Ok, du weißt schon wie es geht?! Legen wir also los.")
        while tipp != zahl:
            tipp = int(input("Ich habe mir eine Zahl ausgedacht, welche ist es wohl?"))
            counter+=1
            if tipp > zahl:
                print(f"Deine Antwort {tipp} ist größer als meine Zahl.")
            else:
                print(f"Deine Antwort {tipp} ist kleiner als meine Zahl.")
        print(f"Richtig!\nDein Tipp: {tipp} ist meine Zahl: {zahl}!\nHerzlichen Glückwunsch!")
        if counter <5:
            print(f"Du hast nur {counter} Versuche benötigt.")
        else:
            print(f"Du hast {counter} Versuche benötigt.")
    else:
        print("Mit Snops die sich Siezen lassen, spiele ich nicht!")
    menu_neu(name, dusie)