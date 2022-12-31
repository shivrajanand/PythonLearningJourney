"""
Inheritence - It is concept of inheriting all the properties of some other class. This can also be achieved by copying the code but it will then defy the DRY Rule

Single Inheritence - when one class inherit from one class
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
    # Cls is the class of the instance of object on which the function is runnning
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves

        # Advantage of this method is that both instance and class can access the method

    @classmethod
    # def from_str(cls, string):
    #     params = string.split("-")
    #     return cls(params[0], params[1], params[2])
    def from_str(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print(f"{string} is good")
        return "CodeCompelted"


class Player:
    no_of_games = 4

    def __init__(Self):
        self.name = name
        self.game = game

    def printdetails(self):
        details = f"Name is {self.name}. Game is {self.game}"
        return details


class cool_programmer(Employee, Player):
    # In multiple inheritences the child class with search for constructor in first parent class
    pass


if __name__ == '__main__':

    harry = Employee.from_str("Harry-255-Instructor")
    rohan = Employee.from_str("Rohan-455-Student")

    shubham = Player("Shubham", ["Cricket"])

    karan - cool_programmer("Karan", salary, role)

    # start from lecture multiple inherittences
