def logo():
    print("-----------------------------------------")
    print("           Notendurchschnitt")
    print("-----------------------------------------")


def abfrage():
    x = input("Wie viele Schüler und Schülerinnen haben die Klausur mitgeschrieben? ")
    return x


def schleife():
    a = input("Wie oft wurden 0 Punkte geschrieben? ")
    b = input("Wie oft wurden 1 Punkt geschrieben? ")
    c = input("Wie oft wurden 2 Punkte geschrieben? ")
    d = input("Wie oft wurden 3 Punkte geschrieben? ")
    e = input("Wie oft wurden 4 Punkte geschrieben? ")
    f = input("Wie oft wurden 5 Punkte geschrieben? ")
    g = input("Wie oft wurden 6 Punkte geschrieben? ")
    h = input("Wie oft wurden 7 Punkte geschrieben? ")
    i = input("Wie oft wurden 8 Punkte geschrieben? ")
    j = input("Wie oft wurden 9 Punkte geschrieben? ")
    k = input("Wie oft wurden 10 Punkte geschrieben? ")
    l = input("Wie oft wurden 11 Punkte geschrieben? ")
    m = input("Wie oft wurden 12 Punkte geschrieben? ")
    n = input("Wie oft wurden 13 Punkte geschrieben? ")
    o = input("Wie oft wurden 14 Punkte geschrieben? ")
    p = input("Wie oft wurden 15 Punkte geschrieben? ")


def durchschnitt():
    q = a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p
    q/x = r
    # Muss den durchschnitt mit verschiedenen angaben durchreichen


def main():
    logo()
    x = abfrage()
    a, b, c, d, e, f, g, h, i, j, k, l, m ,n ,o, p = schleife()

main()

