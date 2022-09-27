# coding by Muhammet Unlu (muhammetunlu@gmail.com)

#List items are indexed and you can access them by referring to the index number.
#example
list = ["apple","banana","cherry"] # [0]=apple, [1]=banana, [2]=cherry
print(list[1])

#Negative indexing means start from the end. -1 refers to the last item, -2 refers to the second last item etc.
#example
list = ["apple","banana", "cherry"]
print(list[-1])

#You can specify a range of indexes by specifying where to start and where to end the range.
#example
myList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(myList[3:6])

#In this example will return the items from index 0 to index 4. Remember that index 0 is the first item, and index 4 is the fifth item
#example
list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list[:4])

# In this example, will return the items from index 2 to the end.
#example
list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list[2:])

#Specify negative indexes if you want to start the search from the end of the list
#example
mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(mylist[-5:-1])

#to determine if a specified item is present in a list use the "in" keyword
#example
fruits = ["apple", "banana", "cherry", "orange", "kiwi"]
if "mango" in fruits:
    print("Yes, the fruit is in the fruits list")
else:
    print("No, the fruit not have in the fruits list")

#To change the value of a specific item, refer to the index number
#example
myLst = ["apple", "banana", "cherry"]
myLst[1] = "mango"
print(myLst)

#To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values
myList = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
myList[1:3] = ["blackcurrant", "watermelon"]
print(myList)

#To insert a new list item, without replacing any of the existing values, we can use the insert() method
#example
myList = ["apple", "banana", "cherry"]
myList.insert(2, "watermelon")
print(myList)