URL = "http://anoik.is/systems/"
ZURL = "https://zkillboard.com/system/"
import time as t
import webbrowser as w

while True:
    system = input("")
    if system.lower() == "thera":
        w.open("http://anoik.is/systems/Thera")
    elif len(system) != 7:
        print("Invalid System Name")
        continue
    elif system[0].lower() != "j":
        print ("Invalid System Name")
        continue
    else:
        fURL = (URL+system.upper())
        w.open(fURL)
        t.sleep(0.5)

