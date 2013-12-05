def fib_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def fib_list(n):
    fg = fib_gen()
    lst = []
    for i in range(n):
        lst.append(fg.next())
    return lst
