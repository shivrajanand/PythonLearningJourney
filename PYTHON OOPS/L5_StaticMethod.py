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


if __name__ == '__main__':
    karan = Employee.from_str("Karan-10_00_00-Engineer")
    print(karan.printgood("Karan"))
    print(Employee.printgood("Rohan"))
