from collections import namedtuple

class Librarian:
    nameUser = ""
    password = ""
    
    def getNumberUser(self):
        return str(nameUser)
    
    def setNameUser(self, nameUser):
        self.nameUser = str(nameUser)

    def getPassword(self):
        return str(password)

    def setPassword(self, password):
        self.password = str(password)

    def hashCode(self):
        
        #Create Constants Variable cause pyhton have constants variable
        Constants = namedtuple('Constants',['prime'])
        constants = Constants(31)

        if nameUser == None :
            temp = 0
        else :
            temp = nameUser.hashCode()

        result = 1
        result = constants.prime * result + temp
        return result

    #check the input are not Null
    #Return True when is Null
    def equals(self, reference, current): 
        if (current == reference):
            return True
        if (current == None):
            return False
        if (__class__ != Librarian):
            return False
        other = Librarian()
        if (self.nameUser == None):
            if(other.nameUser != None):
                return False
        elif (not(self.nameUser == other.nameUser)):
            return False
        return True

    def list_return(self):
        return (self.nameUser,self.password)

    def toString(self):
        return "Librarian [nameUser=" + self.nameUser + ", password=" + self.password + "]"

