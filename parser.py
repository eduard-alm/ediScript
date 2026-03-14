import argparse
import sys

import utils


def parser():
    argumente = argparse.ArgumentParser()
    argumente.add_argument("-f", "--file", required=True, help="Fisierul de intrare")
    args = argumente.parse_args()

    file = args.file
    if not file.endswith(".ediS"):
        print("Fisier de intrare gresit!")
        sys.exit(1)

    sigmaD = []
    qD = []
    sD = []
    fD = []
    dD = []
    deschis = [False, False, False, False, False]
    string = []
    first = True

    with open(file, "r") as fisier:
        for line in fisier:
            lineF = utils.stergereComentarii(line.strip())

            if lineF == "":
                continue

            if first:
                first = False
                for c in lineF[2::]:
                    string.append(c)

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
                deschis = utils.inchidereDeschidere(deschis)

            for c in lineF.split():
                if deschis[0] is True:
                    sigmaD.append(c)
                if deschis[1] is True:
                    qD.append(c)
                if deschis[2] is True:
                    sD.append(c)
                if deschis[3] is True:
                    fD.append(c)
                if deschis[4] is True:
                    dD.append(c)

            if utils.checkErrorDeschideri(deschis) is True:
                print("Eroare la deschieri!")
                sys.exit(1)

    sigmaD, qD, sD, fD, dD = utils.delList(sigmaD, qD, sD, fD, dD)

    return {
        "sigmaD": sigmaD,
        "qD": qD,
        "sD": sD,
        "fD": fD,
        "dD": dD,
        "string": string,
    }
