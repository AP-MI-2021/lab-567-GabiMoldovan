from UI.CRUD.CRUD import checkValidIdtoAdd, checkifBookExists, checkValidDiscountType
from book.Domain import getId, getTitle, getBookType, getPrice, getDiscountType, createBook


def testAdaugaCarte():
    lista = []
    book = createBook("1", "Dumbrava minunata", "Basm", 15, "none")
    lista = lista + [book]

    assert len(lista) == 1
    assert getId(book) == "1"
    assert getTitle(book) == "Dumbrava minunata"
    assert getBookType(book) == "Basm"
    assert getPrice(book) == 15
    assert getDiscountType(book) == "none"
    assert checkValidIdtoAdd("1", lista) == False
    assert checkValidIdtoAdd("2", lista) == True
    assert checkifBookExists("1", lista) == True
    assert checkifBookExists("2", lista) == False
    assert checkValidDiscountType("none") == True
    assert checkValidDiscountType("test") == False
    assert checkValidDiscountType("gold") == True