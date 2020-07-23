from collections import namedtuple

class Publisher:

    name = ""
    address = ""

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address

    def hashCode(self):
        #Create Constants Variable cause pyhton have constants variable
        Constants = namedtuple('Constants', ['prime'])
        constants = Constants(31)

        result = 1

        if (self.address == None):
            temp = 0
        else :
            temp = self.hashCode() 

        if (self.name == None):
            temp = 0
        else :
            temp = self.hashCode()

        result = prime * result + temp
        
        return result

    def equals(self, reference, current):
        if (reference == current):
            return True
        if (current == None):
            return False
        if (__class__ != Publisher):
            return False
        other = Publisher()
        if (self.address == None):
            if(other.address != None):
                return False
        elif (not(self.equals(self.address, other.address))):
            return False
        if (self.name == None):
            if(other.name != None):
                return False
        elif (not(self.equals(self.address, other.address))):
            return False
        return True

    def toString(self):
        return "Publisher [name =" + self.name + ", address=" + self.address + "]"
