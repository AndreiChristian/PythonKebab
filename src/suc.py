from produs import Produs  # Din produs.py importam
# obiectul Produs


class Cola(Produs):

    def __init__(self, pret=8):
        super().__init__("Coca Cola", pret)


class Fanta(Produs):

    def __init__(self, pret=7):
        super().__init__("Fanta", pret)


class Sprite(Produs):

    def __init__(self, pret=7.50):
        super().__init__("Sprite", pret)


def alege_suc(lista_produse):

    print("Doriti sa comandati un suc.")
    print("1.Cola\n2.Fanta\n3.Sprite")

    comanda_suc = input("Ce suc doriti?")
    if comanda_suc == "1":
        lista_produse.append(Cola())
    elif comanda_suc == "2":
        lista_produse.append(Fanta())
    elif comanda_suc == "3":
        lista_produse.append(Sprite())
