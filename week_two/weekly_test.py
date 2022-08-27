# CIT Python End of Week Two Quiz

# Question 1
print('1. Use the get method to print the value of the "model" key of the car dictionary.')

car = { "brand": "Ford", "model": "Mustang", "year": 1964 }

'''
Options
A. print(car['model'])
B. print(get(car.model))
C. print(car.get('model'))
D. print(get('model'))
'''

# Workout
# print(car.get('model')) 

# Results
print("Output: Mustang")
print("Correct Answer: print(car.get('model'))")
print("=================================================================")

# Question 2
print("2. What data type is this?")

quiz = {"Do you help out at home? " : "yes", "Do you beleive in Santa? " : "yes"}

'''
Options
A. Dictionart
B. List
C. Set
D. Dictionary
E. String
'''

# Workout
# print(type(quiz))

# Results
print("Output: <class 'dict'>")
print("Correct Answer: Dictionary")
print("=================================================================")

# Question 3
print("3. Which symbol surrounds a dictionary?")

'''
Options
A. [
B. (
C. {
D. :
'''
print("Correct Answer: {")
print("=================================================================")

# Question 4
print("4. Is this code correct?")

quiz = {"Do you help out at home? ":"yes", }

'''
Options
A. Yes
B. No
C. Maybe
'''

# Workout
# print(quiz)
# print(type(quiz)) # Output: <class 'dict'> 

# Results
print("Output1: {'Do you help out at home? ': 'yes'}")
print("Output2: <class 'dict'>")
print("Correct Answer: No") # Though the output is correct, comma is added only in Tuple when it is only having a single value
print("=================================================================")

# Question 5
print("5. Is this code correct?")
 
quiz = {"Do you help out at home? " : "no it is not correct"}

'''
Options
A. Yes
B. No
C. Maybe
'''

# Workout
# print(quiz)
# print(type(quiz))

# Results
print("Output1: {'Do you help out at home? ': 'yes'}")
print("Output2: <class 'dict'>")
print("Correct Answer: Yes")
print("=================================================================")

# Question 6
print("6. Write the output of the following codes.")
dl = {1:10,2:20,3:30,4:40, 5:50}
dl.items()

'''
Options
A. [1, 2, 3, 4, 5]
B. [10, 20, 30, 40, 50]
C. [(1, 10), (2, 20), (3, 30), (4, 40), (5, 50)]
'''

# Workout
# print(dl.items())

# Results
print("Output: dict_items([(1, 10), (2, 20), (3, 30), (4, 40), (5, 50)])")
print("Correct Answer: [(1, 10), (2, 20), (3, 30), (4, 40), (5, 50)]")
print("=================================================================")

# Question 7
print("7. What is the output of this program?")
dl = {1:10, 2:20, 3:30, 4:40}
d2 = {5:50, 6:60, 7:70}
dl.update(d2)

print(dl)

'''
Options
A. [(1, 10), (2, 20), (3, 30), (4, 40), (5, 50)]
B. {1:10, 2: 20, 4: 40, 5: 50, 6: 60, 7: 70}
C. {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70}
D. [1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70]
'''

# Results
print("Output: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70}")
print("Correct Answer: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70}")
print("=================================================================")

# Question 8
print("8. What will be the result of this program?")
fruits = ["Apple", "Banana", "Mangoes"]
# print(fruits[3])

'''
Options
A. Mangoes
B. None
C. Banana
D. Index Error
'''

# Results
print("Output: IndexError: list index out of range")
print("Correct Answer: IndexError")
print("=================================================================")

# Question 9
print("9. What is a variable?")

'''
Options
A. A box(memory location) where you store values
B. Data type
C. A type of memory
D. A python keyword
'''

# Answer
print("Correct Answer: A box(memory location) where you store values")
print("=================================================================")

# Question 10
print("10. Find the output of the following program:")

D = dict()
for x in enumerate(range(2)):
    D[x[0]] = x[1]
    D[x[1] + 7] = x[0]
print(D)

'''
Options
A. {0: 1, 7: 0, 1: 1, 8: 0}
B. KeyError
C. {1: 1, 7: 2, 0: 1, 8: 1}
D. {0: 0, 7: 0, 1: 1, 8: 1}
'''

# Results
print("Output: {0: 0, 7: 0, 1: 1, 8: 1}")
print("Correct Answer: {0: 0, 7: 0, 1: 1, 8: 1}")
print("=================================================================")

# Question 11
print("11. Find the output of the following program:")

D = {1: 1, 2: '2', '1': 1, '2': 3}
D['1'] = 2
print(D[D[D[str(D[1])]]])

'''
Options
A. KeyError
B. 2
C. 1
D. 3
'''

# Results
print("Output: 3")
print("Correct Answer: 3")
print("=================================================================")

# Question 12
print("12. Find the output of the following program:")

D = {1 : {'A' : {1 : "A"}, 2 : "B"}, 3 :"C", 'B' : "D", "D": 'E'}
# D = {1: {'A': {1: "A"}, 2: "B"}, 3: "C", 'B': "D", "D": 'E'}
# print(D[D[D[1][2]]], end = " ")
# print(D[D[1]["A"][2]]) 

'''
Options
A. E Key Error
B. C B
C. DB
D. BD
'''

# Results
print("Output1: E")
print("Output2: Key Error: 2")
print("Correct Answer: E Key Error")
print("=================================================================")

# Question 13
print("13. Which of these about a dictionary is false?")

'''
Options
A. None of the above
B. The keys of a dictionary can be accessed using values
C. The values of a dictionary can be accessed using keys
D. Dictionaries may or may not be ordered
'''

# Answer
print("Correct Answer: The keys of a dictionary can be accessed using values")
print("=================================================================")

# Question 14
print("14. Which of the following are true of Python lists?")

'''
Options
A. All elements in a list must be of the same type
B. These represent the same list: ['a', 'b', 'c'] ['c', 'a', 'b']
C. A list may contain any type of object except another list
D. There is no conceptual limit to the size of a list
E. A given object may appear in a list more than once
'''

# Answer
print("Correct Answer: A given object may appear in a list more than once")
print("=================================================================")

# Question 15
print("15. Which of the following is mutable?")

'''
Options
A. Lists
B. Sets
C. Strings
D. Tuples
E. None of the above
'''

# Answer
print("Correct Answer: Lists")
print("=================================================================")

# Question 16
print("16. What will be the output of the following code?")
nums = list({1: 'One', 2: 'Two'})
print(nums)

'''
Options
A. Syntax Error
B. {1, 2}
C. [1, 2]
D. (1, 2)
'''

# Answer
print("Correct Answer: [1, 2]")
print("=================================================================")

# Question 17
print("17. The list.pop() function will: ")

'''
Options
A. Remove the first element from the list
B. Remove the last element from the list
C. Remove the last element from the list and return it
D. None will be removed
'''

# Answer
print("Correct Answer: Remove the last element from the list and return it")
print("=================================================================")

# Question 18
print("18. What is the output of the following program?")

tuple = (1, 2, 3, 4) 
# tuple.append((5, 6, 7)) 
# print(len(tuple))

'''
Options
A. 1
B. 2
C. Error
D. 5
'''

# Answer
print("Correct Answer: Error")
print("=================================================================")

# Question 19
print("19.  What is the output of the following program?")

tuple1 = (1, 2, 4, 3) 
tuple2 = (1, 2, 3, 4) 
print(tuple1 < tuple2) 

'''
Options
A. True
B. False
C. Error
'''

# Answer
print("Correct Answer: False")
# print("=================================================================")


