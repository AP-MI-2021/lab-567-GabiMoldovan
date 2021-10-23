from functions.Logic import showBooks, UIadaugaCarte, deleteBookbyId, changeBookData


def printMenu():
    print("Optiunile sunt:")
    print("0. Afiseaza cartile din librarie")
    print("1. Adauga o carte in librarie")
    print("2. Sterge o carte din librarie")
    print("3. Modifica datele unei carti din librarie")
    print("4. Aplica o reducere de tip silver/gold")
    print("5. Modifica genul pentru un titlu dat")
    print("6. Afiseaza pretul minim pentru fiecare gen")
    print("7. Afiseaza vanzarile crescator dupa pret")
    print("8. Afisarea numarului de titluri distincte din fiecare gen")
    print("x. Termina programul")

def runMenu(lista):
    while True:
        printMenu()
        option = input("Scrie numarul aferent unei optiuni: ")
        if option == "0":
            print("Cartile din librarie sunt:")
            showBooks(lista)

        if option == "1":
            lista = lista + [UIadaugaCarte(lista)]
            print("Cartea a fost adaugata cu succes!")

        if option == "2":
            lista = deleteBookbyId(lista)
            print("Cartea a fost stearsa cu succes!")

        if option == "3":
            lista = changeBookData(lista)

        if option == "x":
            break
        print()