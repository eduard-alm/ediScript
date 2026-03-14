import mecanica
import parser

def main():
    date = parser.parser()
    noduri = mecanica.objCreate(date["dD"])
    locatie = mecanica.run(date["sD"], date["string"], date["sigmaD"], noduri)
    mecanica.interpretare(locatie, date["fD"])

if __name__ == "__main__":
    main()