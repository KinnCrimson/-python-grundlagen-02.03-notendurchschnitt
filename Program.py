def logo():
    print("-----------------------------------------")
    print("           Notendurchschnitt")
    print("-----------------------------------------")


def abfrage():
    x = input("Wie viele Schüler und Schülerinnen haben die Klausur mitgeschrieben? ")
    return x

def main():
    logo()
    x = abfrage()

main()

