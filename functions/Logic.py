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

def applyDiscounts(lista):
    discountType = input("Dati tipul de reducere(silver/gold/ambele): ")
    while discountType != "silver" and discountType != "gold" and discountType != "ambele":
        discountType = input("Dati un tip valid de reducere(silver/gold/ambele): ")
    ListaNoua = []
    for book in lista:
        if getDiscountType(book) == "silver" and ( discountType == "silver" or discountType == "ambele" ):
            reducere = float(getPrice(book) / 20)
            reducere = float(getPrice(book) - reducere)
            newBook = createBook(getId(book), getTitle(book), getBookType(book), reducere, "silver")
            ListaNoua.append(newBook)
        elif getDiscountType(book) == "gold" and ( discountType == "gold" or discountType == "ambele" ):
            reducere = float(getPrice(book) / 10)
            reducere = float(getPrice(book) - reducere)
            newBook = createBook(getId(book), getTitle(book), getBookType(book), reducere, "gold")
            ListaNoua.append(newBook)
        else:
            ListaNoua.append(book)
    return ListaNoua

def checkIfTitleExists(lista, title):
    for book in lista:
        if getTitle(book) == title:
            return True
    return False

def modifyTypeByTitle(lista):
    ListaNoua = []
    title = input("Dati titlul: ")
    while checkIfTitleExists(lista, title) == False:
        title = input("Dati un titlu care se afla in librarie: ")
    newType = input("Dati genul: ")
    for book in lista:
        if getTitle(book) == title:
            newBook = createBook(getId(book), getTitle(book), newType, getPrice(book), getDiscountType(book))
            ListaNoua.append(newBook)
        else:
            ListaNoua.append(book)
    return ListaNoua

def isInTypeList(ListaGenuri, gen):
    for genulCartii in ListaGenuri:
        if genulCartii == gen:
            return True
    return False

def getAllTypes(lista):
    ListaGenuri = []
    for book in lista:
        if isInTypeList(ListaGenuri, getBookType(book)) == False:
            ListaGenuri.append(getBookType(book))
    return ListaGenuri

def getMinPriceofType(lista, gen):
    price = None
    for book in lista:
        if getBookType(book) == gen:
            if price == None:
                price = getPrice(book)
            elif getPrice(book) < price:
                price = getPrice(book)
    return price

def printMinPricebyType(lista, gen):
    price = getMinPriceofType(lista, gen)
    for book in lista:
        if getBookType(book) == gen and getPrice(book) == price:
            print("\"" + getTitle(book) + "\"", end = ", ")
    print("cu pretul " + str(price))


def printMinPriceforAllTypes(lista):
    listaGenuri = []
    listaGenuri = getAllTypes(lista)
    for genulCartii in listaGenuri:
        print("Cartea/Cartile cu pretul minim care au genul " + genulCartii + " este/sunt:", end = " ")
        printMinPricebyType(lista, genulCartii)

def isInPriceList(lista, pret):
    for price in lista:
        if price == pret:
            return True
    return False

def getAllPrices(lista):
    prices = []
    for book in lista:
        if isInPriceList(prices, getPrice(book)) == False:
            prices.append(getPrice(book))
    return prices

def sortByPrice(lista):
    priceList = []
    priceList = getAllPrices(lista)
    priceList.sort()
    ListaNoua = []
    for pret in priceList:
        for book in lista:
            if getPrice(book) == pret:
                ListaNoua.append(book)
    return ListaNoua

def notCounted(titluriGen, titluCarte):
    for title in titluriGen:
        if title == titluCarte:
            return True
    return False


def printDistinctTitlesbyType(lista):
    listaGenuri = []
    listaGenuri = getAllTypes(lista)
    for gen in listaGenuri:
        titluriGen = []
        numar = int(0)
        for book in lista:
            if getBookType(book) == gen and notCounted(titluriGen, getTitle(book)) == False:
                numar = numar + int(1)
                titluriGen.append(getTitle(book))
        print("Numarul de titluri distincte din genul " + gen + " este: " + str(numar))