# Exercise 3.2.
# Move the function call back to the bottom and move the definition of 
# print_lyrics after the definition of repeat_lyrics. What happens when you run
# the program?

def repeat_lyrics():
	print_lyrics()
	print_lyrics()

def print_lyrics():
	print "I'm a lumberjack, and I'm okay."
	print "I sleep all night and I work all day."

repeat_lyrics()

# Answer:
# It prints out the lyrics twice. It does this because it doesn't actually 
# run the statements inside the function until the function gets called. Which 
# makes sense: if the function does take arguments, then when you define it, 
# there aren't any values given for the arguments, so how is Python going to 
# run the function?