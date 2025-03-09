from start import start_program
from auswahl import menu

def startpunkt():
    name,dusie = start_program()
    menu(name,dusie)

startpunkt()