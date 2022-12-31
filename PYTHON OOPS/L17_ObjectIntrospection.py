"""
Object introspection refers to getting information about the Object 
"""
import inspect  # Helps to inspect any object


class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{self.fname}.{self.lname}@gmail.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return f"EMAIL IS NOT SET"
        else:
            return f"{self.fname}.{self.lname}@gmail.com"

    # To change the fname and lname if the email is changed we use a setter decorator
    # SYNTAX => @attribute.setter => attribute is the attribute which we want to change by input

    @email.setter
    def email(self, string):
        print("Setting now")
        names = string.split("@")[0]
        self.fname, self.lname = names.split(".")

    @email.deleter  # Deleter for attribute email
    def email(self):
        print("DELETING NOW")
        self.fname = None  # In oops we dont delete instead we put the value to None
        self.lname = None


if __name__ == '__main__':
    skillf = Employee("Skill", "f")
    print(type(skillf))  # Object Introspection => Finding type of skillf instance
    print(id(skillf))  # Object Introspection => Finding id of skillf instance
    print(dir(skillf))  # dir() returns all methods and  defined for skillf

    print(inspect.getmembers(skillf))
