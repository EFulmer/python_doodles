# From http://www.oreillynet.com/lpt/a/5463

import unittest


# Here's our "unit".
def IsOdd(n):
        return n % 2 == 1


# Here's our "unit tests".
# Eric's notes:
# unittest.TestCase must be subclassed to be of any use.
class IsOddTests(unittest.TestCase):
    
    # Eric's notes:
    # all "test*" methods are test suites.
    # guess: all "test*"s run when unittest.main() is called?
    # if implemented, setUp called before each method and tearDown
    # after each.
    def testOne(self):
        self.failUnless(IsOdd(1))
    
    def testTwo(self):
        self.failIf(IsOdd(2))


def main():
    unittest.main()


if __name__ == '__main__':
    main()
