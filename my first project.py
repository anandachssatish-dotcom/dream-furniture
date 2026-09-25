n=int(input("Enter a number: "))
m=int(input("Enter another number: "))

choice=input("Enter your choice (+,-,*,/,%): ")
if choice=='+':
    print("The sum is:", n+m)
elif choice=='-':
    print("The difference is:", n-m)
elif choice=='*':
    print("The product is:", n*m)
elif choice=='/':
    if m!=0:
        print("The quotient is:", n/m)
    else:
        print("Error: Division by zero is not allowed.")
elif choice=='%':
    if m!=0:
        print("The remainder is:", n%m)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid choice. Please enter a valid operator (+, -, *, /, %).")
    