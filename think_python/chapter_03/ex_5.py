# Exercise 3.5
# This exercise can be done using only the statements and other features we 
# have learned so far.
# 
# 1. Write a function that draws a grid like the following:
# +----+----+
# |    |    |
# |    |    |
# |    |    |
# |    |    |
# +----+----+
# |    |    |
# |    |    |
# |    |    |
# |    |    |
# +----+----+
#
# Hint: to print more than one value on a line, you can print a comma-separated
# sequence:
# 
# print '+', '-'
# 
# If the sequence ends with a comma, Python leaves the line unfinished, so the
# value printed next appears on the same line.
# 
# print '+',
# print '-'
# 
# The output of these statements is '+ -'.
# 
# A print statement all by itself ends the current line and goes to the next 
# line.

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_h_border():
    print '+ - - -',

def print_body():
    print '|      ',

def print_grid_1():
    do_twice(print_h_border)
    print '+'
    do_twice(print_body)
    print '|'
    do_twice(print_body)
    print '|'
    do_twice(print_body)
    print '|'
    do_twice(print_body)
    print '|'

print_grid_1()
print_grid_1()
do_twice(print_h_border)
print '+'
