# __dict__ is an attribute of a class that returns all instances of the object

class Employee: #Class name should be written in Title Case
    no_of_leaves = 10

if __name__ == '__main__':
    harry = Employee()
    rohan = Employee()

    harry.name = "Harry"
    harry.salary = 455
    harry.role = "Instructor"

    rohan.name = "rohan"
    rohan.salary = 4554
    rohan.role = "Intern"

    # print(Employee.no_of_leaves)
    # print(rohan.__dict__)
    
    rohan.no_of_leaves = 8 #This creates a new instace variable of rohan that is an independent property of object

    # print(rohan.__dict__)
    # print(Employee.__dict__)
    # print(Employee.no_of_leaves)
    # print(rohan.no_of_leaves)
    i = 1
    for key, value in Employee.__dict__.items():
        print(f"{i} {key} <===> {value}")
        i += 1


    