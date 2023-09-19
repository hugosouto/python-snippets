import time

iterations = 10000000

# List Comprehension
start_time = time.time()
evens = [x for x in range(iterations)] # a list comprehension
end_time = time.time()
exec_time_lc = end_time - start_time
print('List Comprehension runtime:', exec_time_lc)


# Generator
start_time = time.time()
nums = list((x for x in range(iterations) if x % 2 == 0))
end_time = time.time()
exec_time_gn = end_time - start_time
print('Generator runtime:         ', exec_time_gn)

# Ratio
print("Generator runtime is", exec_time_gn/exec_time_lc * 100, "% the List Comprehension runtime.")