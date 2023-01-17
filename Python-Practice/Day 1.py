#Day 1 of Python Practice
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

print("------------------------")

#If you want to print a new line of code on the same line, use the \n character:
print("Hello world\nHello world!")
print("Come inside please\n it's raining outside!")    #a space after the \n character creates an indentation of sorts
print("What's for dinner tonight Mom?\nChicken and Rice!\nOoohhh that sounds good!")

print("------------------------")

#When you concatenate a string, you combine it to the end of another string:
print("Hello" + "Steven")
#Try adding a space in between the two strings:
print("Hello Steven") 
print("Hello" + " " + "Steven")     #adding quotations in-between a string counts as a space in Python

print("-------------------------")

#The input() function prompts the user to enter a word or integer:
input("What is your name? ")
#Prints "Hello" along with the user's input
print("Hello " + input("What is your name? "))

#The len() function is used to determine the length of a string of characters:
print(len(input("What is your name? ")))

#Variables are definitions to a certain extent. You assign a value to a word:
name = input("What is your name? ")
print(name)         #will print the variable that was referenced. Can be referred later on in code if need be

#Try to solve the problem below:
# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

c = a       ######Think of a glass of milk and glass of coffee.
a = b       ######How would you switch them around?
b = c       ######Use another variable.

#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)