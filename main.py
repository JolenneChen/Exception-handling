try: 
    number_1 = int(input("input the 1st number: "))
    number_2 = int(input("input the 2nd number: "))

    answer = number_1/number_2

    print(answer)
except ZeroDivisionError as ex:
    print(f"Error: number 2 cannot be 0")
    
else : 
    print("No Error")

finally: 
    print("Thank you for using our application")