class A:
    classvar1 = "I am a variable in class A"

    def __init__(self):
        self.var1 = "I am inside class A\'s Constructor"
        self.classvar1 = "instance variable in class A"
        self.special = "special"


class B(A):
    classvar2 = "I am in class B"

    def __init__(self):
        super().__init__() #This statement calls parent class constructor. Used to access super class variables
        self.var1 = "I am inside class B\'s Constructor"
        self.classvar1 = "instance variable in class B"


if __name__ == '__main__':

    a = A()
    b = B()

    print(b.special)
