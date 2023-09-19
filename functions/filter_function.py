# Returns True if n is a perfect square, and False otherwise

def is_perfect_square(n):
    """
    Returns True if the given number is a perfect square, False otherwise.
    
    Args:
    - n: An integer to be checked for perfect square.
    
    Returns:
    - A boolean value indicating whether the given number is a perfect square or not.
    """
    return (n ** 0.5).is_integer()

numbers = [3, 4, 37, 9, 7, 32, 25, 81, 79, 100]

perfect_squares = filter(is_perfect_square, numbers)

print(list(perfect_squares))