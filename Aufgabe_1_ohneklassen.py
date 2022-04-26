from array import array
from datetime import date
from multiprocessing.dummy import Array
from datetime import datetime

def personenDaten():
    inp = input("Sind Sie eine natürliche Person ja oder nein: ")
    Personenlist = []
    Firmalist = []
    inp2 = "ja"
    if(inp == "ja"):
        while(inp2 == "ja"):
            name = input("Was ist dein Name? ")
            geb = input("Hallo " + name + " wann hast du Geburtstag? ")
            alter = input("Wie alt bist du " + name + "? ")
            Personenlist.append([name,geb, alter])
            print("Die Person: " + str(Personenlist) + " ist abgespeichert")
            inp2 = input("Wollen Sie noch mehr Personen speichern? ")
    else:
        inp22 = "ja"
        while(inp22 == "ja"):
            firmenname = input("Wie heißt deine Firma? ")
            firmentyp = input("Was macht deine Firma? ")
            gruendungsdatum = input("Wann wurde deine Firma gegründet? ")
            steuernummer = input("Wie lautet die Steuernummer? ")
            Firmalist.append([firmenname,firmentyp,gruendungsdatum,steuernummer])
            print("Die Firma: " + str(Firmalist) + " ist abgespeichert")
            inp22 = input("Wollen Sie noch mehr Firmen speichern? ")

    return Personenlist, Firmalist


def sortieren(personenListe, firmenListe):
    inp10 = input("Möchten Sie die Liste Alphabetisch sortieren: ")
    if(inp10 == "1"):
        print(sorted(personenListe))
    
    

def suchen():
    print("suchen")

def main():
    plist = []
    flist = []
 
    a = "1"
    while(a != "x"):
        a = input("Was möchten Sie tun Datenspeichern(1), Sortieren(2), Suchen(3), Exit(x) ")
        if(a=="1"):
            plist, flist = personenDaten()
        elif(a == "2"):
            sortieren(plist, flist)
        elif(a == "3"):
            suchen()

if __name__ == "__main__":
    main()
    
    