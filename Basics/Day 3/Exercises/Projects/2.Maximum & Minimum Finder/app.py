number1=int(input("Enter first number = "))
number2=int(input("Enter Second number = "))
number3=int(input("Enter Third number = "))

if(number1 > number2 and number2 > number3):
    print(f"{number1} is a maximum number")
elif(number2 > number1 and number2 > number3):
    print(f"{number2} is a maximum number")
else:
    print(f"{number3} is a maximum number")

    

