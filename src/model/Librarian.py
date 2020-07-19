from collections import namedtuple

class Librarian:
    nameUser = ""
    password = ""
    
    def getNumberUser(self):
        return nameUser
    
    def setNameUser(self, nameUser):
        self.nameUser = nameUser

    def getPassword(self):
        return password

    def setPassword(self, password):
        self.password = password

    def hashCode(self):
        
        #Create Constants Variable cause pyhton have constants variable
        Constants = namedtuple('Constants',['prime'])
        constants = Constants(31)

        if nameUser == null :
            temp = 0
        else :
            temp = nameUser.hashCode()

        result = 1
        result = constants.prime * result + temp
        return result

    def equals(self, Librarian):
        if (self == Librarian):
            return True
        if (Librarian == null):
            return False
        if (self.__class__ != Librarian.__class__):
            return False
        other = Librarian()
        if (nameUser == null):
            if(other.nameUser != null):
                return False
        elif (not(nameUser.equals(other.nameUser))):
            return False
        return True

    def toString(self):
        return "Librarian [nameUser=" + nameUser + ", password=" + password + "]"

