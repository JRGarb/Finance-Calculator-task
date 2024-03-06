'''The program will calculate return on investment or increase in
interest on a loan, depending on user choice of calculation.'''

import math


''' This function will take numerical input from the user and ensure it 
is correctly formatted for use in calculations, as well as preventing
unsuitable input such as strings.'''
def user_info(variable, format):
    while True:
        try:
            info = format(input(f'''
    Please enter the value of your {variable} (no symbols) :
    '''))
            break
        except ValueError:
            print("Error - not a valid number.")
            continue
    return info


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
    # Asks for user's deposit amount, percentage interest rate, and period
    # of investment in years.
    deposit = user_info("deposit", float)
    print(f'''
Deposit amount : £{deposit:.2f}
''')

    interest_rate = user_info("percentage interest rate (%)", float)
    print(f'''
Interest rate : {interest_rate:.2f} %
''')

    years = user_info("investment period in years", int)
    print(f'''
Years to calculate for : {years}
''')

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
    # Converted for use in calculations.
    percent = interest_rate / 100
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
        print(f'''
The total value of the investment at the end of the investment period will be :
£ {comp_interest:.2f}.
''')

if calc_type == "bond":
    # Asks the user for the current house value, interest rate and repayment 
    # period in months.
    house_value = user_info("house", float)
    print(f'''
House value amount : £{house_value:.2f}
''')

    interest_rate = user_info("annual percentage interest rate", float)
    print(f'''
Annual interest rate : {interest_rate:.2f} (%)
''')

    months = user_info("repayment period in months", int)
    print(f'''
Months to repay : {months}
''')

    # Calculates the users monthly repayment amount and returns it to them.
    percent = interest_rate / 100
    month_percent = percent / 12
    month_repay = (month_percent * house_value) / (1 - (1 + month_percent) ** (-months))
    print(f"\nYour monthly repayment amount is : £ {month_repay:.2f}.")