#Global Variable - Can be accessed by any function
#Local Variable - Can be accessed ithin locally in a function

#global keyword gives permission to change value of the variable globally to a function

x = 20

def function1():
    x = 30
    # global x
    x = x + 20

    print("Inside Function",x)

function1()
print("Inside Main",x)