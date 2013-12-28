class FibClass(object):

    def __init__(self):
        self.fibs = [1, 1]

    def __iter__(self):
        return self

    def next(self):
        self.fibs.append( self.fibs[-1] + self.fibs[-2] )
        return self.fibs[-1]


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

# David Beazley's stuff:
# os.walk = generator containing 3-tuples: 
# ('dirname', ['subdirs', 'in', 'dir'], ['files', 'in', 'dir']) 
# for each subdir (including arg itself)

def make_and_use_iter(obj):
    _iter = iter(obj)
    while True:
        try:
            x = _iter.next()
        except StopIteration:
            break
        # statements
