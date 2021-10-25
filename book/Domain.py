def createBook(id, titlu, genCarte, pret, tipReducere):
    '''
    Subprogramul care creeaza entitatea "carte"
    :param id: id-ul cartii
    :param titlu: titlul cartii
    :param genCarte: genul cartii
    :param pret: pretul cartii
    :param tipReducere: tipul de reducere al cartii
    :return: cartea
    '''
    return {
        "id": id,
        "titlu": titlu,
        "genCarte": genCarte,
        "pret": pret,
        "tipReducere": tipReducere
    }


def getId(carte):
    '''
    Determina id-ul cartii
    :param carte: cartea
    :return: id-ul cartii
    '''
    return carte["id"]


def getTitle(carte):
    '''
    Determina titlul cartii
    :param carte: cartea
    :return: titlul cartii
    '''
    return carte["titlu"]


def getBookType(carte):
    '''
    Determina genul cartii
    :param carte: cartea
    :return: genul cartii
    '''
    return carte["genCarte"]


def getPrice(carte):
    '''
    Determina pretul cartii
    :param carte: cartea
    :return: pretul cartii
    '''
    return carte["pret"]


def getDiscountType(carte):
    '''
    Determina tipul de reducere al cartii
    :param carte: cartea
    :return: tipul de reducere al cartii
    '''
    return carte["tipReducere"]


def toString(carte):
    '''
    Afiseaza cartea cu parametrii convertiti la string
    :param carte: cartea
    :return: cartea cu parametrii convertiti la string
    '''
    return "Id: {}, Titlu: {}, Gen carte: {}, Pret: {}, Tip reducere: {}".format(
        getId(carte),
        getTitle(carte),
        getBookType(carte),
        getPrice(carte),
        getDiscountType(carte)
    )