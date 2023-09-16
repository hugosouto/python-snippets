# This code is made for learning purposes 
# Resource: https://www.youtube.com/watch?v=SNq4C988FjU

# It covers using list comprehension in Python for:
# 1. Faster For Loops
# 2. Simplified Conditional Statements
# 3. String Manipulation

# List comprehension is a way to create a list using a for loop in one line.

# 1. Faster For Loops
fruits = ['apples', 'bananas', 'strawberries']

# Using a for loop
for fruit in fruits:
    print(fruit)

# Using list comprehension
[print(fruit) for fruit in fruits]