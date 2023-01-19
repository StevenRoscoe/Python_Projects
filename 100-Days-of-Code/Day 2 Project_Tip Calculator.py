#Create a tip calculator that calculates the total tip each person pays, and round the total tip to two decimal places:
#My solution - First try
print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
split = input("How many people to split the bill? ")

bill_as_float = float(bill)
tip_as_int = bill_as_float * int(tip) / 100
split_as_int = int(split)
calculated_bill = bill_as_float + tip_as_int
tip_per_person = round(calculated_bill / split_as_int, 2)
print(f"Each person should pay: ${tip_per_person}")


# Simplified solution 
# print("Welcome to the tip calculator.")
# bill = float(input("What was the total bill? $"))
# tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
# split = int(input("How many people to split the bill? "))

# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / split
# final_tip_amount = round(bill_per_person, 2)
# print(f"Each person should pay: ${final_tip_amount}")

# "{:.2f}".format       #you can also use the format function to move the decimal over two spaces and show the 0 if missing, formatting the final amount