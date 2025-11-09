'''
today i learned nested loops.
nested loop = a loop inside another loop.
useful when you want to repeat something within a repeat.
'''

# simple nested loop
for i in range(1, 4):        # outer loop
    for j in range(1, 3):    # inner loop
        print(i, j)

'''
explanation:
i changes slower (like hours)
j changes faster (like minutes)
'''

# small pattern using nested loop
print("\nstar pattern:")

for i in range(1, 6):
    print("*" * i)

'''
notes:
1. nested loops help in patterns, tables, grids.
2. '*' * i means: repeat * i times.
   (python can repeat strings using *)
'''

# thanks for reading
