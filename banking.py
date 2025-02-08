name = input("your name: ")
age = int(input("your age: "))
if age < 18:
    raise Exception("Your age can't be below 18")
elif age > 110 :
    raise Exception("Old")

print("You have accessed your bank")

amount = int(input("input the amount of money: "))
if amount < 0:
    raise Exception("You can't input a negative number")

def Check_amount():
    print(f"amount: {amount}")

def add_money():
    Add = int(input("Input the money you want to add: "))
    global amount
    amount = amount + Add
    print(f"amount: {amount}")

def withdraw():
    Withdraw = int(input("How much do you want to withdraw? : "))
    global amount
    if Withdraw > amount:
        raise Exception("You cant withdraw more than you have")
    else:     
        amount = amount - Withdraw
        print(f"amount: {amount}")

def main():


    while True: 
        try:
            operation = int(input("\nDo you want to :\n1. Check your amount\n2. Add money\n3. Withdraw money \n4. Exit\n="))

            if operation == 1:
                Check_amount()
            elif operation == 2:
                add_money()
            elif operation == 3:
                withdraw()
            elif operation == 4:
                break
            else: 
                raise Exception("Please pick a valid number")

        except Exception as ex:
            print(f"Error: {ex}")

        else : 
            print("Thank You")

        finally: 
            print("Thank you for using our application")

if __name__ == "__main__" :
    main()