import sys
import argparse

#definim argumentul -f
parser = argparse.ArgumentParser()           
parser.add_argument("-f", "--file", required=True, help="Fisierul de intrare")
args = parser.parse_args()

#verifica extensia
file = args.file                        
if file[2::] != ".ediS":
    print("Fisier de intrare gresit!")          
    sys.exit(1)

#scoate tot dupa #, comentariile
def check(line):
    poz = line.find('#')
    if poz != -1:
        line = line[:poz]
    return line

#functie care verifica cate deschideri avem
def checkErrorDeschideri():    
    deschideri = 0
    
    for e in deschis: 
        if e == True:
            deschideri += 1
    if deschideri >= 2:
        deschideri = 0
        return True
    deschideri = 0
    return False

#daca este un @end lista dispare
def inchidereDeschidere(li):    
    li = [False, False, False, False, False]
    return li

# sterge din listele facute primu element care era @ceva si scoate -> din dD
def delList():    
    sigmaD.pop(0)
    qD.pop(0)
    sD.pop(0)
    fD.pop(0)
    dD.pop(0)
    for i in dD:
        if i == "->":
            dD.remove("->")

#variabile care tin valorile din deschideri
sigmaD = [] 
qD = []   
sD = []
fD = []
dD = []
#lista pt verificare la deschideri
deschis = [False, False, False, False, False]
string = []
first = True      # prima linie 

#deschidem fisierul
with open(file, "r") as file:
    for line in file:
        lineF = check(line.strip())

        #verificam prima linie
        if first:
            first = False
            for c in lineF[2::]:
                string.append(c)
            
        #verificam daca urmeaza sa citim date
        if "@sigma" in lineF:
            deschis[0] = True
        if "@nodes" in lineF:
            deschis[1] = True
        if "@start" in lineF:
            deschis[2] = True
        if "@final" in lineF:
            deschis[3] = True
        if "@rules" in lineF:
            deschis[4] = True
        if "@end" in lineF:
            deschis = inchidereDeschidere(deschis)

        #daca suntem in interior citim date si le punem in listele
        for c in lineF.split():
            if deschis[0] == True:
                sigmaD.append(c)
            if deschis[1] == True:
                qD.append(c)
            if deschis[2] == True:
                sD.append(c)
            if deschis[3] == True:
                fD.append(c)
            if deschis[4] == True:
                dD.append(c)

        #daca a fost o deschidere si nu a fost inchisa exista eroare
        if checkErrorDeschideri() == True:
            print("Eroare la deschieri!")
            sys.exit(1)

delList()      #del la primul elem din lista

#obiectul nod
class Nod:    
    def __init__(self, name):
        self.name = name
        self.trimiteri = {}
    def directie(self, cod, destinatie):
        self.trimiteri[cod] = destinatie
        
noduri = {}     #dict de obiecte

#for pentru creearea de obiecte
for i in range(0, len(dD), 3):   
    nume = dD[i]
    val = dD[i+1]
    directie = dD[i+2]

    if nume not in noduri:
        noduri[nume] = Nod(nume)
    if directie not in noduri:
        noduri[directie] = Nod(directie)
    noduri[nume].directie(val, noduri[directie])


start = sD[0]
locatie = noduri[start]   #practic primul nod

#pt fiecare litera din string
print(start, end="")
for c in string:
    if c not in sigmaD:
        print(f"Caracterul {c} nu exista in string")
        sys.exit(1)
    #next primeste directia
    next = locatie.trimiteri[c]
    locatie = next
    print(" -> ", locatie.name, end="", sep="")
print()

#verificam
final = locatie.name
for c in fD:
    if c == final:
        print(f"True pentru {c}")
    else:
        print(f"False pentru {c}")
