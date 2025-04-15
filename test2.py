#  Copyright (c) 2025. Diese Python Skripte wurden von mir erstellt und können als Referenz von anderen genutzt und gelesen werden.

from funktionen import printf, Farben
try:
    ergebnis = 10 / 2
except ZeroDivisionError:
    printf(f"Hey, du darfst nicht durch 0 dividieren.")
except TypeError:
    printf(f"Hey, du kannst nur mit Zahlen rechnen")
except:
    printf(f"Hier ist etwas schief gelaufen")
finally:
    printf(f"{Farben['Gelb']}{ergebnis}")

printf(f"{Farben['Rot']}Hallo {Farben['Cyan']}Welt")