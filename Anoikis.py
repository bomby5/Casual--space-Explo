#anoikis exploration help tool
#by bomby_5#0001
#feel free to do whatever you want with this
#just credit me
#thanks :)

URL = "http://anoik.is/systems/"
dURL = "http://evemaps.dotlan.net/system/"
zkURL = "https://zkillboard.com/system/"
import time as t
import webbrowser as w

def openSystem(systemname):
    if systemname == "Thera":
        fURL = (URL+"Thera")
        f_d_URL = (dURL+"Thera")
        w.open(f_d_URL)
        w.open(fURL)
    elif systemname[0].lower() != "j" or len(systemname) != 7:
        f_d_URL = (dURL+systemname)
        w.open(f_d_URL)
    else:
        fURL = (URL+systemname.upper())
        f_d_URL = (dURL+systemname.upper())
        w.open(f_d_URL)
        w.open(fURL)


print("Ctrl+C to exit")
try:
    while True:
        t.sleep(0.5)
        system = input("")
        openSystem(system)
#TODO: Zkill Integration(how do i convert systems to system ids)

except KeyboardInterrupt:
    print("Exiting")
