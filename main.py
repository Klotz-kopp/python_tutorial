#  Copyright (c) 2025. Diese Python Skripte wurden von mir erstellt und können als Referenz von anderen genutzt und gelesen werden.

""" Diese Datei dient nur als Start des Programms - es wird zuerst start.py aufgerufen und dann das Menü geladen """

from start import start_program
from auswahl import menu_neu

def startpunkt():
    name,dusie = start_program()
    menu_neu(name,dusie)

startpunkt()