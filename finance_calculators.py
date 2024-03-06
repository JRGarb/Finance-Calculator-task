'''The program will calculate return on investment or increase in
interest on a loan, depending on user choice of calculation.'''

import math

user_choice = """
Investment - to calculate the amount of interest you'll earn on your investment.
Bond       - to calculate the monthly amount you will have to pay on a home loan.
"""

# Welcome messages and prompting user choice from set options.
print(f'''
Welcome to the finance calculator tool.
Please select from the following options :
{user_choice}
Which option would you like today?''')

# Requests user choice and handles errors.
while True:
    calc_type = input("Please type 'investment' or 'bond' : ").lower().strip()
    if calc_type != "investment" and calc_type != "bond":
        print("Choice not recognised.")
        continue
    else:
        break

if calc_type == "investment":

    # Asks for user's deposit amount and restricts it to numbers only.
    while True:
        try:
            deposit = float(input('''
Please enter the value of the deposit amount : £
'''))
            print(f"\nDeposit amount : £{deposit}")
            break
        except ValueError:
            print("Error - entry not a valid number.")

    # Asks for user's interest percentage and restricts it to numbers only.
    while True:
        try:
            interest_rate = float(input('''
Please enter your percentage interest rate (%) :
'''))
            print(f"\nInterest rate : {interest_rate} %")
            break
        except ValueError:
            print("Error - entry not a valid number.")

    # Converts user percentage into a decimal equivalent for use in calculation.
    percent = interest_rate / 100

    # Asks for the number of years user wants to calculate interest 
    # for and restricts it to whole numbers only.
    while True:
        try:
            years = int(input('''
Please enter the number of years to calculate for :
'''))
            print(f"\nYears : {years} ")
            break
        except ValueError:
            print("Error - entry not a valid number.")

    # Prompts user to select simple or compound interest calculation.
    interest_type = input("""
Would you like 'simple' or 'compound' interest?
Please type : 
""").lower().strip()
    
    while interest_type != "simple" and interest_type != "compound":
        print("Choice not recognised.")
        interest_type = input("""
Would you like 'simple' or 'compound' interest?
Please type : 
""").lower().strip()

    # Calculates simple interest for the user and returns the total
    # final value of their investment.
    if interest_type == "simple":
        simp_interest = deposit * (1 + percent*years)
        simp_interest = round(simp_interest, 2)
        print(f'''
The total value of the investment at the end of the investment period will be :
£ {simp_interest}.
''')

    # Calculates compound interest for the user and returns the total final
    # value of their investment.
    if interest_type == "compound":
        comp_interest =  deposit * math.pow((1 + percent) , years)
        comp_interest = round(comp_interest, 2)
        print(f'''
The total value of the investment at the end of the investment period will be :
£ {comp_interest}.
''')

if calc_type == "bond":
    # Asks the user for the current house value and restricts it to numbers only.
    while True:
        try:
            house_value = float(input('''
Please enter the current value of your house (no symbols):
£ '''))
            print(f"\nHouse value amount : £{house_value}")
            break
        except ValueError:
            print("Error - entry not a valid number.")
    
    # Asks the user for their interest rate and restricts it to numbers only.
    while True:
        try:
            interest_rate = float(input('''
Please enter your annual percentage interest rate (%) :
'''))
            print(f"\nAnnual interest rate : {interest_rate} %")
            break
        except ValueError:
            print("Error - entry not a valid number.")

    # Converts user percentage into a monthly decimal for use in calculation.
    percent = interest_rate / 100
    month_percent = percent / 12

    # Asks the user for the number of months they are repaying over.
    while True:
        try:
            months = int(input('''
Please enter the number of months you have to repay the loan :
'''))
            print(f"\nMonths to repay : {months}")
            break
        except ValueError:
            print("Error - entry not a valid number.")

    # Calculates the users monthly repayment amount and returns it to them.
    month_repay = (month_percent * house_value) / (1 - (1 + month_percent) ** (-months))
    month_repay = round(month_repay, 2)
    print(f"\nYour monthly repayment amount is : £ {month_repay}.")