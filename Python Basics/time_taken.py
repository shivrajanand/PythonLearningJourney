import time


def fibonacci_recur(n):
    """This functionr returns fibonacci term for nth index where n is a natural number"""
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return (fibonacci_recur(n-1) + fibonacci_recur(n-2))


def fibonacci_loop(n):
    num1 = 0
    num2 = 1

    for i in range(2, n):
        temp = num1 + num2
        num1 = num2
        num2 = temp

    return num2
 

def dec1(func1, name):
    def executeNow():
        initial = time.time()
        func1
        final = time.time()

        time_taken = final - initial
        print(f"Time taken to run {name} is {time_taken}")

    return executeNow()


if __name__ == '__main__':

    dec1(fibonacci_recur(35), "Recursive Fibonacci")
