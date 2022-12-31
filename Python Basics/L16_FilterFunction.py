def is_greater_than_5(num):
    return num > 5


if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    is_greater_than_5 = list(filter(is_greater_than_5, list1))

    print(is_greater_than_5)


# filter(function, iterable) function iterates through the iterable and runs every element in the boolean return type function and then returns a filter object that contains all the objects that returns all the elements that returns true for the function given.

# usually the filter object is converted into an iterable list
