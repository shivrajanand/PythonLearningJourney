import time


def fibonacci_recur(n):
    """This functionr returns fibonacci term for nth index where n is a natural number"""
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2))


def fibonacci_loop(n):
    num1 = 0
    num2 = 1

    for i in range(2, n):
        temp = num1 + num2
        num1 = num2
        num2 = temp

    return num2


initial_time = time.time()  # returns number of tick, 1 tick = 1 second
print(fibonacci(35))
final_time = time.time()

print(f"Net time for recursive method = {final_time-initial_time}")

initial_time_new = time.time()  # returns number of tick, 1 tick = 1 second


for i in range(1, 100):
    fibonacci_loop(35)

final_time_new = time.time()

print(f"Net time for iterative method = {(final_time_new-initial_time_new)/100}")

print(f"initial = {initial_time_new}, final = {final_time_new}")

