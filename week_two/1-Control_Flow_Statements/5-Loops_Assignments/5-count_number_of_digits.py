#!/usr/bin/python3

# Write a program to count the total number of digits in a number using a while loop. given number `4673453`
given_number = 4673453
count = 0

while given_number != 0:
    given_number //= 10
    count += 1

print("Number of digits is: {}".format(str(count)))