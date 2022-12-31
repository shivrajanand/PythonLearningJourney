"""
Public-  Accessible by everyone
    Public variables can be created by naming variables generally as we do
Protected - Accessible to only specific people
    Protected variables can be created by starting the name of variable with an underscore(_)
    These variables can be accessed by the base class and other classes which are derived by the base class.
Private - Acccessible to only one entity
    Private variables can be created by starting the name of variable with double underscore(__)
    To protect this python uses a method called name mangling that is making the variable name complex
    to access this private variable we have to use mangled variable name that is instance._ClassName__privateVariable


"""
class Employee:
    no_of_leaves = 7
    _protected = 8
    __private = 100

if __name__ == '__main__':
    rohan = Employee()

    print(rohan._Employee__private)