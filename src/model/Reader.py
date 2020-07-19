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

        if idReader == None:
            temp = 0
        else:
            temp = idReader.hashCode()
        
        result = constants.prime * result + temp

        if nameReader == None:
            temp1 = 0
        else:
            temp1 = nameReader.hashCode()

        result = constants.prime * result + temp1

        if sex == None:
            temp2 = 0
        else:
            temp2 = sex.hashCode()

        result = constants.prime * result + temp2

        if level == None:
            temp3 = 0
        else:
            temp3 = level.hashCode()
        
        result = constants.prime * result + temp3
        
        return result

    def equals(self, Reader):
        if (self == Reader):
            return True
        if (Reader == None):
            return False
        if (self.__class__ != Reader.__class__):
            return False
        other = Reader()
        if (idReader == None):
            if(other.idReader != None):
                return False
        elif (not(idReader.equals(other.idReader))):
            return False
        if (nameReader == None):
            if(other.nameReader != None):
                return False
        elif (not(nameReader.equals(other.nameReader))):
            return False
        if (sex == None):
            if(other.sex != None):
                return False
        elif (not(sex.equals(other.sex))):
            return False
        if (level == None):
            if(other.level != None):
                return False
        elif (not(level.equals(other.level))):
            return False
        return True

    def toString(self):
        return "Reader [idReader=" + idReader + ", nameReader=" + nameReader + ", type=" + level + ", sex=" + sex+ ", password=" + password + "]"
