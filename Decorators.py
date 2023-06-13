# This code calculates the total execution time of the main() function.
# main() is a function that counts from 0 to 10,000,000.

# Import the time module so that we can use time.time() to track the current time
import time

# Create a function that will be used as a decorator
def calculate_duration(func):
    # Create a wrapper function that will calculate and print out the total execution time
    def wrapper():
        # Record the start time
        start = time.time()
        # Call the decorated function
        func()
        # Record the end time
        end = time.time()

        # Print out the total execution time
        print("[{func}] Total execution time: {total_time}".format(
            func=func.__name__,
            total_time=str(end - start))
        )

    # Return the wrapper function
    return wrapper

# Decorate the main() function
@calculate_duration
def main():
    # Count from 0 to 10,000,000
    for n in range(0, 10000000):
        pass

# Call the decorated function
main()