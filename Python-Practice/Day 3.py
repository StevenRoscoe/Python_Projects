#Day 3

#Conditional Statements

#A conditional statement is used to handle conditions in your statement. They introduce logic
#to functions that deal in decision-making.

#Ex:
if condition:
    do this
else:
    do this

#This is showing that if the condition is met for the first statement, execute that first 
#statement, otherwise execute the other statement.

#Ex 2:
water_level = 50
if water_level > 80:
    print("Drain water")
else:
    print("Continue")


#Ex 3:
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:                #or if height >= 120:
    print("Can ride!")
else:
    print("Can't ride...")

#Like in Day 2, if you want your code to factor in the 120cm as an acceptable height, you can
#use the >= operator to show greater than or equal to. These are known as comparison operators
#in Python.

#Comparison Operators
# > = greater than
# < = less than
# >= = greater than or equal 
# <= = less than or equal to 
# == = equal 
# != = not equal to 

##Note that when using just one equal sign, you're assigning a value to a variable. When using two,
#you're stating if one value is the exact same as the other.

##################################################################################################

#Write a program that works out if a given number is an odd or even number:

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

#The modulo (%) is a character used to give the remainder of a number. For this piece, any number 
#divisible by 2 equalling 0 is considered even since 2 can go into an even number fully without
#giving a remainder. On the other hand, an odd number will always give a remainder of 1 if used to
#be divisible by 2. 

#Ex:
#2 goes into 50 twenty fives times evenly with no remainder, so 50 is considered an even number.
#2 goes into 49 twenty four times with a remainder of 1, so it's considered an odd number.

##################################################################################################

#Nested if/else conditional loops can have multiple if/else statements inside of one another to 
#satisfy any number of True or False values:

#Ex:
if condition:                       
    if another condition:           #in order for this to be True, the first if has to be false
        do this                     #this executes when the first and second if statement is True
    else:
        do this                     #this executes when the first if statement is True but second is False
else:
    do this                         #this executes when everything else is False


#Ex 2:
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry but you're not tall enough to ride this ride...")

#################################################################################################

#if/elif/else statements
if condition1:
    do A                    #if condition1 is true, this executes
elif condition2:
    do B                    #if condition2 is True and condition1 is false, this executes
else:           
    do this                 #if all previous conditions are False, this executes

#Ex 3:
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry but you're not tall enough to ride this ride...")

################################################################################################
# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

# It should tell them the interpretation of their BMI based on the BMI value.

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round(weight / (height ** 2))

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")

#The reasoning behind not having comparisons between 18.5 to 25 and so on is because using elif
#with (not inside like nested) the if/else statements makes this an entire group of statements 
#that plays off of the previous statement.

################################################################################################

#Write a program that works out whether if a given year is a leap year. A normal year has 365 
#days, leap years have 366, with an extra day in February.

#This is how you work out whether if a particular year is a leap year:

# on every year that is evenly divisible by 4 

# **except** every year that is evenly divisible by 100 

# **unless** the year is also evenly divisible by 400

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

################################################################################################

#Multiple if statements in succession:

#Ex 1:
if condition1:
    do A
if condition2:
    do B
if condition3:
    do C

#Goes through and checks to make sure all statements are True

#Ex 2:
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Child tickets are $5.")
    elif age <= 18:
        print("Youth tickets are $7.")
    else:
        print("Adult tickets are $12.")
    
    wants_photo = input("Do you want a photo taken? y or n? ")

else:
    print("Sorry but you're not tall enough to ride this ride...")