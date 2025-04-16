#  Copyright (c) 2025. Diese Python Skripte wurden von mir erstellt und können als Referenz von anderen genutzt und gelesen werden.

from funktionen import printf, Farben
"""try:
    ergebnis = 10 / 2
except ZeroDivisionError:
    printf(f"Hey, du darfst nicht durch 0 dividieren.")
except TypeError:
    printf(f"Hey, du kannst nur mit Zahlen rechnen")
except:
    printf(f"Hier ist etwas schief gelaufen")
finally:
    printf(f"{Farben['Gelb']}{ergebnis}")

printf(f"{Farben['Rot']}Hallo {Farben['Cyan']}Welt{Farben['Reset']}")"""


def oop():
    class Auto():
        def __init__(self, marke, modell, baujahr, tueren, farbe,ps):
            self.marke = str(marke)
            self.modell = str(modell)
            self.baujahr = int(baujahr)
            self.raeder = 4
            self.tueren = int(tueren)
            self.farbe = str(farbe)
            self.ps = int(ps)

        def begruessung(self):
            printf(f"Hallo mein lieber Fahrer, ich bin {self.modell}.")

        def fahren(self):
            printf(f"Brum Brum " * int(self.ps/10))

    auto1 = Auto('Seat', 'Leon', '2012', 4, 'schwarz', 140)

    printf(f"Mein erstes Auto war ein {auto1.marke} {auto1.modell}, Baujahr {auto1.baujahr} mit {auto1.tueren} Türen in {auto1.farbe}.")
    auto1.begruessung()
    auto1.fahren()
    class Sportwagen(Auto):
        def __init__(self, marke, modell, baujahr, tueren, farbe,ps, beschleunigung):
            super().__init__(marke,modell,baujahr,tueren,farbe,ps)
            self.beschleunigung = beschleunigung
        def fahren(self):
            printf(f"{Farben['Rot']}Brum Brum " * int(self.ps/100*self.beschleunigung)+Farben['Reset'])
    auto2 = Sportwagen("Cupra", "Leon", 2024, 4,'rot', 327,6.7)
    auto2.begruessung()
    auto2.fahren()
oop()




