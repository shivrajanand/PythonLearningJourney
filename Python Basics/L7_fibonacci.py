import matplotlib.pyplot as plt

def fibonacci(n):
    """This functionr returns fibonacci term for nth index where n is a natural number"""
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2))


if __name__ == '__main__':
    num = int(input("Enter term index of Fibonacci serries: "))

    print(fibonacci(num))
    x_list = []
    y_list = []
    for i in range(1, num+1):
        val = fibonacci(i)
        print(val, end=", ")
        x_list.append(i)
        y_list.append(val)


    plt.plot(x_list, y_list)
    plt.show()

    # for i in range(4):
    #     print(fibonacci(i))


