"""
Classes are like templates or blueprints
Objects are entities crreated on the templates
Objects are instances of classes

OOPS run on concept of DRY (Dont Repeat Yourself)
"""

class student:
    pass #pass signifies nothing


if __name__ == '__main__':
    harry = student()
    larry = student()

    harry.name = "Harry"
    harry.std = 12
    harry.section = 'A'

    print(harry.name)