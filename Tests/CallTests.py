from Tests.TestDomain import testCarte
from Tests.testCRUD import testCrud
from Tests.testLogic import testAllLogicFunctions


def runTests():
    testCarte()
    testCrud()
    testAllLogicFunctions()
