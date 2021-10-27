from Tests.TestDomain import testCarte
from Tests.testCRUD import testAdaugaCarte
from Tests.testLogic import testAllLogicFunctions
from UI.CRUD.CRUD import checkValidIdtoAdd, checkifBookExists, checkValidDiscountType
from book.book import getId, getTitle, getBookType, getPrice, getDiscountType


def runTests(lista):

    assert getId(lista[0]) == "1"
    assert getTitle(lista[0]) == "Dumbrava minunata"
    assert getBookType(lista[0]) == "Basm"
    assert getPrice(lista[0]) == 15
    assert getDiscountType(lista[0]) == "none"

    assert getId(lista[1]) == "2"
    assert getTitle(lista[1]) == "Povestea lui Harap-Alb"
    assert getBookType(lista[1]) == "Basm"
    assert getPrice(lista[1]) == 1
    assert getDiscountType(lista[1]) == "none"

    assert checkValidIdtoAdd("1", lista) == False
    assert checkifBookExists("1", lista) == True
    assert checkValidDiscountType(getBookType(lista[0])) == False

    assert checkValidIdtoAdd("2", lista) == False
    assert checkifBookExists("2", lista) == True
    assert checkValidDiscountType(getBookType(lista[1])) == False

