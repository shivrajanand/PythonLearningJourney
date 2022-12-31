def square(x):
    return x*x

def cube(x):
    return x*x*x

if __name__ == '__main__':
    # number = ['3', '34', '64']
    # number = list(map(int, number))

    #map(functionn, object) => map function executes the function passed onto every sub-object of the object given and also returns an object so often have to convert it into list or something else

    # Basically map() applies a functions to all elements of a list
   

    # number[2] = number[2] + 1  
    # print(number[2])


    num = [2, 3, 5, 6, 76, 3, 3, 2]

    # square = list(map(lambda x: x*x, num))
    # print(square)

    func = [square, cube]

    for i in range(5):
        val = list(map(lambda x: x(i), func))
        print(val)