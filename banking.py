def Check_amount(amount):
    print(f"amount: {amount}")

def add_money(amount):
    Add = int(input("Input the money you want to add: "))
    amount = amount + Add
    print(f"amount: {amount}")

def withdraw(amount):
    Withdraw = int(input("How much do you want to withdraw? : "))
    if Withdraw > amount:
        raise Exception("You cant withdraw more than you have")
    else:     
        amount = amount - Withdraw
        print(f"amount: {amount}")

try:
    amount = int(input("input the amount of money: "))
    if amount < 0:
        raise Exception("You can't input a negative number")

    function = int(input(print('''
     Do you want to :
    1. Check your amount
    2. Add money
    3. Withdraw money
    =
    ''')))

    if function == 1:
        Check_amount(amount)
    elif function == 2:
        add_money(amount)
    elif function == 3:
        withdraw(amount)
    else: 
        raise Exception("Please pick a valid number")

except Exception as ex:
    print(f"Error: {ex}")

else : 
    print("No Error")

finally: 
    print("Thank you for using our application")