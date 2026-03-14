from node import Nod
import sys

def objCreate(dD):
    noduri = {}

    for i in range(0, len(dD), 3):   
        nume = dD[i]
        val = dD[i+1]
        directie = dD[i+2]

        if nume not in noduri:
            noduri[nume] = Nod(nume)
        if directie not in noduri:
            noduri[directie] = Nod(directie)
        noduri[nume].directie(val, noduri[directie])

    return noduri


def run(sD, string, sigmaD, noduri):
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

    return locatie

def interpretare(locatie, fD):
    final = locatie.name
    for c in fD:
        if c == final:
            print(f"True pentru {c}")
        else:
            print(f"False pentru {c}")

