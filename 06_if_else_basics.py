'''
today i learned how to make python take decisions.
we use "if", "elif", and "else" to tell python what to do in different situations.
'''

# basic example
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult ")
else:
    print("You are still young, enjoy learning ")

'''
how it works:
"if" checks a condition.
if the condition is true, python runs that block.
if it’s false, python runs the "else" part.
'''

# another example
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A ")
elif marks >= 75:
    print("Grade: B ")
elif marks >= 50:
    print("Grade: C ")
else:
    print("Grade: F ")

'''
use "elif" when there are multiple conditions.
only one block runs — the first one that’s true.
indentation (spaces) is very important here.
'''

# thanks for reading
