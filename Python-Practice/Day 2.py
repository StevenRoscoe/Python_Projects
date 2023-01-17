#Day 2 of Python Practice

#Data Types

#Strings - characterized by the double quotes; can be a word or numbers
"Hello"                 

#You can use square brackets to get the position of a character in a string:
print("Hello"[0])       #prints H as H is the first letter in the string, hence the 0. Always start counting from 0 in coding
print("Hello"[4])       #prints o since it's the fifth character in the string

#Numbers inside of double or single quote are also considered strings:
print("123"[1])         #prints the 2 in the string

#You can even concatenate them:
print("123" + "456")    #prints 123456

#Spaces in between strings also count as characters
street_name = "Abbey Road"
print(street_name[4] + street_name[7])      #prints yo because of the space between Abbey and Road

############################################################################################

#Integers - whole numbers
print(123 + 456)        

#To make integers more human-readable, you can use underscores in place of commas:
print(123_992 + 554_926_785)    #prints 555050777

#To print the output with underscores you can do the following:
num1 = 100_000_000
num2 = 2_394
ans = num1*num2
print(f'{ans:_}')       #prints an 'f' string of the ans output with underscores. Can replace the underscore with a comma if need be.

############################################################################################

#Floats - #any number having a decimal is known as a floating point number
3.14159

############################################################################################

#Boolean - only having two values; True or False
True                    
False

############################################################################################

#You can use the type() function to see what kind of class a data type is:
num_char = len(input("What is your name? "))
print(type(num_char))          #will print 'int' as the length of the name is an integer data type

############################################################################################

#You can convert integers into a string with the str() function:
num_char = len(input("What is your name? "))

new_num_char = str(num_char)

print("Your name has " + new_num_char + " characters.")     #will print out the string with however many characters were input

############################################################################################

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

#print(type(two_digit_number))      #shows the variable as a string data type

first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

sum_of_two_digit_number = first_digit + second_digit
print(sum_of_two_digit_number)      #prints the sum of the two digits that were converted to integers