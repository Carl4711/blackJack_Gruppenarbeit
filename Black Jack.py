from nicegui import ui
from pathlib import Path
from uuid import uuid4
import os
import random


kartenstapel = []
spielerhand = []
dealerhand = []

dateinamen = os.listdir(Path(__file__).resolve().parent / "bilder")
for d in dateinamen:     
    kartenstapel.append("/images/" + d)
random.shuffle(kartenstapel)
spielerhand.append(kartenstapel.pop())
spielerhand.append(kartenstapel.pop())
dealerhand.append(kartenstapel.pop())
dealerhand.append(kartenstapel.pop())
print(kartenstapel)
print("Spielerhand:", spielerhand)
print("Dealerhand:", dealerhand)

def WertErmitteln(spielerhand):
    
    wert = 0
    
    for x in spielerhand:
        if "2" in x:
            wert = wert + 2
        if "3" in x:
            wert = wert + 3
        if "4" in x:
            wert = wert + 4
        if "5" in x:
            wert = wert + 5
        if "6" in x:
            wert = wert + 6
        if "7" in x:
            wert = wert + 7
        if "8" in x:
            wert = wert + 8
        if "9" in x:
            wert = wert + 9
        if "10" in x:
            wert = wert + 10
        if "bube" in x:
            wert = wert + 10
        if "queen" in x:
            wert = wert + 10
        if "king" in x:
            wert = wert + 10

    print(wert)
    
def ziehen():
    global spielerhand
    spielerhand.append(kartenstapel.pop())

WertErmitteln(spielerhand)

ui.label('Hello NiceGUI!')
ui.run()

        
