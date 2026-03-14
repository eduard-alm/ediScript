def stergereComentarii(line):
    poz = line.find('#')
    if poz != -1:
        line = line[:poz]
    return line

# sterge din listele facute primu element care era @ceva si scoate -> din dD
def delList(sigmaD, qD, sD, fD, dD):    
    sigmaD.pop(0)
    qD.pop(0)
    sD.pop(0)
    fD.pop(0)
    dD.pop(0)
    for i in dD:
        if i == "->":
            dD.remove("->")
    return sigmaD, qD, sD, fD, dD

def inchidereDeschidere(li):    
    li = [False, False, False, False, False]
    return li

#functie care verifica cate deschideri avem
def checkErrorDeschideri(deschis):    
    deschideri = 0
    
    for e in deschis: 
        if e == True:
            deschideri += 1
    if deschideri >= 2:
        deschideri = 0
        return True
    deschideri = 0
    return False
