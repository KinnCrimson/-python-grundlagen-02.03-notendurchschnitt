def logo():
    print("-----------------------------------------")
    print("           Notendurchschnitt")
    print("-----------------------------------------")


def abfrage():
    alleschueler = int(input("Wie viele Schüler und Schülerinnen haben die Klausur mitgeschrieben? "))
    return alleschueler


def schleife(alleschueler):
    notenpunkte = 0
    gesamtpunktzahl = 0
    gesamtschueler = 0
    while notenpunkte < 16:
        aktuelleschueler = int(input(f"Wie oft wurden {notenpunkte} Punkte geschrieben? "))
        gesamtschueler = gesamtschueler + aktuelleschueler
        punktzahl = aktuelleschueler * notenpunkte
        gesamtpunktzahl = punktzahl + gesamtpunktzahl
        notenpunkte = notenpunkte + 1
    return gesamtpunktzahl, gesamtschueler


def durchschnitt(alleschueler, gesamtpunktzahl):
    ergebnis = gesamtpunktzahl / alleschueler
    return ergebnis


def durchgefallen(ergebnis):
    if ergebnis <= 5:
        print("Oh weh, wir müssen noch viel lernen!")
    elif ergebnis <=7:
        print("Da ist aber noch ordentlich Luft nach oben... ")
    elif ergebnis < 10:
        print("Kann man machen, muss man aber nicht!")
    else :
        print("Super! Der Durchschnitt ist amazing! ")


def main():
    logo()
    alleschueler = abfrage()
    gesamtschueler = 0
    while alleschueler != gesamtschueler:
        gesamtpunktzahl, gesamtschueler = schleife(alleschueler)
        if alleschueler != gesamtschueler:
            print("Sie haben einen Fehler gemacht, die eingegebenen Schüleranzahl ist ungleich mit der gesamten Schüleranzahl! ")
    ergebnis = durchschnitt(alleschueler, gesamtpunktzahl)
    print(f"Der Durchschnitt in dieser Klausur lautet {ergebnis} Punkte.")
    durchgefallen(ergebnis)


main()

