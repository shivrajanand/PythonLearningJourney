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
    

    @email.deleter  #Deleter for attribute email
    def email(self):
        print("DELETING NOW")
        self.fname = None #In oops we dont delete instead we put the value to None
        self.lname = None


if __name__ == '__main__':
    monitor = Employee("Vishal", "Kumar")
    bermuda = Employee("Syed", "Hamid")

    # print("This is by using email as a constructor attribute")
    # print(monitor.email)
    # monitor.fname = "abhishek"
    # print(monitor.email)

    # Even after changing the fname of monitor instance the email was not changed in runtime because the email was already initialized in the constructor and was not changed in runtime when fname was changed

    # print("This is by using email as a class method")
    # print(monitor.email())
    # monitor.fname = "abhishek"
    # print(monitor.email())

    # In above code function was used which at some point donot provide encapsulation. To solve this we use setters

    # print("This is by using email as a class method of property decorator")
    # print(monitor.email)
    # monitor.fname = "abhishek"
    # print(monitor.email)

    # USAGE OF SETTER DECORATOR
    print("BEFORE => ", monitor.fname, monitor.lname, monitor.email)
    monitor.email = "abhishek.kumar@gmail.com"
    print("AFTER => ",  monitor.fname, monitor.lname, monitor.email)

    del monitor.email
    print("AFTER DELETING => ", monitor.email)
