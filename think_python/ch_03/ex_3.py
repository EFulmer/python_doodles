# Exercise 3.3.
# Python provides a built-in function called len that returns the length of a 
# string, so the value of len('allen') is 5. 
# 
# Write a function named right-justify that takes a string named s as a 
# parameter and prints the string with enough leading spaces so that the last 
# letter of the string is in column 70 of the display.


def right_justify(s):
    # just printing s normally will put its rightmost character at the 
    # len(s)-th column of the display, so we want to put 70 - len(s) blank 
    # spaces between the start of s and the leftmost column of the display:
    # if len(s) is 70 then we put 0 spaces in front of it, if len(s) > 70 then 
    # we're out of luck!
    last = 70
    padding = last - len(s)
    print ' ' * padding + s

