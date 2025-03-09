#  Copyright (c) 2025. Diese Python Skripte wurden von mir erstellt und können als Referenz von anderen genutzt und gelesen werden.


def fahrpreis_berechnen(name, dusie):
    from auswahl import menu
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

        # Nachfrage, ob eine neue Fahrt berechnet werden soll
        if dusie.lower() == 'sie':
            nochmal = input("Möchten Sie die Kosten für eine weitere Fahrt berechnet bekommen? (ja/nein) ")
        elif dusie.lower() == 'du':
            nochmal = input("Möchtest du die Kosten für eine weitere Fahrt berechnet bekommen? (ja/nein) ")

        if nochmal.lower() != 'ja':
            menu(name, dusie)
            #print("Das Programm wird beendet.")
            #break # Beende das Programm, wenn die Antwort nicht 'ja' ist

def waehrungsrechner(name,dusie):
    from auswahl import menu
    euro = float(input("Wie viel Euro hast du? "))
    baht = float(euro * 38.06)
    print(f"Deine {euro:.2f} € sind {baht:.2f} Baht wert.")
    menu(name, dusie)

def bools(name,dusie):
    from auswahl import menu
    var1 = 40+2
    var2 = 42
    if var1 > var2:
        print(f"Variable 1 ({var1}) ist größer als Variable 2 ({var2})")
    elif var1 < var2:
        print(f"Variable 1 ({var1}) ist kleiner als Variable 2 ({var2}).")
    elif var1 == var2:
        print(f"Beide Variablen ({var1}) sind gleich.")
    menu(name, dusie)

def verkehrsmittel(name,dusie):
    from auswahl import menu
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
    menu(name,dusie)

def kinoticket(name, dusie):
    from auswahl import menu

    # Ticketpreise für jede Kategorie
    kind = 5.00
    erwachsen = 10.00
    senior = 7.50

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
    menu(name, dusie)

