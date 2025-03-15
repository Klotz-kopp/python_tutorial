#  Copyright (c) 2025. Diese Python Skripte wurden von mir erstellt und können als Referenz von anderen genutzt und gelesen werden.

from start import start_program
from auswahl import menu_neu

def startpunkt():
    name,dusie = start_program()
    menu_neu(name,dusie)

startpunkt()