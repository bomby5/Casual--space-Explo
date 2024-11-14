#anoikis exploration help tool
#by bomby_5#0001
#feel free to do whatever you want with this
#just credit me
#thanks :)

URL = "http://anoik.is/systems/"
elURL = "https://www.ellatha.com/eve/WormholeSystemview.asp?key="
dURL = "http://evemaps.dotlan.net/system/"
zkURL = "https://zkillboard.com/system/"
import time as t
import webbrowser as w
import requests as req
import json

def getSystemId(systemname):
    json_data = [
        systemname,
    ]
    raw = req.post("https://esi.evetech.net/latest/universe/ids/?datasource=tranquility&language=en", json=json_data)
    jsonv = json.loads(raw.text)
    for i in jsonv['systems']:
        return(str(i['id']))


def openSystem(systemname):
    if systemname.lower() == "thera":
        fURL = (URL+"Thera")
        f_d_URL = (dURL+"Thera")
        f_el_URL = (elURL+"Thera")
        w.open(f_d_URL)
        w.open(fURL)
        w.open(f_el_URL)
        f_zkURL = (zkURL+getSystemId("Thera"))
        w.open(f_zkURL)
    elif systemname[0].lower() != "j" or len(systemname) != 7:
        f_d_URL = (dURL+systemname)
        w.open(f_d_URL)
        f_zkURL = (zkURL+getSystemId(systemname))
        w.open(f_zkURL)
    else:
        fURL = (URL+systemname.upper())
        f_d_URL = (dURL+systemname.upper())
        f_el_URL = (elURL+systemname.upper())
        w.open(f_d_URL)
        w.open(fURL)
        w.open(f_el_URL)
        f_zkURL = (zkURL+getSystemId(systemname))
        w.open(f_zkURL)


print("Ctrl+C to exit")
try:
    while True:
        t.sleep(0.5)
        system = input("")
        openSystem(system)

except KeyboardInterrupt:
    print("Exiting")
    t.sleep(1)
