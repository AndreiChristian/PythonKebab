class Produs:

    def __init__(self, denumire, pret):
        self.denumire = denumire
        self.pret = pret

    def prezentare(self):
        print(f"Denumire: {self.denumire}, Pret = {self.pret}")
