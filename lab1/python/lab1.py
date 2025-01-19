###Python Syntax###
"""
Syntax Error:
if 5 > 2:
print("Five is greater than two!")

Right way:
if 5 > 2:
  print("Five is greater than two!")

Syntax Error:
if 5 > 2:
 print("Five is greater than two!")
        print("Five is greater than two!") 

Right way:
if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 

Variables in Python:
x = 5
y = "Hello, World!"

Comments in Python:
#This is a comment.
print("Hello, World!")
"""

###Python Comments###
"""
#This is a comment
print("Hello, World!")

print("Hello, World!") #This is a comment 

#print("Hello, World!")
print("Cheers, Mate!") 

#This is a comment
#written in
#more than just one line
print("Hello, World!")

"""
"""
This is a comment
written in
more than just one line
"""
#print("Hello, World!") 


###Python Variables###
"""
creating variables
x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0 

get the type
x = 5
y = "John"
print(type(x))
print(type(y)) 

single quotes are identical to double
x = "John"
# is the same as
x = 'John'

a = 4
A = "Sally"
#A will not overwrite a 
"""
###Variable Names###
"""
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

illegal names:
2myvar = "John"
my-var = "John"
my var = "John"

myVariableName = "John" #CamelCase. Every word except the first starts with capital letter
MyVariableName = "John" #PascalCase
my_variable_name = "John" #sneke_case 
"""
###Assign Multiple Values###
"""
Assign values to multiple variables:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

Same value to many variables:
x = y = z = "Orange"
print(x)
print(y)
print(z)

Extract values from the collections (lists, tuples(ig?) etc)
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
"""
###Output Variables###
"""
print is often used to output multiple variables
x = "Python is awesome"
print(x)

also "+" can be used
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
"""
###Global Variables###
"""
Global variables are used everywhere. For example:
x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc() 

Create a variable inside a function, with the same name as the global variable
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x) #python is fantastic

myfunc()

print("Python is " + x) # python is awesome
"""

###Python Data Types###
"""
Text Type: 	str
Numeric Types: 	int, float, complex
Sequence Types: 	list, tuple, range
Mapping Type: 	dict
Set Types: 	set, frozenset
Boolean Type: 	bool
Binary Types: 	bytes, bytearray, memoryview
None Type: 	NoneType

using type() we can get type of function
x = 5
print(type(x))

In Python, the data type is set when you assign a value to a variable:
x = "Hello World" 	str 	
x = 20 	int 	
x = 20.5 	float 	
x = 1j 	complex 	
x = ["apple", "banana", "cherry"] 	list 	
x = ("apple", "banana", "cherry") 	tuple 	
x = range(6) 	range 	
x = {"name" : "John", "age" : 36} 	dict 	
x = {"apple", "banana", "cherry"} 	set 	
x = frozenset({"apple", "banana", "cherry"}) 	frozenset 	
x = True 	bool 	
x = b"Hello" 	bytes 	
x = bytearray(5) 	bytearray 	
x = memoryview(bytes(5)) 	memoryview 	
x = None

or, if we want to specify variable
x = str("Hello World") 	str 	
x = int(20) 	int 	
x = float(20.5) 	float 	
x = complex(1j) 	complex 	
x = list(("apple", "banana", "cherry")) 	list 	
x = tuple(("apple", "banana", "cherry")) 	tuple 	
x = range(6) 	range 	
x = dict(name="John", age=36) 	dict 	
x = set(("apple", "banana", "cherry")) 	set 	
x = frozenset(("apple", "banana", "cherry")) 	frozenset 	
x = bool(5) 	bool 	
x = bytes(5) 	bytes 	
x = bytearray(5) 	bytearray 	
x = memoryview(bytes(5)) 	memoryview
"""
###Python Numbers###
"""
There are three numeric types in Python:
int
float
complex

x = 1    # int
y = 2.8  # float
z = 1j   # complex

to verify the object, we're using type()
print(type(x))
print(type(y))
print(type(z))

int is a whole number:
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z)) 

float is a number of decimals:
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

or, if we need scientific numbers
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z)) 

complex number with imaginary part written as "j"
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

type conversion:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c)) 
"""

###Python Casting###
"""
Casting in python is therefore done using constructor functions:

    int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
    float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
    str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

example for int
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

for float
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

for strings
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0' 
    
"""

###Python Strings###
"""
print("Hello") is the same to print('Hello')

we can use quotes inside strings as long as they don't match
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

assign string
a = "Hello"
print(a) 

You can use three double quotes:
a = """ """
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
""" """
print(a)

or three single quotes

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a) 

STRINGS ARE ARRAYS

Get the character at position 1 (remember that the first character has the position 0):
a = "Hello, World!"
print(a[1])

Loop through the letters in the word "banana":
for x in "banana":
  print(x)

Or use len()

The len() function returns the length of a string:
a = "Hello, World!"
print(len(a))

Check strings using keyword in
txt = "The best things in life are free!"
print("free" in txt)

Print only if "free" is present:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

Check if "expensive" is NOT present in the following text:
txt = "The best things in life are free!"
print("expensive" not in txt)

print only if "expensive" is NOT present:
txt = "The best things in life are free!"
if "expensive" not in txt:
print("No, 'expensive' is NOT present.")
"""

###Slicing Strings###
"""
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.
b = "Hello, World!"
print(b[2:5])

from the start
b = "Hello, World!"
print(b[:5])

to the end
b = "Hello, World!"
print(b[2:])

from the end (aka negative indexing)
b = "Hello, World!"
print(b[-5:-2])
"""
###Modify Strings###
"""
The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())

The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())

The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!" 

The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!'] 
"""
###Concatenate Strings###
"""
Merge variable a with variable b into variable c:
a = "Hello"
b = "World"
c = a + b
print(c)

To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)
"""

####Format Strings###
"""
we cannot use strings like this
age = 36
txt = "My name is John, I am " + age
print(txt)

instead, we can use f-strings
age = 36
txt = f"My name is John, I am {age}"
print(txt)

Add a placeholder for the price variable:
price = 59
txt = f"The price is {price} dollars"
print(txt)

Display the price with 2 decimals:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

Perform a math operation in the placeholder, and return the result:
txt = f"The price is {20 * 59} dollars"
print(txt)
"""
###Excape Characters###
""" 
You will get an error if you use double quotes inside a string that is surrounded by double quotes:
txt = "We are the so-called "Vikings" from the north."

The escape character allows you to use double quotes when you normally would not be allowed:
txt = "We are the so-called \"Vikings\" from the north."

Other escape characters used in Python:
\' 	Single Quote 	
\\ 	Backslash 	
\n 	New Line 	
\r 	Carriage Return 	
\t 	Tab 	
\b 	Backspace 	
\f 	Form Feed 	
\ooo 	Octal value 	
\xhh 	Hex value
"""
###String Methods###
"""
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle() 	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
"""
###String exercises###