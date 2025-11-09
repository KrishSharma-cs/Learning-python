'''
today i learned about break and continue statements.
they are used to control how loops run.
sometimes you want to stop early, sometimes just skip a step.
'''

# break example
print("Break example:")
for i in range(1, 11):
    if i == 6:
        print("Loop stopped at", i)
        break
    print("Number:", i)

'''
break → stops the loop completely when condition is true.
useful when you find what you’re looking for and want to stop.
'''

# continue example
print("\nContinue example:")
for i in range(1, 11):
    if i == 5:
        continue  # skips the rest of the code for this round
    print("Number:", i)

'''
continue → skips that one round and moves to the next.
useful when you want to ignore something and keep going.
'''

# real-life example
print("\nSkipping Sundays in a weekly workout plan")
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

for day in days:
    if day == "Sun":
        continue
    print("Workout day:", day)

'''
notes:
1. break → stops the loop completely.
2. continue → skips one loop and moves to the next.
3. both are used to control flow inside loops.
'''

# thanks for reading
