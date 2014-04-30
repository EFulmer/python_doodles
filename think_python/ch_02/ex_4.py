# Exercise 2.4.
# Practice using the Python interpreter as a calculator:

# 1. The volume of a sphere with radius r is 4/3 * pi * r^3. What is the volume
# of a sphere with radius 5? Hint: 392.7 is wrong!
pi = 3.14159265359
r = 5
volume = (4/3) * pi * (r**3)

# 2. Suppose the cover price of a book is $24.95, but bookstores get a 40% 
# discount. Shipping costs $3 for the first copy and 75 cents for each 
# additional copy. What is the total wholesale cost for 60 copies?
book_price = 24.95
ship_one = 3
ship_more = 0.75
total_cost = (book_price+ship_one) + (book_price+ship_more) * 59

# 3. If I leave my house at 6:52am and run 1 mile at an easy pace (8:15 per 
# mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, 
# what time do I get home for breakfast?
easy = 8 + (15/60)
tempo = 7 + (12/60)
total_time = easy + 3*tempo + easy
leave_home_at = 6*60 + 52
back_home_at = leave_home_at + total_time
back_home_at_hrs = back_home_at // 60
back_home_at_secs = back_home_at - (back_home_at_hrs*60)
print back_home_at_hrs
print back_home_at_secs