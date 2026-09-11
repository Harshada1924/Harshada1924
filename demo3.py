#number=int(input("enter number: "))
#if number%2==0:
#    print(f"{number} is Even.")
#else:
#    print(f"{number} is Odd.")

#age=int(input("enter age: "))
#ticket_price=100
#if age<12:
#    print(f"10% off. final ticket price is {(ticket_price-ticket_price*10/100)}")
#else:
#    print(f"No Discount. Ticket Price is {ticket_price}")
#marks=int(input("Enter Marks: "))
#if marks>=90 and marks<100:
#    print("O Grade")
#elif marks>=80 and marks<90:
#    print("A Grade")
#elif marks>=65 and marks<80:
#    print("B Grade")
#elif marks>=35 and marks<65:
#    print("C Grade")
#elif marks<35 and marks>=0:
#    print("F Grade")

#else:
#    print("INVALID MARKS ")

#number=int(input("Enter Number: "))
#if number>0:
#    print(f"{number} is positive")
#elif number<0:
#    print(f"{number} is negative")
#else:
#    print(f"{number} is Neither Positive nor Negative")

#a=int(input("Enter N0. :"))
#b=int(input("Enter N0. :"))
#c=int(input("Enter N0. :"))

#if a>=b and a>=c:
#    print(f"{a}")
#elif b>=a and b>=c:
#    print(f"{b}")
#else:
#    print(f"{c}")

year=(int(input("Enter YEAR: ")))
if year%4==0 or year%400==0:
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")