""" ************************************************
Der Getränkeautomat Version 6
mit __init__() und __del__()
************************************************"""
# die Vereinbarung der Klasse für die Münzeinheit
class Muenzeinheit:
    # die Methode __init__()
    def __init__(self):
        # die Attribute
        self.betrag = 0
        self.noch_zu_zahlen = 0
        self.rueckgeld = 0

    # die Methode __del__()
    def __del__(self):
        print("Eine Instanz der Klasse Muenzeinheit wurde gelöscht.")
        # die weiteren Methoden
    def muenzen_annehmen(self, wert):
        self.noch_zu_zahlen = self.noch_zu_zahlen - wert

    def rueckgeld_geben(self):
        # den absoluten Betrag von noch_zu_zahlen als Rückgeld
        # liefern
        self.rueckgeld = abs(self.noch_zu_zahlen)
        return self.rueckgeld

    def set_betrag(self, preis):
        self.betrag = preis
        self.noch_zu_zahlen = self.betrag

    def get_noch_zu_zahlen(self):
        return self.noch_zu_zahlen


# die Vereinbarung der Klasse für die Getränke
class Getraenke:

    def __init__(self, t_name, t_preis, t_anzahl):
        self.name = t_name
        self.preis = t_preis
        self.anzahl = t_anzahl


# die Vereinbarung der Klasse für den Automaten
class Getraenkeautomat:

    # übergeben werden die Anzahl und eine Referenz auf die
    # Münzeinheit
    def __init__(self, anzahl1, anzahl2, anzahl3, temp_zahlomat):

        # die Attribute
        # jetzt ist die Münzeinheit Teil des Automaten
        self.zahlomat = temp_zahlomat

        # eine leere Liste für die Getränkenamen
        self.getraenk = []

        # eine leere Liste für die Anzahl der Flaschen
        self.anzahl_flaschen = []


        # die Getränke eintragen

        self.getraenk.append("Limonade")
        self.getraenk.append("Wasser")
        self.getraenk.append("Bier")

        # die Anzahl der Flaschen
        # Sie werden jetzt durch die Argumente gesetzt
        self.anzahl_flaschen.append(anzahl1)
        self.anzahl_flaschen.append(anzahl2)
        self.anzahl_flaschen.append(anzahl3)

        # die Kühlung ist aus
        self.kuehlung = False

    def __del__(self):
        # bitte in einer Zeile eingeben
        print("Eine Instanz der Klasse Getraenkeautomat wurde gelöscht.")

    def getraenke_waehlen(self):

        # die Auswahl
        print("Bitte wählen Sie ein Getränk:")
        print("Es gibt folgende Auswahl:")

        anzeige_auswahl = 1
        for getraenk in self.getraenk:
            print(anzeige_auswahl, getraenk)
            anzeige_auswahl = anzeige_auswahl + 1

        auswahl = int(input("Geben Sie die gewünschte Nummer ein:"))


        # gibt es noch Flaschen vom gewählten Getränk?
        if self.anzahl_flaschen[auswahl - 1] != 0:

            # die Anzahl der Flaschen einlesen
            anzahl = int(input("Wie viele Flaschen möchten Sie? "))

            # erst muss bezahlt werden
            # der Preis 10 ist fest vorgegeben
            print("Sie müssen", anzahl * 10, "Cent bezahlen.")
            self.zahlomat.set_betrag(anzahl * 10)

            while self.zahlomat.get_noch_zu_zahlen() > 0:

                # bitte in einer Zeile eingeben
                print("Es fehlen noch",self.zahlomat.get_noch_zu_zahlen(), "Cent.")

                self.zahlomat.muenzen_annehmen(10)    # Zahlungsmenge

            # das Getränk ausgeben
            auswahl = auswahl - 1
            self.getraenk_ausgeben(anzahl, auswahl)

        else:
            # bitte in einer Zeile eingeben
            print("Das gewählte Getränk ist leider nicht mehr vorhanden.")
            auswahl = -1

        return auswahl

    def getraenk_ausgeben(self, anzahl, getraenke_index):

        # gibt es noch genügend Flaschen?
        if anzahl <= self.anzahl_flaschen[getraenke_index]:

            # bitte jeweils in einer Zeile eingeben
            print("Sie erhalten", anzahl, "Flasche(n)", self.getraenk[getraenke_index])
            self.anzahl_flaschen[getraenke_index] = self.anzahl_flaschen[getraenke_index] - anzahl

        else:
            # bitte in einer Zeile eingeben
            print("Es sind nur noch", self.anzahl_flaschen[getraenke_index], "Flaschen", self.getraenk[getraenke_index], "vorhanden.")
            print("Sie erhalten den Rest.")
            self.anzahl_flaschen[getraenke_index] = 0

        # Geld zurückgeben
        # bitte in einer Zeile eingeben
        print("Sie erhalten", self.zahlomat.rueckgeld_geben(), "Cent zurück.")



    def kuehlen(self, an_aus):
        self.kuehlung = an_aus

        if self.kuehlung == True:
            print("Die Kühlung ist eingeschaltet.")
        else:
            print("Die Kühlung ist ausgeschaltet.")


 # eine Münzeinheit erzeugen
einheit = Muenzeinheit()

# einen Automaten erzeugen
# die Münzeinheit und die Anzahl der Getränke werden übergeben
automat = Getraenkeautomat(10, 20, 30, einheit)
auswahl = -1

# die Kühlung einschalten
automat.kuehlen(True)

# ein Getränk auswählen
while auswahl == -1:
    auswahl = automat.getraenke_waehlen()

# die Kühlung ausschalten
automat.kuehlen(False)

# die Instanzen ausdrücklich freigeben
# zuerst den Automaten
del automat

# und die Münzeinheit
del einheit