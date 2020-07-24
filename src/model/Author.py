from collections import namedtuple

class Author:
    name = ""
    workplace = ""

    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    def getWorkplace(self):
        return self.workplace

    def setWorkplace(self, workplace):
        self.workplace = workplace

    def hashCode(self):

        #Create Constants Variable cause pyhton have constants variable
        Constants = namedtuple('Constants', ['prime'])
        constants = Constants(31)

        result = 1

        if (self.name == None):
            temp = 0
        else :
            temp = int(hash(self.name))

        if (self.workplace == None):
            temp1 = 0
        else :
            temp1 = int(hash(self.workplace))

        result = constants.prime * result + temp
        result = constants.prime * result + temp1

    def equals(self, reference, current):
        if (reference == current):
            return True
        if (current == None):
            return False
        if (__class__ != Author):
            return False
        other = Author()
        if(self.name == None):
            if(other.name != None):
                return False
        elif (not(self.equals(self.name,other.name))):
            return False
        if(self.workplace == None):
            if(other.workplace != None):
                return False
        elif(not(self.equals(self.workplace,other.workplace))):
            return False
        return True

    def toString(self):
        return "Author [name = " + self.name + ", workplace = " + self.workplace +  "]"
