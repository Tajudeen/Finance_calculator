import math      #      import math module library to perform mathematical tasks on numbers



#       menu options
print()
print("*******Menu options*******")

#       Declaring variable of menu
investment = "investment - to calculate the amount of interest you'll earn on your investment"
bond =  "bond - to calculate the amount you'll have to pay on a home loan"

#       Display menu options
print("a) ", investment)
print()
print("b) ", bond)

#       Store user's input
print()
user_option = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

#       Calculation for investment option
if      user_option == "investment":
        principal_amount  = float(input("Enter the amount of money that you are depositing: " ))
        interest_rate  = float(input("Enter interest rate : "))
        number_of_years= int(input("Enter number of years you plan on investing : "))
        type_of_interest = input("Enter the type of interest 'simple' or 'compound' ? : ").lower()

        #       Calculate the rate for simple and compound interest based on user's input
        rate = interest_rate/100

        #       simple interest calculation
        if type_of_interest == "simple":
                total_amount = principal_amount *(1 + rate * number_of_years)  # A = P *(1 + r*t)

        #       compound interest  calculation
        elif    type_of_interest == "compound" :
                total_amount = principal_amount * math.pow((1 + rate),number_of_years) # A = P * math.pow((1+r),t)

        else:
                print("Invalid interest type. Please enter 'simple' or 'compound'.")
                exit()
                
        #       Print out the final answer!
        print()
        print("*********Final Result*************")
        print(f"The total amount you will get on {type_of_interest} interest for {number_of_years} years at {interest_rate}%  is : £{total_amount:.2f}")
        
        #       user's for testing finding the difference using the values below for simple and compound interest

        principal_amount = 2000  # Example amount
        interest_rate = 8       # Example interest rate
        years = 20              # Example number of years
        simple_interest = 5200.00 
        compound_interest = 9321.91

        #       Calculation for bond option

elif    user_option == "bond" : 
        house_value = float(input("Enter present value of the house : "))
        interest_rate = float(input("Enter the annual interest rate : "))
        months = int(input("Enter number of months for the repayment: "))

        #       calculate monthly interest e.g. (8 / 100) before dividing by 12.
        monthly_interest = (interest_rate/100)/12
        #       calculate repayment
        repayment = (monthly_interest * house_value)/(1- (1 + monthly_interest)**(-months))    #repayment = (i * P)/(1 - (1 + i)**(-n))
        
        print()
        print("*********Final Result*************")
        print(f"The monthly repayment on {months} months at {interest_rate}% interest is: £{repayment:.2f}")        
else:
        print("Wrong selection Kindly check your spelling properly !!! Please enter 'investment' or 'bond' to continue..")
        