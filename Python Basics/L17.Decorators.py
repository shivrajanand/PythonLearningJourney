def function1():
    print("Subscribe Now")


def funcret(num):
    if num == 0:
        return print
    if num == 1:
        return sum


def dec1(func1):
    def nowexec():
        print("Executing Now")
        func1()
        print("Exeuted")

    return nowexec


@dec1
def func3():
    print("this is func3")


if __name__ == '__main__':
    # func2 = function1
    # del function1
    # func2()

    # a = funcret(0)
    # print(a)

    # func3 = dec1(func3)
    # func3()

    func3()
