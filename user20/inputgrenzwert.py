g = 300
oben = 400
unten = 100
eingabe = input("Bitte eine Zahl eingeben: ")
try:
    zahl = int(eingabe)
    res = True
except ValueError:
    print("Bitte eine ZAHL eingeben!!")
    res = False
if res:
    if zahl < g:
        print("Zahl kleiner als Grenzwert")
    elif zahl > g:
        print("Zahl ist größer als Grenzwert")
    else:
        print("Zahl und Grenzwert sind gleich groß")
    if(unten < zahl < oben):
        print("Eingegebene Zahl liegt innerhalb des Bereiches.")
    else:
        print("Eingegebene Zahl liegt außerhalb des Bereiches.")