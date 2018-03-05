#Zahlenraten
import random
zufallszahl=(random.randint(1,100))
titel = "Willkomen beim Zahlratespiel!"
text = "Bitte versuche meine Zahl zwischen 1 und 100 zu erraten."
eingabeText= "Bitte gib deine Zahl ein: "

print(titel)
print (text)
fertig =False
anzahlderversuche=0;
while fertig == False:
    zahl = int(input(eingabeText))
    anzahlderversuche=anzahlderversuche+1
    if (zahl == zufallszahl):
        print("gewonnen")
        
        fertig = True
    elif(zahl < zufallszahl):
        print("die gesuchte zahl ist größer")
        
    else:
        print("die gfesuchte zahl ist kleiner")
    
print("super, du hast dafür nur ", anzahlderversuche, " Versuche benötigt!")
print("ende")
    
