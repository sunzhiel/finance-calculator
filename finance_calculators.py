# This is a Capstone Project demonstrating the use of variables and control structures.
# It is a financial calculator that allows the user to choose either
# investing or borrowing in order to calculate potential outcomes.

import math

# Brief user on what is to come.
print("Choose either \"investment\" or \"bond\" from the menu below to proceed:")
print("")

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")
print("")

# Request user input to initiate conditional statements.
invest_or_borrow = input("Please enter \"investment\" or \"bond\": ")
user_choice = invest_or_borrow.lower()
print("")

# Wrap code in while loop to ensure program runs until a
# valid input is entered. Error message displayed otherwise.
while True:
    if user_choice != "investment" and user_choice != "bond":
        print("You've entered an invalid input!")
        print("")
        invest_or_borrow = input("Please enter \"investment\" or \"bond\": ")
        user_choice = invest_or_borrow.lower()
        print("")

# Investment is the first option.
# Request further user input to customise investment.
    elif user_choice == "investment":
        print("You selected investment.")
        print("")
        deposit = float(input("How much are you depositing? R"))
        print("")
        rate = float(input("At what percentage interest rate? "))
        print("")
        time = float(input("How many years will you invest for? "))
        print("")
        simp_or_comp = input("What kind of interest?\n Enter \"simple\" or \"compound\": ")
        interest = simp_or_comp.lower()
        print("")
        if interest == "simple":
            amount = round(deposit * (1 + ((rate/100) * time)), 2)
            print(f"If you invest R{deposit} at {rate}% {interest} interest for {time} years,\n the total amount you'll get back is R{amount}!")
            break # Use break function to terminate program after every valid operation

        elif interest == "compound":
            amount = round(deposit * math.pow(1 + (rate/100), time), 2)
        
            print(f"If you invest R{deposit} at {rate}% {interest} interest for {time} years,\n the total amount you'll get back is R{amount}!")
            break # Break function terminates program after valid operation

# Bond is the second option.
# Request more user input to set loan terms.
    elif user_choice == "bond":
        print("You selected bond.")
        print("")
        present_value = float(input("How much is the house currently worth? R"))
        print("")
        loan_rate = float(input("At what percentage interest rate is the bond? "))
        print("")
        term = float(input("How many months will you take to repay the loan? "))
        print("")
    
        monthly_payment = round(((loan_rate/100) * present_value) / (1 - math.pow((1 + (loan_rate / 100)), -term)), 2)

        print(f"If you borrow R{present_value} at {loan_rate}% and repay in {term} months,\nyour monthly repayments will be R{monthly_payment}!")
        break # Break terminates program after valid operation. Stops it running in a loop!

