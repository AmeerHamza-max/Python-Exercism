num1=int(input('Enter first number: '))
num2=int(input('Enter first number: '))
op=input("Enter Operator to perform + - * / % = ")

if(op=='+'):
    print(f"Sum of two numbers {num1} and {num2} = {num1+num2}")
elif(op=='-'):
    print(f"Subtraction betweem two numbers {num1} and {num2} = {num1-num2}")
elif(op=='*'):
    print(f"Product of two numbers {num1} and {num2} = {num1*num2}")
elif(op=='/'):
    print(f"Division of two numbers {num1} and {num2} = {num1/num2}")
elif(op=='%'):
    print(f"Sum of two numbers {num1} and {num2} = {num1%num2}")
else:
    print("Invalid Operator")
    
