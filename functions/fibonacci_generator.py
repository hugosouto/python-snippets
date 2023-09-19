# This code is an exercise in learning Python functions using the yield return
# from the Codecademy documentation.
# 
# Available at: https://www.codecademy.com/resources/docs/python/functions.

# Function to produce infinite Fibonacci numbers
def fibonacci():
  """
  A generator function that yields the Fibonacci sequence indefinitely.

  Yields:
    int: The next number in the Fibonacci sequence.
  """
  # Generate first number
  a = 1
  yield a

  # Generate second number
  b = 1
  yield b

  # Infinite loop
  while True:
    # Return sum of a + b
    c = a + b
    yield c
    # Function resumes loop here on next call
    a = b
    b = c

# Iterate through the Fibonacci sequence until a limit is reached
for num in fibonacci():
  if num > 50:
    break
  print(num)


list = []
list = list.append(fibonacci())
print(list)

# def fibonacci():
#     # Generate first number
#     a = 1
#     return a

# while fibonacci() < 200:
#     print(fibonacci())