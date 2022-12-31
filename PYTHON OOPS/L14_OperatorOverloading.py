"""
method which start and end from double underscore(__) are called Dunder Methods and are special as they are constructor methods

to get which method to edit in order to overload an operator search on google "Mapping operator to functions in python documentation"
"""


class Employee:
    no_of_leaves = 30

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def printdetails(self):
        details = f"REPR: Employee({self.name}, {self.salary}, {self.role})"

        return details

    def __add__(self, other):  # Dunder Addition
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary/other.salary

    def __repr__(self):  # generally __repr__ is used to overload it in order to print beautifully the details of instance
        return self.printdetails()

    def __str__(self):  # if __str__ is not overloaded then by default __repr__ will be used by print. but if __str__ is available then __repr__ will be ignored
        return f"STR: Employee({self.name}, {self.salary}, {self.role})"


if __name__ == '__main__':
    emp1 = Employee("harry", 345, "Programmer")
    # emp2 = Employee("rohan", 450, "cleaner")

    print(emp1)
