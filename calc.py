num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
calc=int(input(" 1.addition\n 2.subtraction\n 3.multiplication\n 4.division\ enter choice"))
match calc:
    case 1:
        print(f"addition is {num1+num2}")
    case 2:
        print(f"subtraction is {num1-num2}")
    case 3:
        print(f"multiplication is {num1*num2}")
    case 4:
        if num2!=0:
           print(f"division is {num1%num2}")
        else:
            print(f"can't divide by 0")
    case _:
        print("Invalid Input")


     
