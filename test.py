#  Copyright (c) 2025. Diese Python Skripte wurden von mir erstellt und können als Referenz von anderen genutzt und gelesen werden.
#from auswahl import clear_screen

""" Diese Datei wird zum experementieren genutzt, in der Regel werden neue Programme / Funktionen hier geschrieben und getestet
 bevor Sie in die programme.py übernommen werden"""

def tiere_raten(name, dusie):
    counter = 1
    limit = int(input("Wie weit soll ich zählen? "))
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
            case _:
                print("Ich glaube ich habe mich verzählt!")
        counter+=1
    print("Das wars...")

tiere_raten("Simon", "du")

""" Template für neue Programme:

def programmname(name, dusie):
    # beschreibung: TEXT
    from auswahl import menu_neu

    menu_neu(name, dusie)

"""
