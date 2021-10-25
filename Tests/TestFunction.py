from Tests.TestDomain import testCarte
from Tests.testCRUD import testAdaugaCarte
from Tests.testLogic import testAllLogicFunctions


def runTests():
    testCarte()
    testAdaugaCarte()
    testAllLogicFunctions()
