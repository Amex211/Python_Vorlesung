class Person:
    def __init__(self, name, datum):
        self.name = name
        self.datum = datum

    def output(self):
        return f"{self.name}, {self.datum}"

class NatuerlichePerson(Person):
    def __init__(self, vorname, nachname, gebdat):
        super().__init__(nachname,gebdat)
        self.vorname = vorname

    
    def output(self):
        s = super().output()
        s += f", {self.vorname}"
        return s

class NichtNatuerlichePerson(Person):
    def __init__(self, firmenname, firmentyp, grdat, steuernummer):
        super().__init__(firmenname, grdat)
        self.firmentyp = firmentyp        
        self.steuernummer = steuernummer
    
    def output(self):
        s = super().output()
        s += f"{self.steuernummer}"
        return s
    
def personenDatenErfassen(personenInput, plist):
    i = 0    
    while(i < int(personenInput)):
        name = input("Was ist dein Name? ")
        geb = input("Hallo " + name + " wann hast du Geburtstag? ")
        vorname = input("Was ist dein Vorname? ")
        plist.append(NatuerlichePerson(vorname,name,geb))
        print("Die Person: ist abgespeichert ")
        inp2 = input("Wollen Sie noch mehr Personen speichern? ")
        i = i + 1

    
def nichtNatürlichePersonErfassen(firmaInput, plist):
    g = 0    
    inp22 = "ja"
    while(g < int(firmaInput)):
        firmenname = input("Wie heißt deine Firma? ")
        firmentyp = input("Was macht deine Firma? ")
        gruendungsdatum = input("Wann wurde deine Firma gegründet? ")
        steuernummer = input("Wie lautet die Steuernummer? ")
        plist.append(NichtNatuerlichePerson(firmenname,firmentyp,gruendungsdatum,steuernummer))
        print("Die Firma: ist abgespeichert ")
        g = g + 1


def main():
    plist = []
    a = ""
    while(a != "x"):
        a = input("Was möchten Sie tun Datenspeichern(1), Sortieren(2), Suchen(3), Exit(x) ")
        if(a == "1"):
            inp = input("Sind Sie eine natürliche Person ja oder nein: ")
            if(inp == "ja"):
                personenInput = input("Wie viele Personen wollen Sie anlegen? ")
                personenDatenErfassen(personenInput, plist)
            if(inp == "nein"):
                firmaInput = input("Wie viele  Firmen wollen Sie anlegen? ")
                nichtNatürlichePersonErfassen(firmaInput, plist)
        elif(a == "2"):
            sortieren(plist)
            pass
        elif(a == "3"):
            #suchen()
            pass

def sortieren(plist):
    for p in plist:
        
        sorted(p.output)
        print(f"{p.output()}")
    for x in sorted(plist):
        print(x)
    

 
if __name__ == "__main__":
    main()

