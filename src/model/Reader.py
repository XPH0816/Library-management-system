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

        if self.idReader == None:
            temp = 0
        else:
            temp = int(hash(self.idReader))
        
        result = constants.prime * result + temp

        if self.nameReader == None:
            temp1 = 0
        else:
            temp1 = int(hash(self.nameReader))

        result = constants.prime * result + temp1

        if self.sex == None:
            temp2 = 0
        else:
            temp2 = int(hash(self.sex))

        result = constants.prime * result + temp2

        if self.level == None:
            temp3 = 0
        else:
            temp3 = int(hash(self.level))
        
        result = constants.prime * result + temp3
        
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

    def list_return_reader(self):
        return (self.idReader,self.nameReader,self.level,self.sex,self.password)

    def toString(self):
        return "Reader [idReader = " + self.idReader + ", nameReader = " + self.nameReader + ", type = " + self.level + ", sex = " + self.sex+ ", password = " + self.password + "]"
