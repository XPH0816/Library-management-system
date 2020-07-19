from collections import namedtuple


class Reader:
    idReader = ""
    nameReader = ""
    level = ""
    sex = ""
    password = ""

    def getIdReader(self):
        return idReader
    
    def setIdReader(self, idReader):
        self.idReader = idReader

    def getNameReader(self):
        return nameReader

    def setNameReader(self, nameReader):
        self.nameReader = nameReader

    def getLevel(self):
        return level

    def setLevel(self, level):
        self.level = level

    def getSex(self):
        return sex

    def setSex(self, sex):
        self.sex = sex

    def getPassword(self):
        return password

    def setPassword(self, password):
        self.password = password

    def hashCode(self):

        #Create Constants Variable cause pyhton have constants variable
        Constants = namedtuple('Constants', ['prime'])
        constants = Constants(31)

        result = 1

        if idReader == null:
            temp = 0
        else:
            temp = idReader.hashCode()
        
        result = constants.prime * result + temp

        if nameReader == null:
            temp1 = 0
        else:
            temp1 = nameReader.hashCode()

        result = constants.prime * result + temp1

        if sex == null:
            temp2 = 0
        else:
            temp2 = sex.hashCode()

        result = constants.prime * result + temp2

        if level == null:
            temp3 = 0
        else:
            temp3 = level.hashCode()
        
        result = constants.prime * result + temp3
        
        return result

    def equals(self, Reader):
        if (self == Reader):
            return True
        if (Reader == null):
            return False
        if (self.__class__ != Reader.__class__):
            return False
        other = Reader()
        if (nameUser == null):
            if(other.nameUser != null):
                return False
        elif (not(nameUser.equals(other.nameUser))):
            return False
        return True

    def toString(self):
        return "Reader [nameUser=" + nameUser + ", password=" + password + "]"
