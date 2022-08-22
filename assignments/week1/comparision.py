#!/usr/bin/python3

val1 = input("Please enter the first value: ")
val2 = input("Please enter the second value: ")

if ( val1 == val2 ):
   print("First Line: Great! {} is equal to {}".format(val1, val2))
else:
   print("First Line: Oh! {} and {} are not equal".format(val1, val2))

if ( val1 != val2 ):
   print("Second Line: Great! {} is not equal to {}".format(val1, val2))
else:
   print("Second Line: Oh! {} is equal to {}".format(val1, val2))

if ( val1 == val2 ):
   print("Third Line: Great! {} is not equal to {}".format(val1, val2))
else:
   print("Third Line: Oh! {} is equal to {}".format(val1, val2))

if ( val1 < val2 ):
   print("Fourth Line: Great! {} is less than {}".format(val1, val2))
else:
   print("Fourth Line: Oh! {} is not less than {}".format(val1, val2))

if ( val1 > val2 ):
   print("Fifth Line: Great! {} is greater than {}".format(val1, val2))
else:
   print("Fifth Line: Oh! {} is not greater than {}".format(val1, val2))
