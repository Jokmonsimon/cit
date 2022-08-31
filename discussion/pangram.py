# Python program to Check if the string is pangram
import string
  
def ispangram(str):
    # Declare Alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # Loop through alphabet
    for char in alphabet:
        if char not in str.lower():
            return False
  
    return True
      
# Pangram Code to check
string = 'the quick brown fox jumps over the lazy dog'
# Check if the string exist
if(ispangram(string) == True):
    print("Yes")
else:
    print("No")