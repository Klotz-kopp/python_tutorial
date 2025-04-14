#  Copyright (c) 2025. Diese Python Skripte wurden von mir erstellt und können als Referenz von anderen genutzt und gelesen werden.
import re
def printf(*args, sep=' ', end='\n'):
    BLUE = "\033[34m"
    RESET = "\033[0m"

    def einfärben(text):
        # Ersetzt alle Zahlen durch farbige Zahlen
        return re.sub(r'\b\d+\b', lambda m: f"{BLUE}{m.group()}{RESET}", text)

    # Alles in Strings umwandeln & einfärben
    output = [einfärben(str(arg)) for arg in args]

    print(sep.join(output), end=end)
