# 1. 
# Write a function called square that takes a parameter named t, which is a
# turtle. It should use the turtle to draw a square. 
# 
# Write a function call that passes bob as an argument to square, and then run
# the program again.

from swampy.TurtleWorld import *


def square(t):
    for i in range(4):
        fd(t, 100)
        lt(t)


world = TurtleWorld()
bob = Turtle()
square(bob)


# 2.
# Add another parameter, named length, to square. Modify the body so length of
# the sides is length, and then modify the function call to provide a second 
# argument. Test your program with a range of values for length.


def square_2(t, length):
    for i in range(4):
        fd(t, length)
        lt(t)


square_2(bob, 150)


# 3.
# The functions lt and rt make 90-degree turns by default, but you can provide 
# a second argument that specifies the number of the degrees. For example, 
# lt(bob, 45) turns bob 45 degrees to the left.
# 
# Make a copy of square and change the name to polygon. Add another parameter 
# named n and modify the body so it draws an n-sided regular polygon. Hint: The
# exterior angles of an n-sided regular polygon are 360/n degrees.


def polygon(t, length, n):
    for i in range(n):
        fd(t, length)
        lt(t, 360 - 360/n)


polygon(bob, 50, 4)

wait_for_user()
