class Nod:    
    def __init__(self, name):
        self.name = name
        self.trimiteri = {}
    def directie(self, cod, destinatie):
        self.trimiteri[cod] = destinatie