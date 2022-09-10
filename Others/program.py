# print('Hello World')
# This code a separator>> , end=' | '

print('Hello, World!', end=' | ')
print(100, end=' | ')
print(5 + 5, end=' | ')

name = 'SteveCmd'
age = 41

# any string passed as the value of the end parameter will be used as the terminating character of the current line 
print('My name is ' + name, end=' @ ')


print('**************')


print(f'My name is {name}')
print(f'I am {age} years old')
'''This is a multiline comment however, f 
turns the strings into f-strings. 
These strings are evaluated at runtime, so 
inside a f-string, you can put any valid 
Python statement within curly braces. 
This makes embedding variables or 
even simple logic within strings very easy.'''


#Accessing elements of a string is through an index
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])


# slicing
print(name[0:3])


# figuring out the length of a string
print(len(name))


# Print a string and capitalize the first character
print(name.capitalize())


# Transform a string to uppercase use lower for lowercase
print(name.upper())


# Arithmetic in Python
a = 10
b = 5

print(a+b)
print(a-b)
print(a*b)
print(a/b) #result is a floating point
print(a//b) #result is an integer

#Handling input
school = input('Where did you study at in Primary school?')
print(f'Your primary school was {school}')

# the sort method can be used on an array
vowels = ['u', 'e', 'a', 'o', 'i']

vowels.sort()

print(vowels)


# Tuples are pretty similar to lists but you can not modify a tuple.


# Loops
vowels = ['a', 'e', 'i', 'o', 'u']

for letter in vowels:
    print(letter.upper())


# Dictionary: This is a dictionary. 
# Each letter is a key and their occurrence number is the value.
#Note that the count starts at 1
sentence = 'She sells sea shells by the sea shore'

record = {}

for letter in sentence:
    if letter in record:
        record[letter] += 1
    else:
        record[letter] = 1

print(record)

# Functions are declared using the keyword def
def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

a = float(input('First: '))
b = float(input('Second: '))
op = input('Operation (sum/sub/mul/div): ')

if op == 'sum':
    print(f'a + b = {sum(a, b)}')
elif op == 'sub':
    print(f'a - b = {sub(a, b)}')
elif op == 'mul':
    print(f'a * b = {mul(a, b)}')
elif op == 'div':
    print(f'a / b = {div(a, b)}')
else:
    print('Invalid Operation!')