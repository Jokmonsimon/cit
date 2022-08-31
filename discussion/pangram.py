# Python program to Check if the string is pangram
import string
  
def ispangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
  
    return True
      
# Pangram Code to check
string = 'the quick brown fox jumps over the lazy dog'
if(ispangram(string) == True):
    print("Yes")
else:
    print("No")