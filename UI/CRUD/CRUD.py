from book.Domain import createBook, getId


def adaugaCarte(id, titlu, genCarte, pret, tipReducere, lista):
    '''
    Creeaza o carte si returneaza lista cu cartea adaugata in ea
    :param id: id-ul cartii
    :param titlu: titlul cartii
    :param genCarte: genul cartii
    :param pret: pretul cartii
    :param tipReducere: tipul de reducere al cartii
    :param lista: lista de carti existente
    :return: lista cu cartea adaugata in ea
    '''
    carte = createBook(id, titlu, genCarte, pret, tipReducere)
    return lista + [carte]


def checkValidIdtoAdd(id, lista):
    '''
    Verifica daca un id exista in lista de carti in vederea adaugarii unei noi carti cu acel id
    :param id: id-ul
    :param lista: lista de carti
    :return: False daca exista, True altfel
    '''
    for book in lista:
        if getId(book) == id:
            return False
    return True


def checkifBookExists(id, lista):
    '''
    Verifica daca exista o carte cu un id
    :param id: id-ul
    :param lista: lista de carti
    :return: True daca exista, True False
    '''
    for book in lista:
        if getId(book) == id:
            return True
    return False


def checkValidDiscountType(tipReducere):
    '''
    Verifica daca un tip de reducere este none/silver/gold
    :param tipReducere: tipul de reducere
    :return: True daca este none/silver/gold, altfel False
    '''
    if tipReducere != "none" and tipReducere != "silver" and tipReducere != "gold":
        return False
    return True