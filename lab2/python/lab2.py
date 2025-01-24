###BOOLEANS###
"""
In programming you often need to know if an expression is True or False.
You can evaluate any expression in Python, and get one of two answers, True or False.
When you compare two values, the expression is evaluated and Python returns the Boolean answer:

print(10 > 9)
print(10 == 9)
print(10 < 9)
"""
###OPERATORS###
"""
Operators are used to perform operations on variables and values.

In the example below, we use the + operator to add together two values:

print(10 + 5) 

"""
###LISTS###
"""
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:
thislist = ["apple", "banana", "cherry"]
print(thislist)
"""

#ACCESS LIST###
"""
List items are indexed and you can access them by referring to the index number:

thislist = ["apple", "banana", "cherry"]
print(thislist[1])
"""

###CHANGE LIST###
"""
To change the value of a specific item, refer to the index number:

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
"""

###ADD LIST###
"""
To add an item to the end of the list, use the append() method:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
"""

###REMOVE LIST###
"""
The remove() method removes the specified item.
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
"""
###LOOP LISTS###
"""
You can loop through the list items by using a for loop:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x) 
"""
###LIST COMPREHENSION###
"""

List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

Example:

Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

Without list comprehension you will have to write a for statement with a conditional test inside:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist) 
"""
###SORT LISTS###
"""
List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

"""
###COPY LISTS###
"""
You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
"""
###JOIN LISTS###
"""

There are several ways to join, or concatenate, two or more lists in Python.

One of the easiest ways are by using the + operator.

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3) 
"""
###LIST METHODS###
"""
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""
###PYTHON TUPLES###
"""
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.

thistuple = ("apple", "banana", "cherry")
print(thistuple)

"""
###ACCESS TUPLES###
"""
You can access tuple items by referring to the index number, inside square brackets:
Note: The first item has index 0.
Print the second item in the tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
"""
###UPDATE TUPLES###
"""
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x) 

"""
###UNPACK TUPLES###
"""
When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
Packing a tuple:
fruits = ("apple", "banana", "cherry")

Unpacking a tuple:
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
"""
###LOOP TUPLES###
"""
You can loop through the tuple items by using a for loop.

Iterate through the items and print the values:
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x) 
"""
###JOIN TUPLES###
"""
To join two or more tuples you can use the + operator:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3) 

"""
###TUPLE METHODS###
"""
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
"""
###PYTHON SETS###
"""
Sets are used to store multiple items in a single variable.
Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
A set is a collection which is unordered, unchangeable*, and unindexed.
* Note: Set items are unchangeable, but you can remove items and add new items.

Create a Set:
thisset = {"apple", "banana", "cherry"}
print(thisset) 
"""
###ACCESS SET ITEMS###
"""
You cannot access items in a set by referring to an index or a key.
But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

"""
###ADD SET###
"""
Once a set is created, you cannot change its items, but you can add new items.
To add one item to a set use the add() method.

Add an item to a set, using the add() method:
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset) 
"""
###REMOVE SET###
"""
To remove an item in a set, use the remove(), or the discard() method.

Remove "banana" by using the remove() method:
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset) 
"""
###LOOP SET###
"""
You can loop through the set items by using a for loop:

Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x) 
"""
###JOIN SET###
"""
There are several ways to join two or more sets in Python.
The union() and update() methods joins all items from both sets.
The intersection() method keeps ONLY the duplicates.
The difference() method keeps the items from the first set that are not in the other set(s).
The symmetric_difference() method keeps all items EXCEPT the duplicates.

Join set1 and set2 into a new set:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3) 
"""
###SET METHODS###
"""
add() 	  	Adds an element to the set
clear() 	  	Removes all the elements from the set
copy() 	  	Returns a copy of the set
difference() 	- 	Returns a set containing the difference between two or more sets
difference_update() 	-= 	Removes the items in this set that are also included in another, specified set
discard() 	  	Remove the specified item
intersection() 	& 	Returns a set, that is the intersection of two other sets
intersection_update() 	&= 	Removes the items in this set that are not present in other, specified set(s)
isdisjoint() 	  	Returns whether two sets have a intersection or not
issubset() 	<= 	Returns whether another set contains this set or not
  	< 	Returns whether all items in this set is present in other, specified set(s)
issuperset() 	>= 	Returns whether this set contains another set or not
  	> 	Returns whether all items in other, specified set(s) is present in this set
pop() 	  	Removes an element from the set
remove() 	  	Removes the specified element
symmetric_difference() 	^ 	Returns a set with the symmetric differences of two sets
symmetric_difference_update() 	^= 	Inserts the symmetric differences from this set and another
union() 	| 	Return a set containing the union of sets
update() 	|= 	Update the set with the union of this set and others
"""
###PYTHON DICTIONARIES###
"""
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
Dictionaries are written with curly brackets, and have keys and values:

Create and print a dictionary:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
"""
###ACCESS ITEMS###
"""
You can access the items of a dictionary by referring to its key name, inside square brackets:
Get the value of the "model" key:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
"""
###CHANGE ITEMS###
"""
You can change the value of a specific item by referring to its key name:
Change the "year" to 2018:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

"""
###ADD ITEMS###
"""
Adding an item to the dictionary is done by using a new index key and assigning a value to it:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

"""
###REMOVE ITEMS###
"""
There are several methods to remove items from a dictionary:

The pop() method removes the item with the specified key name:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict) 
"""
###LOOP DICTIONARIES###
"""
You can loop through a dictionary by using a for loop.
When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

for x in thisdict:
  print(x) 
"""
###COPY DICTIONARIES###
"""
Make a copy of a dictionary with the copy() method:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

"""
###NESTED DICTIONARIES###
"""
Create a dictionary that contain three dictionaries:
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
} 
"""
###DICTIONARY METHODS###
"""
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
"""
###IF/ELSE###
"""
Python supports the usual logical conditions from mathematics:

    Equals: a == b
    Not Equals: a != b
    Less than: a < b
    Less than or equal to: a <= b
    Greater than: a > b
    Greater than or equal to: a >= b

These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the if keyword.

Example:
a = 33
b = 200
if b > a:
  print("b is greater than a")
"""
###WHILE LOOPS###
"""
Python has two primitive loop commands:
    while loops
    for loops

Print i as long as i is less than 6:

i = 1
while i < 6:
  print(i)
  i += 1
"""
###FOR LOOPS###
"""
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

Print each fruit in a fruit list:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
"""