#Input() Function
#Python input() function is used to take user input. By default, it returns the user input in form of a string.
#Examples
name = input("Please Enter Your Name: ")
print("Your name is {0}.".format(name))
#Output
'''
Please Enter Your Name: Muhammet
Your name is Muhammet.
'''
#We need to specify the input type. Otherwise, the result may be much different than we expected.
#For example
x = input("Please Enter a Number:")
print(x * 3)

y = int(input("Please Enter a Number:"))
print(y*3)
#Output
'''
Please Enter a Number:4
444
Please Enter a Number:4
12
'''
#In this example, we will be looking at how to take integer input from users. To take integer input we will be using int() along with input()
#For example
num1 = int(input("Please Enter First Number: "))
num2 = int(input("Please Enter Second Number: "))
sum = num1 + num2
print("The sum of the two given numbers is {0} ".format(sum))
'''
Please Enter First Number: 5
Please Enter Second Number: 9
The sum of the two given numbers is 14 
'''

#Similarly, we can use float() to take two float numbers
#For example
a = float(input("Please Enter First Number: "))
b = float(input("Please Enter Second Number: "))
c = a + b
print("The sum of the two given numbers is {0}".format(c))
#Output
'''
Please Enter First Number: 5.04
Please Enter Second Number: 3.14
The sum of the two given numbers is 8.18
'''

#Taking Two lists as input and appending them
#Example
lst1 = list(input("Please Enter Elements of List1:"))
lst2 = list(input("Please Enter Elements of List2:"))

# Now, we appending list2 into list1 using .append function
for i in lst2:
    lst1.append(i)
print(lst1)
#Output
'''
Please Enter Elements of List1:1234
Please Enter Elements of List2:56789
['1', '2', '3', '4', '5', '6', '7', '8', '9']

Please Enter Elements of List1:Apple
Please Enter Elements of List2:Banana
['A', 'p', 'p', 'l', 'e', 'B', 'a', 'n', 'a', 'n', 'a']
'''

#Taking input from the user as tuple
#Example
num = tuple(input("Please Enter Number:"))
print(num)
#Output
'''
Please Enter Number: 12345
('1', '2', '3', '4', '5')
'''