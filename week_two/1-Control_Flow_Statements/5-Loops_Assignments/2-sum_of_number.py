#!/usr/bin/python3

# Calculate the sum of all numbers from 1 to a given number
given_number = int(input("Please enter the number: "))
sum_of_number = 0
for number in range(1, given_number + 1):
    sum_of_number += number
print("sum of {} is: {}".format(given_number, sum_of_number))