from UI.CRUD.CRUD import checkValidDiscountType, checkifBookExists
from book.Domain import getId, getTitle, getBookType, getPrice, getDiscountType, createBook


def showBooks(lista):
    '''
    Afiseaza toate cartile din lista
    :param lista: lista de carti
    :return: None
    '''
    for book in lista:
        print("Id: " + getId(book))
        print("Titlu: " + getTitle(book))
        print("Gen: " + getBookType(book))
        print("Pret: " + str(getPrice(book)))
        print("Tip reducere: " + str(getDiscountType(book)))
        print()


def UIadaugaCarte(lista):
    '''
    Creeaza o carte
    :param lista: lista de carti existente
    :return: cartea creata
    '''
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
    carte = {'id': id, 'titlu': titlu, 'genCarte': gen, 'pret': pret, 'tipReducere': tipReducere}
    return carte


def deleteBookbyId(lista):
    '''
    Sterge o carte dupa id
    :param lista: lista de carti
    :return: lista cu cartea stearsa
    '''
    id = input("Dati id-ul cartii care doriti sa fie stearsa: ")
    while checkifBookExists(id, lista) == False:
        id = input("Dati un id valid: ")
    ListaNoua = []
    for book in lista:
        if getId(book) != id:
            ListaNoua = ListaNoua + [book]
    return ListaNoua


def changeBookData(lista):
    '''
    Schimba datele unei carti dupa id
    :param lista: lista de carti
    :return: lista cu datele cartii schimbate
    '''
    id = input("Dati id-ul cartii pentru care doriti sa modificati datele: ")
    while checkifBookExists(id, lista) == False:
        id = input("Dati un id valid: ")
    ListaNoua = []
    for book in lista:
        if getId(book) == id:
            idNou = input("Dati id: ")
            titluNou = input("Dati titlu: ")
            genNou = input("Dati genul: ")
            pretNou = input("Dati pretul: ")
            # rezolvare ca pretul sa fie un numar natural
            tipReducereNou = input("Dati tipul reducerii (none/silver/gold): ")
            while checkValidDiscountType(tipReducereNou) == False:
                tipReducereNou = input("Dati un tip de reducere valid (none/silver/gold):")
            ListaNoua.append((idNou, titluNou, genNou, pretNou, tipReducereNou))
        else:
            ListaNoua.append(book)
    return ListaNoua


def applyDiscounts(lista):
    '''
    Aplica reducerile de tip silver/gold
    :param lista: lista de carti
    :return: lista dupa aplicarea reducerilor
    '''
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
    '''
    Verifica daca title se afla in lista
    :param lista: lista de titluri
    :param title: titlul
    :return: True daca lista contine title, altfel False
    '''
    for book in lista:
        if getTitle(book) == title:
            return True
    return False


def modifyTypeByTitle(lista):
    '''
    Modifica genul unei carti dupa un titlu dat
    :param lista: lista de carti
    :return: lista cu aplicarea modificarii genului asupra cartii cu titlul dat
    '''
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
    '''
    Verifica daca un gen apare in lista de genuri
    :param ListaGenuri: lista de genuri
    :param gen: genul pentru care se verifica daca apare in lista de genuri
    :return: True daca apare, altfel False
    '''
    for genulCartii in ListaGenuri:
        if genulCartii == gen:
            return True
    return False


def getAllTypes(lista):
    '''
    Construieste o lista cu toate genurile de carti din librarie
    :param lista: lista de carti din librarie
    :return: o lista cu toate genurile de carti din librarie
    '''
    ListaGenuri = []
    for book in lista:
        if isInTypeList(ListaGenuri, getBookType(book)) == False:
            ListaGenuri.append(getBookType(book))
    return ListaGenuri


def getMinPriceofType(lista, gen):
    '''
    Determina cel mai mic pret al cartii care are un anumit gen
    :param lista: lista de carti
    :param gen: genul pentru care se determina pretul
    :return: cel mai mic pret al cartii cu un anumit gen
    '''
    price = None
    for book in lista:
        if getBookType(book) == gen:
            if price == None:
                price = getPrice(book)
            elif getPrice(book) < price:
                price = getPrice(book)
    return price


def printMinPricebyType(lista, gen):
    '''
    Determina daca cartile dintr-un gen au pretul minim, si afiseaza cartile din acel gen
    :param lista: lista de carti
    :param gen: genul pentru care se determina cartile cu pretul minim
    :return: None
    '''
    price = getMinPriceofType(lista, gen)
    for book in lista:
        if getBookType(book) == gen and getPrice(book) == price:
            print("\"" + getTitle(book) + "\"", end = ", ")
    print("cu pretul " + str(price))


def printMinPriceforAllTypes(lista):
    '''
    Afiseaza cartea/cartile cu pretul minim pentru fiecare gen
    :param lista: lista de carti
    :return: None
    '''
    listaGenuri = []
    listaGenuri = getAllTypes(lista)
    for genulCartii in listaGenuri:
        print("Cartea/Cartile cu pretul minim care au genul " + genulCartii + " este/sunt:", end = " ")
        printMinPricebyType(lista, genulCartii)


def isInPriceList(lista, pret):
    '''
    Verifica daca un pret apare in lista de preturi
    :param lista: lista de preturi
    :param pret: pretul
    :return: True daca pret apare in lista, False altfel
    '''
    for price in lista:
        if price == pret:
            return True
    return False


def getAllPrices(lista):
    '''
    Determina o lista cu toate preturile distincte ale cartilor
    :param lista: lista de carti
    :return: o lista cu toate preturile distincte ale cartilor
    '''
    prices = []
    for book in lista:
        if isInPriceList(prices, getPrice(book)) == False:
            prices.append(getPrice(book))
    return prices


def sortByPrice(lista):
    '''
    Sorteaza lista de carti dupa pret in ordine crescatoare
    :param lista: lista pe care o sorteaza
    :return: lista sortata
    '''
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
    '''
    Verifica daca titluCarte se afla in lista titluriGen
    :param titluriGen: o lista in care apare fiecare titlu al unui gen
    :param titluCarte: un titlu de carte
    :return: True daca titluCarte se afla in lista titluriGen, False altfel
    '''
    for title in titluriGen:
        if title == titluCarte:
            return True
    return False


def printDistinctTitlesbyType(lista):
    '''
    Determina numarul de titluri distincte din fiecare gen
    :param lista: lista de carti
    :return: None
    '''
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