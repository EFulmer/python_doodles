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

def print_body_line():
    print '|      ',

def print_two_h_border():
    do_twice(print_h_border)
    print '+'

def print_two_cell_body_line():
    do_twice(print_body_line)
    print '|'

def print_two_cell_bodies():
    do_four(print_two_cell_body_line)

def print_two_by_two():
    print_two_h_border()
    print_two_cell_bodies()
    print_two_h_border()
    print_two_cell_bodies()
    print_two_h_border()

print_two_by_two()

# 2. Write a function that draws a similar grid with four rows and four 
# columns.

def print_four_h_borders():
    do_four(print_h_border)
    print '+'

def print_four_body_lines():
    do_four(print_body_line)
    print '|'

def print_four_cell_bodies():
    do_four(print_four_body_lines)

def print_one_top_cell():
    print_four_h_borders()
    print_four_cell_bodies()

def print_four_by_four():
    do_four(print_one_top_cell)
    print_four_h_borders()

print_four_by_four()
