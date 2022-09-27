# coding by Muhammet Unlu (muhammetunlu@gmail.com)

#To add an item to the end of the list, use the append() method
#example
myList = ["apple", "banana", "cherry"]
myList.append("orange")
print(myList)

#To insert a list item at a specified index, use the insert() method
#example
myList = ["apple", "banana", "cherry"]
myList.insert(1, "orange")
print(myList)

#To append elements from another list to the current list, use the extend() method
#example
myList = ["apple","banana","cherry"]
tropicals = ["mango", "pineapple", "papaya"]
myList.extend(tropicals)
print(myList)

#The remove() method removes the specified item.
#example
myList = ["apple", "banana", "cherry"]
myList.remove("banana")
print(myList)

#The pop() method removes the specified index
#example
myList = ["apple", "banana", "cherry"]
myList.pop(2)
print(myList)

#The del keyword also removes the specified index
#example
myList = ["apple", "banana", "cherry", "mango"]
del myList[3]
print(myList)

#The clear() method empties the list. The list still remains, but it has no content
#example
myList = ["apple", "banana", "cherry"]
myList.clear()
print(myList)

#Delete the entire list. But the list not remains
myList = ["apple", "banana", "cherry", "mango"]
del myList
print(myList)


