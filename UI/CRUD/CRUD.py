from book.Domain import createBook, getId


def adaugaCarte(id, titlu, genCarte, pret, tipReducere, lista):
    carte = createBook(id, titlu, genCarte, pret, tipReducere)
    return lista + [carte]

def checkValidIdtoAdd(id, lista):
    for book in lista:
        if getId(book) == id:
            return False
    return True

def checkifBookExists(id, lista):
    for book in lista:
        if getId(book) == id:
            return True
    return False

def checkValidDiscountType(tipReducere):
    if tipReducere != "none" and tipReducere != "silver" and tipReducere != "gold":
        return False
    return True