from UI.CRUD.CRUD import checkValidDiscountType, checkifBookExists
from book.Domain import getId, getTitle, getBookType, getPrice, getDiscountType, createBook


def showBooks(lista):
    for book in lista:
        print("Id: " + getId(book))
        print("Titlu: " + getTitle(book))
        print("Gen: " + getBookType(book))
        print("Pret: " + str(getPrice(book)))
        print("Tip reducere: " + getDiscountType(book))
        print()

def UIadaugaCarte(lista):
    id = input("Dati id: ")
    titlu = input("Dati titlu: ")
    gen = input("Dati genul: ")
    pret = input("Dati pretul: ")
    tipReducere = input("Dati tipul reducerii (none/silver/gold): ")
    while checkifBookExists(id, lista) == True:
        id = input("Dati un id valid: ")
    while checkValidDiscountType(tipReducere) == False:
        tipReducere = input("Dati un tip de reducere valid (none/silver/gold):")
    return createBook(id, titlu, gen, pret, tipReducere)

def deleteBookbyId(lista):
    id = input("Dati id-ul cartii care doriti sa fie stearsa: ")
    while checkifBookExists(id, lista) == False:
        id = input("Dati un id valid: ")
    ListaNoua = []
    for book in lista:
        if getId(book) != id:
            ListaNoua = ListaNoua + [book]
    return ListaNoua

def changeBookData(lista):
    id = input("Dati id-ul cartii pentru care doriti sa modificati datele: ")
    while checkifBookExists(id, lista) == False:
        id = input("Dati un id valid: ")
    ListaNoua = []
    for book in lista:
        if getId(book) == id:
            newBook = UIadaugaCarte(ListaNoua)
            ListaNoua.append(newBook)
        else:
            ListaNoua.append(book)
    return ListaNoua
