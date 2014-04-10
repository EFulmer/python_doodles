# Exercise 3.4.
# A function object is a value you can assign to a variable or pass as an 
# argument. For example, do_twice is a function that takes a function object 
# and calls it twice:
# 
# def do_twice(f):
#     f()
#     f()
#
# Here's an example that uses do_twice to call a function named print_spam 
# twice.
# 
# def print_spam():
#     print 'spam'
#

# 1. Type this example into a script and test it. 

def do_twice(f):
    f()
    f()


def print_spam():
    print 'spam'


# 2. Modify do_twice so that it takes two arguments, a function argument and a
# value, and calls the function twice, passing the value as an argument.

def do_twice(f, x):
    f(x)
    f(x)


# 3. Write a more general version of print_spam, called print_twice, that takes 
# a string as a parameter and prints it twice.

def print_twice(s):
    print s
    print s


# 4. Use the modified version of do_twice to call print_twice twice, passing 
# 'spam' as an argument.

do_twice(print_twice, 'spam')

# 5. Define a new function called do_four that takes a function object and a 
# value and calls the function four times, passing the value as a parameter.
# There should only be two statements in the body of this function, not four.

def do_four(f, x):
    do_twice(f, x)
    do_twice(f, x)
