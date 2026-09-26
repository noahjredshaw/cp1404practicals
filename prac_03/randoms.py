import random

# What did you see on line 1?
# What was the smallest number you could have seen, what was the largest?
# I saw 8.
# The smallest number is 5, and the largest is 20.

# What did you see on line 2?
# What was the smallest number you could have seen, what was the largest?
# Could line 2 have produced a 4?
# I saw 5.
# 3 is the smallest, and 9 is the largest. Line 2 can not produce a 4 as it is capable of only producing odd numbers between 3 and 9 inclusive.

# What did you see on line 3?
# What was the smallest number you could have seen, what was the largest?
# I saw 4.307980187121439
# The smallest number is 2.5, and the largest is 5.5. Interestingly: the longest number of the highest value is: 5.49999999999999.

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))