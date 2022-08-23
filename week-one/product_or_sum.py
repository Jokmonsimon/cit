#!/usr/bin/python3

val1 = int(input("Please enter the first value: "))
val2 = int(input("Please enter the second value: "))

addition = val1 + val2
product = val1 * val2

if (product <= 1000):
    print("The product of {} and {} is {}".format(val1, val2, product))
else:
    print("The sum of {} and {} is {}".format(val1, val2, addition))