# This code is an exercise in learning Python Generators from the Codecademy 
# documentation.
# 
# Available at: https://www.codecademy.com/resources/docs/python/generators.

def return_evens(lst):
    """
    A generator function that yields even numbers from a given list.

    Parameters:
    lst (list): A list of integers.

    Yields:
    int: Even numbers from the input list.

    """
    for l in lst:
        if l % 2 == 0:
            yield l

if __name__ == '__main__':
    eggs = [x for x in range(20)]

    print(list(return_evens(eggs)))
    # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]