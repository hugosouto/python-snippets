# This code is made for learning purposes 
# Resource: https://www.youtube.com/watch?v=SNq4C988FjU

# It covers using list comprehension in Python for:
# 1. Faster For Loops
# 2. Simplified Conditional Statements
# 3. String Manipulation

# List comprehension is a way to create a list using a for loop in one line.

# 1. Faster For Loops

fruits = ['apples', 'bananas', 'strawberries']

# Print using a for loop
for fruit in fruits:
    print(fruit)

# Print using list comprehension
[print(fruit) for fruit in fruits]

# Change to upper case using a for loop
for fruit in fruits:
    fruits[fruits.index(fruit)] = str(fruit).upper()

print(fruits)

# Change to upper case using a list comprehension
fruits_lc = [str(fruit).upper() for fruit in fruits]
print(fruits_lc)