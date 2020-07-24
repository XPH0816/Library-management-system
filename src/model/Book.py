from collections import namedtuple

class Book:
    idBook = ""
    nameBook = ""
    price = 0
    type_ = ""
    author = ""
    publisher = ""

    def getIdBook(self):
        return self.idBook

    def setIdBook(self, idBook):
        self.idBook = idBook

    def getNameBook(self):
        return self.nameBook

    def setNameBook(self, nameBook):
        self.nameBook = nameBook

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price
    
    def getType(self):
        return self.type_

    def setType(self, Type):
        self.type_ = Type

    def getAuthor(self):
        return self.author

    def setAuthor(self, author):
        self.author = author

    def getPublisher(self):
        return self.publisher

    def setPublisher(self, publisher):
        self.publisher = publisher

    def hashCode(self):

        #Create Constants Variable cause pyhton have constants variable
        Constants = namedtuple('Constants', ['prime'])
        constants = Constants(31)

        result = 1

        if (self.author == None):
            temp = 0
        else :
            temp = int(hash(self.author))
        
        result = constants.prime * result + temp

        if (self.idBook == None):
            temp = 0
        else :
            temp = int(hash(self.idBook))

        result = constants.prime * result + temp

        if (self.nameBook == None):
            temp = 0
        else:
            temp = int(hash(self.nameBook))

        result = constants.prime * result + temp

        if (self.price == None):
            temp = 0
        else:
            temp = self.price

        result = constants.prime * result + temp

        if (self.publisher == None):
            temp = 0
        else:
            temp = int(hash(self.publisher))

        result = constants.prime * result + temp

        if (self.type_ == None):
            temp = 0
        else:
            temp = int(hash(self.type_))

        result = constants.prime * result + temp

        return result

    def equals(self, reference, current):
        if (reference == current):
            return True
        if (current == None):
            return False
        if (__class__ != Book):
            return False
        other = Book()
        if(self.author == None):
            if(other.author != None):
                return False
        elif(not(self.equals(self.author, other.author))):
            return False
        if(self.nameBook == None):
            if(other.nameBook != None):
                return False
        elif(not(self.equals(self.nameBook, other.nameBook))):
            return False
        if(self.idBook == None):
            if(other.idBook != None):
                return False
        elif(not(self.equals(self.idBook, other.idBook))):
            return False
        if (self.price != other.price):
            return False
        if (self.publisher == None):
            if(other.publisher != None):
                return False
        elif(not(self.equals(self.publisher, other.publisher))):
            return False
        if(self.type_ == None):
            if(other.type_ != None):
                return False
        elif(not(self.equals(self.type_, other.type_))):
            return False
        return True

    def list_return(self):
        return (self.idBook,self.nameBook,self.price,self.type_,self.author,self.publisher)

    def toString(self):
        return "Book [idBook = " + self.idBook + ", nameBook = " + self.nameBook + ", price = " + self.price + ", type = " + self.type_ + ", author = "+ self.author + ", publisher = " + self.publisher + "]"
