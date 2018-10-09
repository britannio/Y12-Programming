
'''
Notes
-----

in psuedo code variable assignment is shown with an arrow insead of an


'''

import math

i = 0  # int
name = "Britannio"
myFloat = 5.6 # also called a real (real number)
myChar = "h" # demo char
# int myInt = 4 explicit casting

number = myFloat * myFloat + myFloat - (2 * myFloat) ** 2 % 5

print(number)

print(round(myFloat))

print(math.trunc(myFloat)) # cuts off the

print(myFloat % 2) # modulus
print(myFloat // 2) # floor division

print(len(name)) # length of the variable

print(name.title()) # First letter is capitalised
print(name.upper()) # upper case
print(name.lower()) # lower case
print(name.find("brit"))
print(ord(myChar)) #ascii/unicode
print(chr(104)) # value from ascii/unicode
print(str(myFloat) + name) # Concatenate

# Variable. Content that can change during the course of a program
# Constant. Cannot change once declared

if name != "Britannio" :
    print("1")
else:
    print("2")

try:
    int("string")
except Exception as e:
    print("e")

name2 =  name #input("Enter your name:")
print(len(name))

if (type(name2) is str):
    if len(name2) > 5:
        print("Your name has more than five characters")
    else:
        print("Your name doesn't have more than five characters")
else:
    print("only strings are accepted")

'''
'catch all' is the same as 'else'
there's no limit to the amount of elif statements allowed

case statements

Boolean operators:
AND
OR
NOT
XOR(exclusive OR)

'repeat until loop' (do while) runs code once before evaluating a condition

'''
i = 1
while i <= 10:
    print(i)
    i = i + 1

for letter in name:
    if letter.lower() == 'z':
        print("a")
    else:
        print(chr(ord(letter) + 1))

'''
Chapter 4
Elementary data types 
Composite/elemetary data types or structured data typese.g. a string or an array
pop removes and returns a value from an array
Array operations:


'''

myArray = [1,2,3,4,5,6]
myMDArray = [[1,2,3,4,5,6],myArray, [2,3,4,5,6,7]]

for x in myArray:
    print(x)

newArray = []
x = 0
y = 0
while x < 1:
    while y < 10:
        newArray.append([0 for i in range(10)])
        y = y + 1
    x = x + 1

#print(newArray)

for row in newArray:
    print(row)


patternArray1 = []
patternArray2 = []
isOne = False

print("---")

for x in range(10):
    if isOne:
        patternArray1.append(0)
        isOne = False
    else:
        patternArray1.append(1)
        isOne = True

isOne = True
for x in range(10):
    if isOne:
        patternArray2.append(0)
        isOne = False
    else:
        patternArray2.append(1)
        isOne = True

for x in range(10):
    if isOne:
        print(patternArray1)
        isOne = False
    else:
        print(patternArray2)
        isOne = True

print("-----")

for x in range(10): print([0 for x in range(10)])


'''
subroutine - repeatable code that can be called.
procedure - subroutine that doesn't return data
function - subroutine that does return data

len() is an example of a function
print() is an example of a procedure

language in-built functions are functions that are pre-defined

local variable - only in the defined scope
global variable - available everywhere

modular programming - breaking code down into subroutines



C6 - files and exception handling

files can have records, each record having a field.
Fields can refer to columns of data or an individual piece of data
'''
# TODO: learn how to read and write to a text file
'''
error handling - catching errors to prevent crashes

'''

print("09/10/2018 \n")
'''

Dictionaries
- Holds key and value pairs
'''
myDict = {"name":"bob", "age":17, "height-m":"1.6",}
print(myDict["height-m"])

with open("text_file.txt", "w") as file:
    file.write("Hello world!")

try:
    myString = int(input(":"))
except TypeError:
    print("Invalid input")
except Exception as e:
    print("Exception", str(e))















