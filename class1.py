thisdict = {
  "username": "AyaanA",
  "password": "abcdefg",
 
}

print(thisdict)

# Git is a version control ssoftware that saves a snapshot of the folder and its children
"""
gt status 

git init
git add .
git commit -m 'message goes here'
git push
"""

username = 1234567
password = 9876543

if (username == 1234567 and password == 9876543 ):
    print("Acsess granted")
else:
    print("acsess denied")


''' 
9/20 Assesment

TYPES
  strings
  int
  dicts
  lists

If Statements
Loops

Needs Help with Args/ Params
  
'''



'''
EVERY LANGUAGE FOUNDATIONS

Data Types
  string  "hey29@hotmail.com"
  int     25
  array  ["apple", "bannana", "cucumber"]
  dict   {"age":"12", "name":"ayaan"}

  
Conditional Statements
IF ....
ELSE ....

Loops
FOR LOOPS
WHILE LOOPS

FUNCTIONS
'''

"""
PRINCIPAL 1: Don't hardcode data
PRINCIPAL 2: If the code repeats something stinks
"""


"""

SCENARIO 1: A user enters a form and decides to add a list of allowed websites


"""

sum = 5 + 10
sum = 7 + 9
sum = 10 + 10

# DEFINING A FUNCTION - A set of logic to be repeated aka a formula
# Name is sum
# Parameters is x and y | Variables that can be used in function
# Output a number
def sum(x, y):
  print("Ayaan rules")
  print("This is my handy sum function that adds stuff")
  print(f'These are my params {x}, {y}')
  return x + y


#  __________________________
# Calling the function by its name
# Using the function
# Arguments of 5 and 5 | Literal values of what you pass in
age = 12
print(sum(age, 7))
print(sum(3, 7))



#_______________________


manualCount = {
   "f": 1,
   "a": 2
}

def allUniqueCharacters(word):
  count = {}
  for letter in word:
    if letter in count:
      count[letter] += 1
    else:
      count[letter] = 1
  
  print(count)
      

allUniqueCharacters("faraz ahmad ababwa")
allUniqueCharacters("ayaan")