#Import Turtle for visualization
import turtle

#Define function to get user input
def get_user_input():
    Monthly_Income = float(input("Please enter your Monthly Income: "))
    Rent = float(input("Please enter your monthly rent expense: "))
    Grocery = float(input("Please enter your monthly grocery expense: "))
    Transportation = float(input("Please enter your monthly transportation expense: "))
    return Monthly_Income, Rent, Grocery, Transportation

#Define function to add varibles of expenses together to get total expenses
def add_expenses(Rent,Grocery,Transportation):
    #print(Rent)
    #print(Grocery)
    #print(Transportation)
    Total_Expenses = Rent + Grocery + Transportation
    return Total_Expenses

#Define function to subtract expences from monthly income to get remaining balance
def find_difference(Monthly_Income,Total_Expenses):
    #print(Monthly_Income)
    #print(Expenses)
    Remaining_Balance = Monthly_Income - Total_Expenses
    return Remaining_Balance

#Define main function to execute all math and display results to user in a formated manner
def main():
    Monthly_Income, Rent, Grocery, Transportation = get_user_input()
    Total_Expenses = add_expenses(Rent,Grocery,Transportation)
    Remaining_Balance = find_difference(Monthly_Income,Total_Expenses)
    print(f'Monthly Income: ${Monthly_Income:,.2f}')
    print(f'Totlal Expenses: ${Total_Expenses:,.2f}')
    print(f'Remaining Balance: ${Remaining_Balance:,.2f}')

main()