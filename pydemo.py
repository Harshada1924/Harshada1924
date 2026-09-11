#write a program to check if a number is odd or even
#a=int(input("enter number ")) 
#print("Number is Odd : ",a%2!=0)

#write a program to print age in days
#age=int(input("enter age "))
#print(f"{a} years = {age*365} days" )

#write a program to convert minutes into hours anage=int(input("enter age "))

#print(f"{min} is {min//60} hours {min%60} minutes" )

# write a program to extract the last digit of an number
#number=int(input("enter number ")) 
#print(f"{number} : last digit is {number%10}")

#write a program to check if a person is eligible for discount the criteria must be a student and age must be below 21
#role=input("Enter Role(student/teacher) : ")#demo
#age=int(input("Enter age : "))
#print(f"Eligible : {role=="student" and age<21} ") #harshada

#is_raining= False
#if is_raining==True:
 #   print("Raining Outside")
#else:
 #   print("Not Raining")

#age>=18 eligible to vote else not eligible
#age=int(input("enter age: "))
#if age>=18:
#    print("Eligible to vote")
#else:
#    print("Not Eligible to vote")

n=int(input("enter number"))
if n==1:
   print("Monday")    
elif n==2:
    print("Tuesday")
elif n==3:
    print("wednsday")
elif n==4:
    print("Thursday")
elif n==5:
    print("friday")
elif n==6:
    print("saturday")
elif n==7:
    print("sunday")
else:
    print("INVALID NO.")

AGE=20
has_id=True
if AGE>=18:
    if has_id:
        print("entry allowed")
    else:
        print("entry not allowed")
else:
    print("NO ENTRY")

day=int(input("enter the day number: "))
match day:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednsday")
    case _:
        print("invalid input")