from functools import reduce

if __name__ == '__main__':

    list1 = [1, 2, 3, 4, 5, 6, 7, 8]

    prod = reduce(lambda x, y: x*y, list1)

    print(prod)
