def funargs(x, *args, **kwargs):
    print(f"{x}^2 = {x^2}")

    for item in args:
        print(item)

    for key, value in kwargs.items():
        print(f"{key} is a {value}")


#  *args is just a convention of using multiple arguments in form of tuple. it can be given any other ame like *variable

# Always write normal arguments before * arguamemts

kw = {"Rohan": "Monitor", "Harry": "Fitness-Instructor",
      "The Programmer": "Coordinator"}

listh = ["a", "b", "c", "d"]

# for key, value in kw.items():
#     print(f"{key} is a {value}\n")

funargs(5, *listh, **kw)
