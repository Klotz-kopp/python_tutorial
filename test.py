#  Copyright (c) 2025. Diese Python Skripte wurden von mir erstellt und können als Referenz von anderen genutzt und gelesen werden.
#from auswahl import clear_screen

""" Diese Datei wird zum experementieren genutzt, in der Regel werden neue Programme / Funktionen hier geschrieben und getestet
 bevor Sie in die programme.py übernommen werden"""
from dataclasses import replace
import re
from funktionen import printf, Farben
def schon_wieder_einkaufsliste(name, dusie):

    einkaufsliste = []

    while True:
        aktion = input("Was möchtest du mit deiner Einkaufsliste tun? (hinzufügen / entfernen / ansehen / beenden)? ")

        #hinzufügen
        if aktion == 'hinzufügen':
            einkaufsliste.append(input("Was möchtest du deiner Liste hinzufügen? "))

        #ansehen
        elif aktion == 'ansehen':
            printf(f"Dies ist deine aktuelle {einkaufsliste}.")

        #entfernen
        elif aktion == 'entfernen':
            artikel = input("Welchen Artikel möchtest du entfernen?")
            if artikel in einkaufsliste:
                einkaufsliste.remove(artikel)
                printf(f"{artikel} von der Einkaufsliste entfernt.")
            else:
                printf(f"Der Artikel {artikel} ist nicht auf deiner Einkaufsliste.")

        #beenden
        elif aktion == 'beenden':
            printf("Tschüss!")
            break
        else:
            printf(f"Dein Eingabe {aktion} ist leider nicht korrekt.\nBitte nur hinzufügen, entfernen, ansehen oder beenden wählen.")

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
            printf("Alles klar, die Regeln sind sehr einfach. Ich denke mir eine Zahl aus, und du musst versuchen diese Zahl zu erraten.\nKeine Angst, ich nehme nur Zahlen zwischen 1 und 100.\nUnd ich bin nett, immer wenn deine Antwort nicht richtig ist, gebe ich dir einen Hinweis, ob meine Zahl größer oder kleiner ist. Legen wir los...")
        else:
            printf("Ok, du weißt schon wie es geht?! Legen wir also los.")
        while tipp != zahl:
            tipp = int(input("Ich habe mir eine Zahl ausgedacht, welche ist es wohl?"))
            counter+=1
            if tipp > zahl:
                printf(f"Deine Antwort {tipp} ist größer als meine Zahl.")
            else:
                printf(f"Deine Antwort {tipp} ist kleiner als meine Zahl.")
        printf(f"Richtig!\nDein Tipp: {tipp} ist meine Zahl: {zahl}!\nHerzlichen Glückwunsch!")
        if counter <5:
            printf(f"Du hast nur {counter} Versuche benötigt.")
        else:
            printf(f"Du hast {counter} Versuche benötigt.")
    else:
        printf("Mit Snops die sich Siezen lassen, spiele ich nicht!")
    menu_neu(name, dusie)

zahlen_raten("Simon", "du")

""" Template für neue Programme:

def programmname(name, dusie):
    # beschreibung: TEXT
    from auswahl import menu_neu

    menu_neu(name, dusie)

"""
