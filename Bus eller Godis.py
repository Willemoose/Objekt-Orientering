import random

bus = 0
poäng = 0
godis = 0
i = 0
sannolikhet = int(input("1 - 100% chanse att få godis vid besök: "))

def busellergodis(odds):
    tal = random.randint(1,101)
    if tal < odds + 1:
        return(1)
    else:
        return(2)

besök = int(input("Hur många hus vill du besöka: "))
while i < besök:
    x = busellergodis(sannolikhet)
    if x == 1:
        godis += 1
        poäng += 2
    else:
        bus += 1
        poäng += -1
    i += 1

totpoäng = besök * 2
print("Antalet godis du fick:", godis)
print("Antalet bus du genomförde:", bus)
print("Antalet hus du besökte:", besök)
print("Totala poäng", poäng, "av", totpoäng)
        
    
