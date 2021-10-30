from UI.CRUD.CRUD import checkifBookExists, checkValidDiscountType
from functions.Logic import showBooks, UIadaugaCarte, deleteBookbyId, changeBookData, applyDiscounts, modifyTypeByTitle, \
    sortByPrice, getAllTypes, getMinPriceofType, getTitlesWithMinPriceOfType, checkIfTitleExists, \
    getDistinctTitlesbyType


def printMenu():
    '''
    Afiseaza meniul de optiuni
    :return: None
    '''
    print("Optiunile sunt:")
    print("0. Afiseaza cartile din librarie")
    print("1. Adauga o carte in librarie")
    print("2. Sterge o carte din librarie")
    print("3. Modifica datele unei carti din librarie")
    print("4. Aplica o reducere de tip silver/gold sau pe ambele")
    print("5. Modifica genul pentru un titlu dat")
    print("6. Afiseaza pretul minim pentru fiecare gen")
    print("7. Ordoneaza vanzarile crescator dupa pret")
    print("8. Afisarea numarului de titluri distincte din fiecare gen")
    print("9. Undo")
    print("x. Termina programul")


def runMenu(lista):
    '''
    Functia care ruleaza meniul
    :param lista: lista de carti
    :return: None
    '''
    while True:
        printMenu()
        option = input("Scrie numarul aferent unei optiuni: ")

        if option == "0":

            print("Cartile din librarie sunt:")
            showBooks(lista)

        elif option == "1":
            id = input("Dati id: ")
            while checkifBookExists(id, lista) == True:
                id = input("Exista deja o carte cu acest ID, introduceti un nou id: ")
            titlu = input("Dati titlu: ")
            gen = input("Dati genul: ")
            while True:
                try:
                    pret = int(input("Dati pretul: "))
                    break
                except ValueError:
                    print("Nu ati dat un numar natural pentru pret!")
            tipReducere = input("Dati tipul reducerii (none/silver/gold): ")
            while checkValidDiscountType(tipReducere) == False:
                tipReducere = input("Dati un tip de reducere valid (none/silver/gold):")
            lista = lista + [UIadaugaCarte(id, titlu, gen, pret, tipReducere)]
            print("Cartea a fost adaugata cu succes!")

        elif option == "2":
            id = input("Dati id-ul cartii care doriti sa fie stearsa: ")
            while checkifBookExists(id, lista) == False:
                id = input("Dati un id valid: ")
            lista = deleteBookbyId(lista, id)
            print("Cartea a fost stearsa cu succes!")

        elif option == "3":
            id = input("Dati id: ")
            while checkifBookExists(id, lista) == False:
                id = input("Cartea cu id-ul dat nu exista, dati un id valid: ")
            titlu = input("Dati titlu: ")
            gen = input("Dati genul: ")
            while True:
                try:
                    pret = int(input("Dati pretul: "))
                    break
                except ValueError:
                    print("Nu ati dat un numar natural pentru pret!")
            tipReducere = input("Dati tipul reducerii (none/silver/gold): ")
            while checkValidDiscountType(tipReducere) == False:
                tipReducere = input("Dati un tip de reducere valid (none/silver/gold):")
            lista = changeBookData(lista, id, titlu, gen, pret, tipReducere)
            print("Datele cartii au fost schimbate cu succes!")

        elif option == "4":
            discountType = input("Dati tipul de reducere(silver/gold/ambele): ")
            while discountType != "ambele" and discountType != "silver" and discountType != "gold":
                discountType = input("Dati un tip valid de reducere(silver/gold/ambele): ")
            lista = applyDiscounts(lista, discountType)
            print("Reducerea a fost aplicata cu succes!")

        elif option == "5":
            title = input("Dati titlul: ")
            while checkIfTitleExists(lista, title) == False:
                title = input("Dati un titlu care se afla in librarie: ")
            newType = input("Dati genul: ")
            lista = modifyTypeByTitle(lista, title, newType)
            print("Modificarea genului cartii a fost aplicata cu succes!")

        elif option == "6":
            listaGenuri = []
            listaGenuri = getAllTypes(lista)
            for gen in listaGenuri:
                pretGen = getMinPriceofType(lista, gen)
                titluriPreturiMinimePtGen = []
                titluriPreturiMinimePtGen = getTitlesWithMinPriceOfType(gen, pretGen, lista)
                print("Cartea/Cartile cu pretul minim ( de " + str(pretGen) + " ) al genului " + gen + " sunt:", end = " ")
                for titlu in titluriPreturiMinimePtGen:
                    if titlu is not titluriPreturiMinimePtGen[int(len(titluriPreturiMinimePtGen))-int(1)]:
                        print("\"" + titlu + "\"", end=", ")
                    else:
                        print("\"" + titlu + "\"", end=".")
                print()



        elif option == "7":
            lista = sortByPrice(lista)
            print("Ordonarea a avut loc cu succes!")

        elif option == "8":
            listaGenuri = []
            listaGenuri = getAllTypes(lista)
            print("Numarul de titluri distincte din fiecare gen sunt:")
            for gen in listaGenuri:
                listaTitluriDistincte = []
                listaTitluriDistincte = getDistinctTitlesbyType(lista, gen)
                print("Numarul de titluri distincte care au genul " + gen + " este: " + str(len(listaTitluriDistincte)))

        elif option == "x":
            break

        else:
            print("Ati ales o optiune gresita!")
        print()