num1=int(input("Enter a where to start = "))
num2=int(input("Enter a where to end = "))

while num1 < num2:
    if(num1%2==0):
        print(f"{num1} is an even number within given range ")
    else:
        print(f"{num1} is an odd number within given range")
    num1+=1