#!/usr/bin/python3

'''
 Write a program to display only those numbers from a list that satisfy the following conditions

- The number must be divisible by five
- If the number is greater than 150, then skip it and move to the next number
- If the number is greater than 500, then stop the loop
  given `numbers = [12, 75, 150, 180, 145, 525, 50]`
'''
# Declare list values
numbers = [12, 75, 150, 180, 145, 525, 50]
new_list = []

# Iterate through the list
for num in numbers:
    if num > 150:
        if num > 500:
            break
        continue
    if num % 5 == 0:
        new_list.append(num)
print(new_list)