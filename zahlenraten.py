#Zahlenraten
import random
titel = "Willkomen beim Zahlratespiel!"
print(titel)



von = int(input("Bitte eine ZUfallszahlunterschranke festlegen"))
bis = int(input(" Bitte die Zufallszahl Oberschranke festlegen"))
zufallszahl=(random.randint(von , bis))
text = "Bitte versuche meine Zahl zwischen",von, "und " ,bis, " zu erraten."
print(text)
eingabeText= "Bitte gib deine Zahl ein: "
anzahlderversuche=0;
fertig =False

while fertig == False:
    zahl = int(input(eingabeText))
    anzahlderversuche=anzahlderversuche+1
    if (zahl == zufallszahl):
        print("gewonnen")

        fertig = True
    elif(zahl < zufallszahl):
        print("die gesuchte zahl ist größer")

    else:
        print("die gesuchte zahl ist kleiner")

print("super, du hast dafür nur ", anzahlderversuche, " Versuche benötigt!")
print("ende")
