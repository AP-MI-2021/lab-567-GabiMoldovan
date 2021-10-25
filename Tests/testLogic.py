from UI.CRUD.CRUD import adaugaCarte
from functions.Logic import checkIfTitleExists, isInTypeList, getAllTypes, getMinPriceofType, isInPriceList, \
    getAllPrices, notCounted


def testAllLogicFunctions():
    lista = []
    lista = adaugaCarte("1", "Dumbrava minunata", "Basm", 15, "none", lista)
    lista = adaugaCarte("2", "Povestea lui Harap-Alb", "Basm", 1, "none", lista)
    lista = adaugaCarte("3", "Moara cu noroc", "Nuvela", 10, "silver", lista)

    assert checkIfTitleExists(lista, "Povestea lui Harap-Alb")
    assert isInTypeList(["Balada", "Roman", "Basm", "Comedie"], "Basm") == True
    assert getAllTypes(lista) == ["Basm", "Nuvela"]
    assert getMinPriceofType(lista, "Basm") == 1
    assert isInPriceList(["15", "34", "64", "24", "54"], "24") == True
    assert isInPriceList(["15", "34", "64", "24", "54"], "25") == False
    assert getAllPrices(lista) == [15, 1, 10]
    assert notCounted(lista, "Ion") == False

