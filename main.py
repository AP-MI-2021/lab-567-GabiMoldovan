from Tests.CallTests import runTests
from UI.CRUD.CRUD import adaugaCarte
from UI.UserInterface import runMenu

def main():

    '''

    lista = []
    lista = adaugaCarte("1", "Dumbrava minunata", "Basm", 15, "none", lista)
    lista = adaugaCarte("2", "Povestea lui Harap-Alb", "Basm", 1, "none", lista)
    lista = adaugaCarte("3", "Moara cu noroc", "Nuvela", 20, "silver", lista)
    lista = adaugaCarte("4", "Mara", "Nuvela", 20, "silver", lista)
    lista = adaugaCarte("5", "Ion", "Roman", 13, "none", lista)
    lista = adaugaCarte("6", "Ultima noapte de dragoste, intaia noapte de razboi", "Roman", 18, "gold", lista)
    lista = adaugaCarte("7", "Plumb", "Poezii", 8, "gold", lista)

    '''

    lista = [
        ("1", "Dumbrava minunata", "Basm", 15, "none"),
        ("2", "Povestea lui Harap-Alb", "Basm", 1, "none"),
        ("3", "Moara cu noroc", "Nuvela", 20, "silver"),
        ("4", "Mara", "Nuvela", 20, "silver"),
        ("5", "Ion", "Roman", 13, "none"),
        ("6", "Ultima noapte de dragoste, intaia noapte de razboi", "Roman", 18, "gold"),
        ("7", "Plumb", "Liric", 8, "gold")
    ]

    runTests()
    runMenu(lista)

main()