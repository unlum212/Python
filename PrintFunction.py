#Print() Function and Formatting

#In this section, we will learn about the print() function and formatting methods we use to print data types to the screen.
#Examples
print(10)
print(3.14)
print("Hello World!")
print('Hi Guys!')
#Output
'''
10
3.14
Hello World!
Hi Guys!
'''

#The "type()" function specifies the data type of the value.
#For example
x = 100
print(x)
print(type(x))
print(type(str(x)))

a = 3
b = 4.2
print(a + b)
print(type(a))
print(type(b))
#Output
'''
<class 'int'>
<class 'str'>
7.2
<class 'int'>
<class 'float'>
'''

#If we want to print several values on the same line, we can use the "," character between the values.
#For example
print("Muhammet", "Unlu", 1, 2, 3.14)
#Output
'''
Muhammet Unlu 1 2 3.14
'''

#There are some special characters used in "string" operations in Python. The two most used characters are "\n" and "\t".
#For example
print("Hello\nWorld")
print("Hello\tWorld")
print("Hi Guys!\tHow is it going?\nHi\tNot bad.")
#Output
'''
Hello
World
Hello	World
Hi Guys!	How is it going?
Hi	Not bad.
'''

#The "sep" parameter, which can be used in the "print()" function, inserts any desired character between the values we print. If this parameter is not used, a space is inserted between values by default.
#For example
print(1, 2, 3, 4, 5)
print(1, 2, 3, 4, 5, sep=".")
print("01","02","2022", sep="/")
print("Muhammet", "Unlu", "Computer Engineer", sep="\n")
#Output
'''
1 2 3 4 5
1.2.3.4.5
01/02/2022
Muhammet
Unlu
Computer Engineer
'''

#If a string is prefixed with a "*" and sent to the print function, this string will be separated into characters and each character will be printed as a separate string.
#For example
print(*"Python")
print(*"Python", sep="\n")
print(*"MUHAMMET", sep=".")
'''
P y t h o n
P
y
t
h
o
n
M.U.H.A.M.M.E.T
'''

#format() Function
#When using the "Print()" function, the defined variables can be processed more easily by using the "format()" function.
#For example
print("{},{},{},{}".format(1, 2, 3, 4))

a = 3
b = 5
print("{} + {} = {}".format(a, b, a + b))
print("The first number is {}, the second number is {}, and the sum of these two numbers is {}.".format(3,5,8))
#Output
'''
3 + 5 = 8
The first number is 3, the second number is 5, and the sum of these two numbers is 8.
'''
#We can manually specify the order of the values inside the "format()" function.
print("{3} {0} {2} {1}".format("Unlu", "Muhammet", 1, 2))
#Output
'''
2 Unlu 1 Muhammet
'''

#Any amount of decimal part can be taken.
#For example
print("{:.2f} {:.3f} {:.4f}".format(3.14638,7.324104,2.724324))
#Output
'''
3.15 7.324 2.7243
'''

