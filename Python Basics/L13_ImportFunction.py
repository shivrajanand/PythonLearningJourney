import  sys
x = sys.path

for item in x:
    print(item)

# if we use "import module" statement then the interpreter looks for the module hierarchially down in the list x