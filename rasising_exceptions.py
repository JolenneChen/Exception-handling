try: 
    number_1 = int(input("input the 1st number: "))
    number_2 = int(input("input the 2nd number: "))

    if number_2 < 0 :
        raise Exception("Number can't be less than 0")
    answer = number_1/number_2
    

    print(answer)

except ZeroDivisionError as ex:
    print(f"Error: number 2 cannot be 0")
    
except Exception as ex:
    print(f"Error: {ex}")
    
else : 
    print("No Error")

finally: 
    print("Thank you for using our application")