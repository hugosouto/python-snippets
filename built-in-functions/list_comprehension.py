# List comprehension is a way to create a list using a for loop in one line.
# It covers using list comprehension in Python for:
# 1. Faster For Loops
# 2. Simplified Conditional Statements
# 3. String Manipulation

# This code is made for learning purposes 
# Resource: https://www.youtube.com/watch?v=SNq4C988FjU

# Imports
import time


# 1. Faster For Loops
fruits = ['apples', 'bananas', 'strawberries']


# 1.1. Print

# 1.1.1. Print using a for loop
for fruit in fruits:
    print(fruit)

# 1.1.2. Print using list comprehension
[print(fruit) for fruit in fruits]


# 1.2. Change Lower Case to Upper Case

# 1.2.1. Using a for loop
# for fruit in fruits:
    # fruits[fruits.index(fruit)] = str(fruit).upper()
# print(fruits)

# 1.2.2. Using a list comprehension
print([str(fruit).upper() for fruit in fruits])


# 2. Conditional Loops

bits = [False, True, False, False, True, False, False, True]
print(bits)

# 2.1. Change True/False to 0/1 with For Loop

# 2.1.1 Traditional (wrong) way: boolean compared to True
new_bits_fl = []
for b in bits:
    if b == True: 
        new_bits_fl.append(1)
    else:
        new_bits_fl.append(0)
print('new_bits_fl_1:', new_bits_fl)

# 2.1.2 Traditional (right) way: boolean 'True' verification
new_bits_fl = []
for b in bits:
    if b is True: 
        new_bits_fl.append(1)
    else:
        new_bits_fl.append(0)
print('new_bits_fl_2:', new_bits_fl)

# 2.1.3 Better way: direct boolean verification
new_bits_fl = []
for b in bits:
    if b:
        new_bits_fl.append(1)
    else:
        new_bits_fl.append(0)
print('new_bits_fl_3:', new_bits_fl)


# 2.2. Change True/False to 0/1 with List Comprehension
new_bits_lc = [1 if b else 0 for b in bits]
print('new_bits_lc:', new_bits_lc)

# 3. String Manipulation

string = 'HelloMyNameIsHugo'

# 3.1. CamelCase to String with Spaces Using For Loops

string_list = list(string)
new_string = ['']
for i in string_list:
    if i.isupper():
        new_string.append(' ')
        new_string.append(i)
    else:
        new_string.append(i)

new_string = ''.join(new_string)
if new_string.startswith(' '):
    new_string = new_string[1:]
    
print(new_string)
