'''
today i learned about loops in python.
loops help us repeat tasks without writing the same code again and again.
python mainly has two types of loops — for and while.
'''

# for loop example
print("Counting from 1 to 5 using for loop:")
for i in range(1, 6):
    print(i)

'''
range(1, 6) means numbers from 1 to 5.
"for" goes through each number one by one.
'''

# while loop example
print("\nCounting from 1 to 5 using while loop:")
x = 1
while x <= 5:
    print(x)
    x += 1  # increases x by 1 in every loop

'''
while loop keeps running until the condition becomes false.
perfect when you don’t know how many times it should run.
'''

# real-life example
print("\nGym time! counting pushups")
for pushup in range(1, 6):
    print("Pushup:", pushup)

'''
notes:
1. loops save time and make code shorter.
2. for loop → best when you know how many times to run.
3. while loop → best when condition controls the stop point.
'''

# thanks for reading