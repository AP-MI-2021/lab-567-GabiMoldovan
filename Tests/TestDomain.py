from book.Domain import createBook, getId, getTitle, getBookType, getPrice, getDiscountType


def testCarte():

    assert getTitle( ("1", "Dumbrava minunata", "Basm", 15, "none") ) == "Dumbrava minunata"
    assert getBookType( ("1", "Dumbrava minunata", "Basm", 15, "none") ) == "Basm"
    assert getPrice( ("1", "Dumbrava minunata", "Basm", 15, "none") ) == 15
    assert getDiscountType( ("1", "Dumbrava minunata", "Basm", 15, "none") ) == 'none'