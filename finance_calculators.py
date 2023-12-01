'''The program will calculate return on investment or increase in interest on a loan, depending on user choice of calculation.

Start.
Import the math package.

Assign new variable (user_choice) - information on calculation options for user to choose from
Print a welcome message
Print user_choice
Print a message asking the user to choose

Assign a new variable (calc_type) - request input from user for choice of calculation and make it lowercase.
while calc_type does not equal "investment" or "bond"
    print an error message telling user the calculation type is not recognised
    request user value for calc_type again

If calc_type is equal to "investment"
    while True
        try
            assign a a new variable (deposit) - request user input for the deposit amount and cast to float
            break out of the loop
        if a value error occurs
            print an error message
                
    while True
        try
            assign a new variable (interest_rate) - request interest rate value from user and cast to float
            break out of the loop
        if a value error occurs
            print an error message

    assign a new variable (percent) - interest_rate divided by 100

    while True
        try
            assign a new variable (years) - request value from user for number of hyears of interest and cast to integer
            break out of loop
        if a value error occurs
            print an error message   
    
    assign a new variable (interest_type) - request input from user choosing simple or compound, and make this lowercase
    
    while interest_type is not equal to "simple" or "compound"
        print a sentence that tells the user they entered an unrecognised interest type
        request user input for interest_type again

    if interest_type is equal to simple
        assign a new variable (simp_interest) - calculate the simple interest based on user inputs
        print a sentence telling the user what the value of their investment plus simp_interest is, rounded to two decimal places
    if interest_type is equal to compound
        assign a new variable (comp_interest) - calculate the compound interest based on user inputs
        print a sentence telling the user what the value of their investment plus comp_interest is, rounded to two decimal places

If calc_type is equal to "bond"
    while True
        try
            assign a a new variable (house_value) - request user input for the current house value and cast to float
            break out of the loop
        if a value error occurs
            print an error message
    
    while True
        try
            assign a new variable (interest_rate) - request interest rate value from user and cast to float
            break out of the loop
        if a value error occurs
            print an error message

    assign new variable (percent) - interest_rate divided by 100
    assign new variable (month_percent) - percent divided by 12

    while True
        try
            assign a new variable (months) - request value from user for number of repayment months and cast to integer
            break out of the loop
        if a value error occurs
            print an error message

    assign new variable (month_repay) - calculate the monthly repayment amount
    print a sentence telling the user the value of month_repay

end
'''

#program begins
import math

#gives the user their options for which program to run
user_choice = """
Investment - to calculate the amount of interest you'll earn on your investment.
Bond       - to calculate the monthly amount you will have to pay on a home loan.
"""

#welcome messages and prompting user choice
print("Welcome to the finance calculator tool. Please select from the following options : ")
print(user_choice)
print("Which option would you like today?")

calc_type = input("""Please type 'investment' or 'bond' : """).lower()

#removes white space from user input, and restricts user input to required words
calc_type = calc_type.strip(" ")

while calc_type != "investment" and calc_type != "bond":
    print("Choice not recognised.")
    calc_type = input("""Please type 'investment' or 'bond' : """).lower()
    calc_type = calc_type.strip(" ")

if calc_type == "investment":

    #asks for user's deposit amount and restricts it to numbers only
    while True:
        try:
            deposit = float(input("\nPlease enter the value of the deposit amount : £ "))
            print(f"\nDeposit amount : £{deposit}")
            break
        except ValueError:
            print("Error - entry not a valid number.")

    #asks for user's interest percentage and restricts it to numbers only
    while True:
        try:
            interest_rate = float(input("\nPlease enter your percentage interest rate (%) : "))
            print(f"\nInterest rate : {interest_rate} %")
            break
        except ValueError:
            print("Error - entry not a valid number.")

    #converts user percentage into a decimal equivalent for use in calculation
    percent = interest_rate / 100

    #asks for the number of years user wants to calculate interest for and restricts it to whole numbers only
    while True:
        try:
            years = int(input("\nPlease enter the number of years to calculate for : "))
            print(f"\nYears : {years} ")
            break
        except ValueError:
            print("Error - entry not a valid number.")

    #prompts user to select simple or compound interest calculation
    interest_type = input("""
Would you like 'simple' or 'compound' interest?
Please type : 
""").lower()

    #strips white space from user input and restricts user input to required words
    interest_type = interest_type.strip(" ")
    
    while interest_type != "simple" and interest_type != "compound":
        print("Choice not recognised.")
        interest_type = input("""
Would you like 'simple' or 'compound' interest?
Please type : 
""").lower()
        interest_type = interest_type.strip(" ")
    
    #calculates simple interest for the user and returns the total final value of their investment
    if interest_type == "simple":
         simp_interest = deposit * (1 + percent*years)
         simp_interest = round(simp_interest, 2)
         print(f"\nThe total value of the investment at the end of the investment period will be : £ {simp_interest}.")

    #calculates compound interest for the user and returns the total final value of their investment
    if interest_type == "compound":
        comp_interest =  deposit * math.pow((1 + percent) , years)
        comp_interest = round(comp_interest, 2)
        print(f"\nThe total value of the investment at the end of the investment period will be : £ {comp_interest}.")

if calc_type == "bond":
    
    #asks the user for the current house value and restricts it to numbers only
    while True:
        try:
            house_value = float(input("\nPlease enter the current value of your house (no symbols): £ "))
            print(f"\nHouse value amount : £{house_value}")
            break
        except ValueError:
            print("Error - entry not a valid number.")
    
    #asks the user for their interest rate and restricts it to numbers only
    while True:
        try:
            interest_rate = float(input("\nPlease enter your annual percentage interest rate (%) : "))
            print(f"\nAnnual interest rate : {interest_rate} %")
            break
        except ValueError:
            print("Error - entry not a valid number.")

    ##converts user percentage into a monthly decimal for use in calculation
    percent = interest_rate / 100
    month_percent = percent / 12

    #asks the user for the number of months they are repaying over
    while True:
        try:
            months = int(input("\nPlease enter the number of months you have to repay the loan : "))
            print(f"\nMonths to repay : {months}")
            break
        except ValueError:
            print("Error - entry not a valid number.")

    #calculates the users monthly repayment amount and returns it to them
    month_repay = (month_percent * house_value) / (1 - (1 + month_percent) ** (-months))
    month_repay = round(month_repay, 2)
    print(f"\nYour monthly repayment amount is : £ {month_repay}.")