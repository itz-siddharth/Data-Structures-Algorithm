class Vehicle():
    def __init__(self,color,maxSpeed):
        self.color = color
        self.__maxSpeed = maxSpeed
        
    def getmaxSpeed(self):
        return self.__maxSpeed
    
    def setmaxSpeed(self,maxSpeed):
        self.__maxSpeed = maxSpeed
        
    def print(self):
        print("Color : ", self.color)
        print("MaxSpeed : ", self.__maxSpeed)
        
        
class Car(Vehicle):
    
    def __init__(self,color,maxSpeed,numGears,isConvertible):
        
        super().__init__(color,maxSpeed)
        self.numGears = numGears
        self.isConvertible = isConvertible
        
    def printCar(self):
        #super().print() can also be used
        self.print()
        #this can be used as the child class inheret the properties of the parent class
        print("NumGears : ", self.numGears)
        print("IsConvertible : ", self.isConvertible)
        
c = Car("red",15,3,False)
c.printCar()