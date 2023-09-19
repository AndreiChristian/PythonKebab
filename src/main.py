import produs
from suc import alege_suc

program_activ = True  # Definim o variabila "program_activ" care porneste ca fiind True
lista_produse = []


while program_activ:  # Cat timp program_activ este true

    print("Bine ati venit la Python Kebab!")  # Printam un mesaj de bun venit
    print("1.Kebab\n2.Suc\n3.Cartofi\n4.Meniu\n5.Arata cosul\n6.Pretul total")

    # Intrebam utilizatorul ce doreste sa
    comanda = input("Ce doriti sa comandati? ")
    # comande si stocam comanda utilizatorului intr-o variabila
    if comanda == 'q':  # Daca comanda este 'q' ne luam la revedere si oprim programul,
        # deoarece program_activ devine False
        print("La revedere")
        program_activ = False

    elif comanda == "1":
        print("Optiunea selectata este nr 1")

    elif comanda == "2":
        alege_suc(lista_produse)

    elif comanda == "3":
        pass

    elif comanda == "4":
        pass

    elif comanda == "5":

        for produs in lista_produse:  # Pentru fiecare produs din lista de produse,
            # produsul se va prezenta, folosind metoda de prezentare din produs.py
            produs.prezentare()

    elif comanda == "6":
        suma = 0
        for produs in lista_produse:
            suma += produs.pret

        print(f"Pretul total este {suma}")

    else:

        # Altfel, printam comanda utilizatorului
        print(f"Optiunea selectata este:{comanda}")

    # si cerem urmatoarea comanda
