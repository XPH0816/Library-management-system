from collections import namedtuple


class Reader:
    idReader = ""
    nameReader = ""
    level = ""
    sex = ""
    password = ""

    def setAll(self, list):
        self.idReader = list[0]
        self.nameReader = list[1]
        self.level = list[2]
        self.sex = list[3]
        self.password = list[4]

    def getIdReader(self):
        return self.idReader
    
    def setIdReader(self, idReader):
        self.idReader = idReader

    def getNameReader(self):
        return self.nameReader

    def setNameReader(self, nameReader):
        self.nameReader = nameReader

    def getLevel(self):
        return self.level

    def setLevel(self, level):
        self.level = level

    def getSex(self):
        return self.sex

    def setSex(self, sex):
        self.sex = sex

    def getPassword(self):
        return self.password

    def setPassword(self, password):
        self.password = password

    def hashCode(self):

        #Create Constants Variable cause pyhton have constants variable
        Constants = namedtuple('Constants', ['prime'])
        constants = Constants(31)

        result = 1

        if self.idReader == None:
            temp = 0
        else:
            temp = int(hash(self.idReader))
        
        result = constants.prime * result + temp

        if self.nameReader == None:
            temp = 0
        else:
            temp = int(hash(self.nameReader))

        result = constants.prime * result + temp

        if self.sex == None:
            temp = 0
        else:
            temp = int(hash(self.sex))

        result = constants.prime * result + temp

        if self.level == None:
            temp = 0
        else:
            temp = int(hash(self.level))
        
        result = constants.prime * result + temp
        
        return result

    def equals(self, reference, current):
        if (reference == current):
            return True
        if (current == None):
            return False
        if (__class__ != Reader):
            return False
        other = Reader()
        if (self.idReader == None):
            if(other.idReader != None):
                return False
        elif (not(self.idReader == other.idReader)):
            return False
        if (self.nameReader == None):
            if(other.nameReader != None):
                return False
        elif (not(self.nameReader == other.nameReader)):
            return False
        if (self.sex == None):
            if(other.sex != None):
                return False
        elif (not(self.sex == other.sex )):
            return False
        if (self.level == None):
            if(other.level != None):
                return False
        elif (not(self.level == other.level)):
            return False
        return True

    def list_return(self):
        return (self.idReader,self.nameReader,self.level,self.sex,self.password)

    def toString(self):
        return "Reader [idReader = " + self.idReader + ", nameReader = " + self.nameReader + ", type = " + self.level + ", sex = " + self.sex+ ", password = " + self.password + "]"
