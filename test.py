#  Copyright (c) 2025. Diese Python Skripte wurden von mir erstellt und können als Referenz von anderen genutzt und gelesen werden.
#from auswahl import clear_screen


def tiere_raten(name, dusie):
    #from auswahl import menu_neu
    tier = input("Bitte nenne ein Tier: ").capitalize()
    match tier:
        case "Hund" | "Katze" | "Goldfisch":
            print(f"{tier} ist ein Haustier.")
        case "Fliege" | "Biene" | "Wespe":
            print(f"{tier} ist ein Fliegevieh.")
        case "Reh" | "Hirsch" | "Wildschwein":
            print(f"{tier} ist ein Wildtier.")
        case "Kuh" | "Schwein" | "Schaf":
            print(f"{tier} ist ein Nutztier.")
        case "Berta":
            print(f"{tier} ist der süßeste Hunde den von wo gibt!")
        case "Mücke" | "Schabe" | "Maulwurf":
            print(f"Ich fragte nach einem Tier\n{tier} ist ein Untier (vgl. Kraut und Unkraut)")
        case _ if tier == name:
            print("Das ist mein süßer Schatz")
        case _:
            print(f"{tier} kenne ich leider nicht, ich bin ja auch nur ein dummer Computer.")

tiere_raten("Simon", "du")