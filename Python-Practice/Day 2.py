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

#Write a program that adds the digits in a two digit number. For example, if the input was 35, the output should be 3+5=8

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

############################################################################################

#Mathematical Operators
print(3 + 5)       #addition
print(7 - 3)       #subtraction
print(3 * 2)       #multiplication
print(6 / 3)       #division; whenever you divide something it always comes out with a floating point number
print(2 ** 6)      #exponent; left number to the power of the right number

#Everything starts at parenthesis and ends with addition and subtraction
# Parenthesis ()
# Exponents **
# Multiplication *
# Division /
# Addition +
# Subtraction -

#Example:
print(3 * 3 + 3 / 3 - 3)        #prints 7 because of PEMDAS
print(3 * (3 + 3) / 3 - 3)      #prints 3 because of PEMDAS

############################################################################################

#Write a program to calculate the BMI of an individual
#BMI = weight(kg) / height(m) ** 2

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

entered_height = float(height)
entered_weight = int(weight)

BMI = entered_weight / (entered_height ** 2)

print(int(BMI))

#or

bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)

############################################################################################

#The round() function allows you to round an integer:
print(round(8 / 3))     #prints 3 as 8 / 3 prints out 2.666666666666665 and is rounded to 3

#You can also round the number to two decimal places with the following:
print(round(8 / 3, 2))  #the ( , 2) specifies that you want to round the the number to two decimal places

#Floor division ( // ) 
#Floor division is used to get the output of an equation whose number is less than or equal to the original output:
print(8 // 3)       #prints 2 as originally 8 divided by 3 gives 2.66666666666665, but by floor division, it rounds it down to 2 since it's less than 2.6666666666665 and a whole number. You're basically chopping off everything after the decimal.

#You can continuously print the calculations on a variable using assignment operator shorthands:
result = 4 / 2
result /= 2         #divide equals will take the previous variable output and divide it by the number specified, in this case 4 divided by 2 divided by 2 again
print(result)       #prints 1.0, since every division calculation has a floating point value

#Same can be done for many of the other operators. Think of a game where you want to keep score of a player who scores 1 point:
score = 0           #scores starts off at zero
score += 1          #everytime the player scores a point, plus equals will add 1 point to the score
print(score)        #prints the new score

#Same thing can be done for minus equals(-=), multiply equals(*=), so on and so forth

############################################################################################

#F-string manipulation:
#You can use an easier method of adding variables with number or boolean values into string with f-strings:
score = 0
height = 1.86
isWinning = True

#f-String:
print(f"Your score is {score}, your height is {height}, and you are winning is {isWinning}! ")

#Make sure you add the f in front of the double or single quotes, and that your variables are in curly braces to ensure the f-string is correct

###########################################################################################

#Come up with a program that calculates the amount of days, weeks, and months you have left if you lived to 90:

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age = int(age)

x = (90 - age) * 365
y = (90 - age) * 52
z = (90 - age) * 12

print(f"You have {x} days, {y} weeks, and {z} months left. ")
