#  Copyright (c) 2025. Diese Python Skripte wurden von mir erstellt und können als Referenz von anderen genutzt und gelesen werden.

""" Diese Datei enthält alle Mini Programme welche im Rahmen des / der Youtube Tutorials erstellt wurden.
Konventionen:   - alle Programme sind in einer eigenen Funktion
                - alle Programme werden mit der Übergabe der Variablen 'name' & 'pronomen' gestartet, auch wenn nicht, benutzt
                - alle Programme haben in der ersten Zeile ein Kommentar welcher beginnt mit '# beschreibung: ' gefolgt von einer
                  Beschreibung des Programms welches später den entsprechenden Menüpunkt bildet, dies ist nötig damit
                  das Menü automatisch erstellt werden kann
                - alle Programme starten mit 'from auswahl import menu_neu' und enden mit 'menu_neu(name, pronomen)' damit
                  beim Beenden das Menü erneut aufgerufen wird.
                Live Template progtemp"""

import xml.etree.ElementTree as ET

import requests

from funktionen import printf


def fahrpreis_berechnen(name, pronomen):
    # beschreibung: für den Taxameter welcher dir den Preis für eine Taxifahrt berechnet
    from auswahl import menu_neu
    printf(
        f"Hallo {name},\nherzlich willkommen beim Taxameter.\nDer Taxameter soll den voraussichtlichen Fahrpreis für eine Taxifahrt ermitteln.\nFangen wir an.")
    while True:
        if pronomen.lower() == 'sie':
            km = input("Wie viele Kilometer möchten Sie fahren? ")
        elif pronomen.lower() == 'du':
            km = input("Wie viele Kilometer möchtest du fahren? ")
        else:
            printf("Ungültige Eingabe, bitte 'du' oder 'Sie' wählen.")
            return

        basispreis = 2.5
        km_preis = 1.75

        # Leetspeak für eine spezielle Eingabe (1337)
        if km == "1337":
            printf("Für j3m4nd3n d3r s0 l33t 1st w13 du, 1st d13 T0ur gr4t1s")
        else:
            try:
                km = float(km)
                fahrpreis = basispreis + (km * km_preis)
                printf(f"Die gewählte Strecke von {km} Kilometern wird voraussichtlich {fahrpreis:.2f}€ kosten.")
            except ValueError:
                printf("Ungültige Eingabe. Bitte eine gültige Zahl für die Kilometeranzahl eingeben.")
                continue  # Bei ungültiger Eingabe zurück zur Kilometerabfrage
        nochmal = "ja"
        # Nachfrage, ob eine neue Fahrt berechnet werden soll
        if pronomen.lower() == 'sie':
            nochmal = input("Möchten Sie die Kosten für eine weitere Fahrt berechnet bekommen? (ja/nein) ")
        elif pronomen.lower() == 'du':
            nochmal = input("Möchtest du die Kosten für eine weitere Fahrt berechnet bekommen? (ja/nein) ")

        if nochmal.lower() != 'ja':
            menu_neu(name,
                     pronomen)  # printf("Das Programm wird beendet.") # break # Beende das Programm, wenn die Antwort nicht 'ja' ist


def waehrungsrechner(name, pronomen):
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
            printf("Der Wechselkurs für den thailändischen Baht konnte nicht gefunden werden.")
            return

        # Benutzerabfrage für den Euro-Betrag
        euro = float(input("Wie viel Euro möchten Sie umrechnen? "))
        baht = euro * baht_kurs
        printf(f"Ihre {euro:.2f} € sind {baht:.2f} Baht wert (Wechselkurs: 1 € = {baht_kurs:.2f} THB).")

    except requests.RequestException as e:
        printf(f"Fehler beim Abrufen der Wechselkurse: {e}")
    except ET.ParseError:
        printf("Fehler beim Verarbeiten der XML-Daten.")
    except ValueError:
        printf("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")

    # Rückkehr zum Hauptmenü
    menu_neu(name, pronomen)


def bools(name, pronomen):
    # beschreibung: für die Wahrheitsprüfung einer hard codierte Variable
    from auswahl import menu_neu
    var1 = 40 + 2
    var2 = 42
    if var1 > var2:
        printf(f"Variable 1 ({var1}) ist größer als Variable 2 ({var2})")
    elif var1 < var2:
        printf(f"Variable 1 ({var1}) ist kleiner als Variable 2 ({var2}).")
    elif var1 == var2:
        printf(f"Beide Variablen ({var1}) sind gleich.")
    menu_neu(name, pronomen)


def verkehrsmittel(name, pronomen):
    # beschreibung: für eine Empfehlung welches Verkehrsmittel genutzt werden sollte
    from auswahl import menu_neu
    strecke = int(input(f"Wie weit ist deine Strecke in Kilometer?"))
    if strecke < 3:
        printf(f"Deine {strecke} km lange Strecke kannst du zu Fuß gehen")
    elif 3 < strecke < 20:
        printf(f"Deine {strecke} km lange Strecke kannst du mit dem Fahrrad zurück legen.")
    elif strecke == 3:
        printf(
            f"Deine {strecke} km lange Strecke kannst du sowohl mit dem Fahrrad als auch zu Fuß zurücklegen,\nganz nach belieben.")
    elif strecke == 42:
        printf("Schnapp dir dein Handtuch und halt den Daumen raus.")
    elif strecke > 20:
        printf(f"Deine {strecke} km lange Strecke solltest du mit den Öfis oder dem Auto zurück legen.")
    menu_neu(name, pronomen)


def kinoticket(name, pronomen):
    # beschreibung: für unseren alten Kinoticket Automaten
    from auswahl import menu_neu

    # Ticketpreise für jede Kategorie
    kind = 5.00
    erwachsen = 10.00
    senior = 7.50
    preis = 0
    # Eingabe des Alters
    try:
        alter = int(input(
            f"Hallo {name},\nwir bieten in unserem Kino drei Preiskategorien an.\n1.) Kind\n2.) Erwachsene\n3.) Senioren\nBitte gib das Alter der Kinobesucher an: "))
    except ValueError:
        printf("Bitte gib ein gültiges Alter ein.")
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
            printf("Die Anzahl der Tickets muss größer als 0 sein.")
            return
    except ValueError:
        printf("Bitte gib eine gültige Anzahl an Tickets ein.")
        return

    # Berechnung des Preises basierend auf der Kategorie
    if kategorie == "kind":
        preis = menge * kind
    elif kategorie == "erwachsen":
        preis = menge * erwachsen
    elif kategorie == "senior":
        preis = menge * senior

    # Ausgabe der Rechnung
    if pronomen == 'du':
        printf(
            f"Die {menge} Kinotickets in der Kategorie {kategorie} kosten dich {preis:.2f}€. Bitte an Schalter 2 bezahlen.\nVielen Dank für deinen Besuch in unserem Kino.")
    else:
        printf(
            f"Die {menge} Kinotickets in der Kategorie {kategorie} kosten Sie {preis:.2f}€. Bitte zahlen Sie an Schalter 3.\nWir danken Ihnen für Ihren Besuch in unserem Kino.")

    # Zurück zum Menü
    menu_neu(name, pronomen)


def einkaufszettel(name, pronomen):
    # beschreibung: um einen Einkaufszettel zu erstellen
    from auswahl import menu_neu
    einkaufszettel = []
    printf(f"Hallo {name},\nlass uns einen Einkaufszettel schreiben.\nAktuell ist dein Einkaufszettel leer.")

    while True:
        auswahl = input("Möchtest du etwas hinzufügen, entfernen, ansehen oder beenden? ").strip().lower()

        if auswahl == 'hinzufügen':
            item = input("Was möchtest du hinzufügen? ").strip()
            einkaufszettel.append(item)
            printf(f"{item} wurde hinzugefügt.")

        elif auswahl == 'entfernen':
            item = input("Was möchtest du entfernen? ").strip()
            if item in einkaufszettel:
                einkaufszettel.remove(item)
                printf(f"{item} wurde entfernt.")
            else:
                printf(f"{item} ist nicht auf dem Einkaufszettel.")

        elif auswahl == 'ansehen':
            if not einkaufszettel:
                printf("Dein Einkaufszettel ist noch leer.")
            else:
                printf("Aktueller Einkaufszettel:")
                for index, item in enumerate(einkaufszettel, start=1):
                    printf(f"{index}. {item}")

        elif auswahl == 'beenden':
            printf("Auf Wiedersehen!")
            break

        else:
            printf("Ungültige Auswahl. Bitte wähle 'hinzufügen', 'entfernen', 'ansehen' oder 'beenden'.")

    # Zurück zum Menü
    menu_neu(name, pronomen)


def kinoticket2(name, pronomen):
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
    senior = Ticket('Senior', 65, 120, 7.5)
    anzahl = int(input(
        f"Hallo {name},\nWillkommen an unserem Kinoticket Verkaufsautomaten.\nWie viele Personen möchten gerne ins Kino?"))
    i = 0
    gesamtpreis = 0
    while i < anzahl:
        alter = int(input(f"Wie alt ist Person Nummer {i + 1}?"))
        if kind.alter_start <= alter <= kind.alter_ende:
            gesamtpreis += kind.preis
        elif erwachsener.alter_start <= alter <= erwachsener.alter_ende:
            gesamtpreis += erwachsener.preis
        elif senior.alter_start <= alter <= senior.alter_ende:
            gesamtpreis += senior.preis
        else:
            gesamtpreis += 0
            printf("Freiticket!")
        i += 1
    printf(
        f"Der Kinobesuch kostet eure {anzahl} köpfige Besuchergruppe: {gesamtpreis:.2f} €\nWir wünschen euch viel Spaß.")

    # Zurück zum Menü
    menu_neu(name, pronomen)


def weihnachtsbaum(name, pronomen):
    # beschreibung: um einen schönen Weihnachtsbaum zu bekommen
    from auswahl import menu_neu

    printf(
        f"Hallo {name},\nschön dass {pronomen} hier {'bist' if pronomen == 'du' else 'sind'}\nIch habe eine Weihnachtsbaum für {'dich' if pronomen == 'du' else 'Sie'}.")
    groesse = int(input("Wie groß soll der Weihnachtsbaum werden? (1-99) "))
    groesse += 1
    if name[-1] == 's':
        printf(f"Hier ist {name}' Weihnachtsbaum:")
    else:
        printf(f"Hier ist {name}'s Weihnachtsbaum:")

    for i in range(1, groesse):
        x = 2 * i - 1
        y = len(range(1, groesse)) - i
        printf(y * " " + x * "*")
    y = len(range(1, groesse)) - 1
    printf(y * " " + "*")
    if input("Möchtest du einen weiteren Weihnachtsbaum? (ja/nein)") == "ja":
        weihnachtsbaum(name, pronomen)
    else:
        menu_neu(name, pronomen)


def tiere_raten(name, pronomen):
    # beschreibung: ein Tierkategoriesierer
    from auswahl import menu_neu
    tier = input("Bitte nenne ein Tier: ").capitalize()
    match tier:
        case "Hund" | "Katze" | "Goldfisch":
            printf(f"{tier} ist ein Haustier.")
        case "Fliege" | "Biene" | "Wespe":
            printf(f"{tier} ist ein Fliegevieh.")
        case "Reh" | "Hirsch" | "Wildschwein":
            printf(f"{tier} ist ein Wildtier.")
        case "Kuh" | "Schwein" | "Schaf":
            printf(f"{tier} ist ein Nutztier.")
        case "Berta":
            printf(f"{tier} ist der süßeste Hunde den von wo gibt!")
        case "Mücke" | "Schabe" | "Maulwurf":
            printf(f"Ich fragte nach einem Tier\n{tier} ist ein Untier (vgl. Kraut und Unkraut)")
        case _ if tier == name:
            printf("Das ist mein süßer Schatz")
        case _:
            printf(f"{tier} kenne ich leider nicht, ich bin ja auch nur ein dummer Computer.")

    menu_neu(name, pronomen)


def zaehlen(name, pronomen):
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
                    printf("Null")
                case 1:
                    printf("Eins")
                case 2:
                    printf("Zwei")
                case 3:
                    printf("Drei")
                case 4:
                    printf("Vier")
                case 5:
                    printf("Fünf")
                case 42:
                    printf("Dies ist die Antwort auf die Frage nach dem Leben, dem Universum und dem ganzen Rest.")
                case _:
                    printf("Ich glaube ich habe mich verzählt!")
            counter += 1

        printf("Das wars...")

        # Nachfrage für Wiederholung
        nochmal = input("Nochmal zählen? (j/n): ").lower() == "j"

    # Rückkehr zum Menü
    menu_neu(name, pronomen)


def zahlen_raten(name, pronomen):
    # beschreibung: Das Zahlenrate Spiel
    from auswahl import menu_neu
    from random import randint
    zahl = randint(1, 100)
    tipp = 0
    counter = 0
    if pronomen == 'du':
        regeln_ansehen = input(
            f"Hallo {name},\nWillkommen beim Zahlen rate Spiel.\nMöchtest du die Spielregel sehen? (j/n) ")
        if regeln_ansehen == 'j':
            printf(
                "Alles klar, die Regeln sind sehr einfach. Ich denke mir eine Zahl aus, und du musst versuchen diese Zahl zu erraten.\nKeine Angst, ich nehme nur Zahlen zwischen 1 und 100.\nUnd ich bin nett, immer wenn deine Antwort nicht richtig ist, gebe ich dir einen Hinweis, ob meine Zahl größer oder kleiner ist. Legen wir los...")
        else:
            printf("Ok, du weißt schon wie es geht?! Legen wir also los.")
        while tipp != zahl:
            tipp = int(input("Ich habe mir eine Zahl ausgedacht, welche ist es wohl?"))
            counter += 1
            if tipp > zahl:
                printf(f"Deine Antwort {tipp} ist größer als meine Zahl.")
            else:
                printf(f"Deine Antwort {tipp} ist kleiner als meine Zahl.")
        printf(f"Richtig!\nDein Tipp: {tipp} ist meine Zahl: {zahl}!\nHerzlichen Glückwunsch!")
        if counter < 5:
            printf(f"Du hast nur {counter} Versuche benötigt.")
        else:
            printf(f"Du hast {counter} Versuche benötigt.")
    else:
        printf("Mit Snops die sich Siezen lassen, spiele ich nicht!")
    menu_neu(name, pronomen)


def tic_tac_toe(name, pronomen):
    # beschreibung: Lust auf eine Runde Tic Tac Toe?
    from auswahl import menu_neu
    from großes_programm import spiele_tic_tac_toe
    spiele_tic_tac_toe(name, pronomen)
    menu_neu(name, pronomen)
