from abc import ABC, abstractclassmethod

class Shape(ABC): #Inheriting class Shape from class ABC gives Shape the power to force the child classes to define all the abstractclassmethod(s)
    @abstractclassmethod #This will force all the child classes to define a method print area otherwise error
    def printarea(self):
        return 0
    
    # @abstractclassmethod
    def func(self): #we cannot make objcts of astract base classes
        print("This is func")

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def printarea(self):
        return self.length*self.breadth

    # def func(self):
    #     print("This is a rectangle")

if __name__ == '__main__':
    rect1 = Rectangle(3, 4)
    # print(rect1.printarea())
    # rect1.func()

    # d = Shape()



    