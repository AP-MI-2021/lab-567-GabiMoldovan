def createBook(id, titlu, genCarte, pret, tipReducere):
    return {
        "id": id,
        "titlu": titlu,
        "genCarte": genCarte,
        "pret": pret,
        "tipReducere": tipReducere
    }

def getId(carte):
    return carte["id"]

def getTitle(carte):
    return carte["titlu"]

def getBookType(carte):
    return carte["genCarte"]

def getPrice(carte):
    return carte["pret"]

def getDiscountType(carte):
    return carte["tipReducere"]

def toString(carte):
    return "Id: {}, Titlu: {}, Gen carte: {}, Pret: {}, Tip reducere: {}".format(
        getId(carte),
        getTitle(carte),
        getBookType(carte),
        getPrice(carte),
        getDiscoundType(carte)
    )