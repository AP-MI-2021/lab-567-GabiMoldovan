from CRUD.CRUD import adaugaCarte, checkValidIdtoAdd, checkifBookExists, checkValidDiscountType
from Domain.book import getId, getTitle, getBookType, getPrice, getDiscountType, createBook


def testCrud():
    lista = []
    book = createBook("1", "Dumbrava minunata", "Basm", 15, "none")
    lista = lista + [book]

    assert adaugaCarte( "2", "Povestea lui Harap-Alb", "Basm", 1, "none", lista ) == [ ("1", "Dumbrava minunata", "Basm", 15, "none"),  ("2", "Povestea lui Harap-Alb", "Basm", 1, "none") ]
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