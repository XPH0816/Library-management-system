from datetime import *
from dateutil.relativedelta import *

class Borrow:
    idReader = ""
    idBook = ""
    lendDate = datetime
    dueDate = datetime
    overtime = ""

    def getIdReader(self):
        return self.idReader

    def setIdReader(self, idReader):
        self.idReader = idReader

    def getIdBook(self):
        return self.idBook

    def setIdBook(self, idBook):
        self.idBook = idBook

    def getLendDate(self):
        return self.lendDate

    def setLendDate(self, lendDate):
        self.lendDate = lendDate

    def getDueDate(self):
        return self.dueDate

    def setDueDate(self, dueDate):
        self.dueDate = dueDate

    def getOvertime(self):
        return self.overtime

    def setOvertime(self, overtime):
        self.overtime = overtime
    
    def toString(self):
        return "Borrow [idReader = " + self.idReader + ", idBook = " + self.idBook + ", lendDate = " + self.lendDate + ", dueDate = " + self.dueDate + ", overtime = " + self.overtime + "]"

