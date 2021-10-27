from UI.CRUD.CRUD import checkifBookExists, checkValidDiscountType
from book.Domain import createBook
from functions.Logic import showBooks, UIadaugaCarte, deleteBookbyId, changeBookData, applyDiscounts, modifyTypeByTitle, \
    printMinPriceforAllTypes, sortByPrice, printDistinctTitlesbyType


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
    print("4. Aplica o reducere de tip silver/gold")
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
            titlu = input("Dati titlu: ")
            gen = input("Dati genul: ")
            pret = input("Dati pretul: ")
            # rezolvare ca pretul sa fie un numar natural
            tipReducere = input("Dati tipul reducerii (none/silver/gold): ")
            while checkifBookExists(id, lista) == True:
                id = input("Dati un id valid: ")
            while checkValidDiscountType(tipReducere) == False:
                tipReducere = input("Dati un tip de reducere valid (none/silver/gold):")
            lista.append( (id, titlu, gen, pret, tipReducere) )
            print("Cartea a fost adaugata cu succes!")

        elif option == "2":
            lista = deleteBookbyId(lista)
            print("Cartea a fost stearsa cu succes!")

        elif option == "3":
            lista = changeBookData(lista)
            print("Datele cartii au fost schimbate cu succes!")

        elif option == "4":
            lista = applyDiscounts(lista)
            print("Reducerea a fost aplicata cu succes!")

        elif option == "5":
            lista = modifyTypeByTitle(lista)
            print("Modificarea genului cartii a fost aplicata cu succes!")

        elif option == "6":
            printMinPriceforAllTypes(lista)

        elif option == "7":
            lista = sortByPrice(lista)
            print("Ordonarea a avut loc cu succes!")

        elif option == "8":
            print("Numarul de titluri distincte din fiecare gen sunt:")
            printDistinctTitlesbyType(lista)

        elif option == "x":
            break

        else:
            print("Ati ales o optiune gresita!")
        print()