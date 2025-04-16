#  Copyright (c) 2025. Diese Python Skripte wurden von mir erstellt und können als Referenz von anderen genutzt und gelesen werden.

""" Diese Datei dient nur als Start des Programms - es wird zuerst start.py aufgerufen und dann das Menü geladen """
import logging

from auswahl import menu_neu
from start import start_program

# Logging konfigurieren
logging.basicConfig(
    filename='fehlerlog.txt',  # Name der Logdatei
    level=logging.ERROR,  # Nur Fehler (ERROR) und schwerwiegendere Nachrichten protokollieren
    format='%(asctime)s - %(levelname)s - %(message)s',  # Format der Lognachricht
)


def startpunkt():
    try:
        name, dusie = start_program()
        menu_neu(name, dusie)
    except Exception as e:
        # Fehler wird ins Log geschrieben
        logging.error(f'Fehler: {e}', exc_info=True)


startpunkt()
