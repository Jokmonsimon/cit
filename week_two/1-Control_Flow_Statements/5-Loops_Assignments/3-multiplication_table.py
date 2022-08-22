#!/usr/bin/python3

# Write a program to print multiplication table of a given number. E.g. if number is 2, then output should be 2, 4, 6, 8 ...

# Multiplication Table (from 1 to 12)

# Prompt user to enter number
num = int(input("Display Multpilcation Table of? "))

# Iterate 10 times from i = 1 to 12
for i in range(1, 13):
    print(num, 'x', i, '=', num*i)