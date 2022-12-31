"""
Diamond problem arises in cases like this where, say, a class D is inherited from class B and C which are both individually inherited from class A.
Now when using any method or variable there arises a confusion that in the multiple inheritence hieracrchy which method will be used specially in case of overwriting

Python's Hierarchial order solves this problem but some languages cannot solve it hence donot allow multiple inheritences like JAVA. C++ allows it but is still a major problem in it

To avoid the diamond problem it is advised to avoid using of multiple inheritences
"""
class A:
    def met(self):
        print("This is method from class A")

class B(A):
    def met(self):
        print("This is method from class B") #overwritten method 

class C(A):
    def met(self):
        print("This is method from class C")

class D(C, B):
    def met(self):
        print("This is method from class D")

if __name__ == '__main__':
    a = A()
    b = B()
    c = C()
    d = D()

    d.met()