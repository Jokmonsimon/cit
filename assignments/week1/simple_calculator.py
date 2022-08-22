#!/usr/bin/python3

val1 = int(input("Please enter the first value: "))
val2 = int(input("Please enter the second value: "))

addition = val1 + val2
difference = val1 - val2
division = val1 / val2
product = val1 * val2
modulus = val1 % val2

print("The sum of {} and {} is {}".format(val1, val2, addition))
print("The difference of {} and {} is {}".format(val1, val2, difference))
print("The division of {} and {} is {}".format(val1, val2, division))
print("The product of {} and {} is {}".format(val1, val2, product))
print("The modulus of {} and {} is {}".format(val1, val2, modulus))