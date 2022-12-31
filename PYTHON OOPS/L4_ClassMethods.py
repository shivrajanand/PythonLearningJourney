"""
NOTES 
self is the instance on which value and methods are applicable.

when operated on some object, eg, object.value or method(object) >>>> self is replaced by object instance

Constructor is a method used to initialize all the class variables. A sepcial method used is __init__(self):
"""

class Employee:
    no_of_leaves = 30

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary    
        self.role = role     

    def printdetails(self):
        details = f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"
        return details

    @classmethod
    def change_leaves(cls, new_leaves): #Cls is the class of the instance of object on which the function is runnning
        cls.no_of_leaves = new_leaves

        # Advantage of this method is that both instance and class can access the method

    @classmethod
    # def from_str(cls, string):
    #     params = string.split("-")
    #     return cls(params[0], params[1], params[2])

    def from_str(cls, string):
        return cls(*string.split("-"))
         


        return details

if __name__ == '__main__':
    # rohan = Employee()
    # rohan.name = "Rohan"
    # rohan.salary = 50,000
    # rohan.role = "CEO"

    # shivraj = Employee("Shivraj", 1_000_000, "Agent-X")
    # print(rohan.printdetails())
    karan = Employee.from_str("Karan-480-student")
    print(karan.printdetails())
    # print(f"SALARY => {karan.salary}")


