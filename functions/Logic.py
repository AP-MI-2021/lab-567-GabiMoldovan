from UI.CRUD.CRUD import checkValidDiscountType, checkifBookExists
from Domain.book import getId, getTitle, getBookType, getPrice, getDiscountType, createBook


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
        print("Tip reducere: " + getDiscountType(book))
        print()

def UIadaugaCarte(id, titlu, gen, pret, tipReducere):
    '''
    Creeaza o carte
    :return: cartea creata
    '''
    return createBook(id, titlu, gen, pret, tipReducere)


def deleteBookbyId(lista, id):
    '''
    Sterge o carte dupa id
    :param lista: lista de carti
    :return: lista cu cartea stearsa
    '''
    ListaNoua = []
    for book in lista:
        if getId(book) != id:
            ListaNoua = ListaNoua + [book]
    return ListaNoua


def changeBookData(lista, id, titlu, gen, pret, tipReducere):
    '''
    :param lista:
    :param id:
    :param titlu:
    :param gen:
    :param pret:
    :param tipReducere:
    :return:
    '''
    ListaNoua = []
    for book in lista:
        if getId(book) == id:
            newBook = UIadaugaCarte(id, titlu, gen, pret, tipReducere)
            ListaNoua.append(newBook)
        else:
            ListaNoua.append(book)
    return ListaNoua


def applyDiscounts(lista, discountType):
    '''
    Aplica reducerile de tip silver/gold
    :param lista: lista de carti
    :return: lista dupa aplicarea reducerilor
    '''
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


def modifyTypeByTitle(lista, title, newType):
    '''
    Modifica genul unei carti dupa un titlu dat
    :param lista: lista de carti
    :return: lista cu aplicarea modificarii genului asupra cartii cu titlul dat
    '''
    ListaNoua = []
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
            elif getPrice(book) < int(price):
                price = getPrice(book)
    return price


def getTitlesWithMinPriceOfType(gen, pretGen, lista):
    listaTitluriPretMinimPtGen = []
    for book in lista:
        if getBookType(book) == gen and getPrice(book) == pretGen:
            listaTitluriPretMinimPtGen.append(getTitle(book))
    return listaTitluriPretMinimPtGen

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


def countedTitle(titluriGen, titluCarte):
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


def getDistinctTitlesbyType(lista, gen):
    '''
    Determina numarul de titluri distincte din fiecare gen
    :param lista: lista de carti
    :return: None
    '''
    titluriGen = []
    numar = int(0)
    for book in lista:
        if getBookType(book) == gen and countedTitle(titluriGen, getTitle(book)) == False:
            numar = numar + int(1)
            titluriGen.append(getTitle(book))
    return titluriGen