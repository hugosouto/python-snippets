from itertools import product

# Data
A = [1, 2]
B = [3, 4, 5]

# For Loop concatenation
print('For Loop iteration:')
lst = []
for a in A:
    for b in B:
        lst.append(str(a) + str(b))
print(lst)

# List Comprehension concatenation
print('List Comprehension iteration:')
print([str(a) + str(b) for a in A for b in B])

# Generator concatenation
print('Generator iteration:')
gen = (str(a) + str(b) for a in A for b in B)
print(list(gen))

# Itertools Product concatenation
print('Itertools Product iteration:')
prd = product(A, B)
prd_lst = list(prd)
temp1 = []
for i in prd_lst:
    temp2 = []
    for j in list(i):
        temp2.append(str(j))
    temp1.append(''.join(temp2)) 
print(temp1)

# Itertools Product unpacking
print('EXTRA: Itertools Product with unpacking:')
C = [[1,2,3],[3,4,5]]
print('C:', C)
print('*C:', *C)
print(list(product(*C)))