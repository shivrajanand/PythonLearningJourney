"""   

Iterable  => Python object which has __iter__() or __getitem__() is defined.
             If these methods are used on the iterable object it returns
             an Iterator
Iterators => Python object that has __next__() defined in it
Iteration => Process of iterating an object is called Iteration
Generators => It is a sub-class of iterator which can be iterated only 
              once.
              range() is a generator as it generates new values at the
              moment of iteration. Once iterated though a value it cannot
              iterate again on that value.

#### USER DEFINED GENERATOR ####
return statement => once return is executed, function terminates, therefore no statement after it is 
                    executed or even considered

print statement => print writes the output on console

yield => yield generates values on the fly

"""

# User defined generator


def fibonacci_generator(n):
    t1, t2 = 0, 1

    for i in range(1, n+1):
        yield t1
        t1, t2 = t2, (t1+t2)



if __name__ == '__main__':
    g = fibonacci_generator(10000)
    for item in g:
        print(item)
