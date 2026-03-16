number1=int(input("Enter a number to print a Table = "))
number2=int(input("Enter a range where to print a table = "))

for i in range(1,number2+1):
    print(f"{number1} X {i} = {number1 * i}")