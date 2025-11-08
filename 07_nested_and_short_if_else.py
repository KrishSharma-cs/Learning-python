'''
today i learned about nested if and short if-else (ternary) in python.
nested if means putting one if inside another — like thinking step by step.
'''

# nested if example
age = int(input("Enter your age: "))

if age > 0:
    if age < 18:
        print("You are a teenager")
    elif age < 60:
        print("You are an adult")
    else:
        print("You are a senior citizen")
else:
    print("Age can’t be negative!")

'''
nested if:
used when one condition depends on another.
example: checking something only if the first condition is true.
'''

# short if-else (also called ternary)
marks = int(input("Enter your marks: "))

# one line version
result = "Pass" if marks >= 40 else "Fail"
print("Result:", result)

'''
short if-else:
used when you want to write a quick condition in one line.
syntax →  value_if_true  if condition else  value_if_false
'''

# thanks for reading
