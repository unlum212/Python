# coding by Muhammet Unlu (muhammetunlu@gmail.com)

#Python Lists
#Lists are used to store multiple items in a single variable.
#Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.


#example
lst = ["apple", "banana", "cherry"]
print(lst)
#output
#['apple', 'banana', 'cherry']

#Allow Duplicates
#Since lists are indexed, lists can have items with the same value.
#example
lst =["apple","banana","cherry","apple","banana"]
print(lst)

#To determine how many items a list has, use the len() function
#example
lst = ["apple","banana","cherry"]
print(len(lst))

#It is also possible to use the list() constructor when creating a new list.
#exaple

myList = list(("apple", "banana", "cherry"))
print(myList)

