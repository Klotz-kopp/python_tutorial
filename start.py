#  Copyright (c) 2025. Diese Python Skripte wurden von mir erstellt und können als Referenz von anderen genutzt und gelesen werden.
def start_program():
    name = input("Hallo,\nwie ist dein Name? ")
    print(f"Hallo {name},\n")

    # Gültigkeitsprüfung für 'dusie'
    while True:
        dusie = input("Soll ich 'du' oder 'Sie' sagen? ").strip()
        if dusie.lower() in ["du", "sie"]:
            break  # Gültige Eingabe -> Schleife verlassen
        print("Bitte gib nur 'du' oder 'Sie' ein.")

    return name, dusie



# Starte das Programm
#start_program()
