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

if __name__ == '__main__':
    # rohan = Employee()
    # rohan.name = "Rohan"
    # rohan.salary = 50,000
    # rohan.role = "CEO"

    shivraj = Employee("Shivraj", 1_000_000, "Agent-X")
    # print(rohan.printdetails())
    print(shivraj.printdetails())


