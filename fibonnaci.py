def fibonacci(num):
    a = 0
    b = 1

    for x in range(num):
        print(a,end=" ")
        c = a + b
        a = b
        b = c

    return c


print(fibonacci(32))
