# Conditional Expression = A one-line shortcut for the if-else
# statement (ternary operators) print or assign one of two
# values based on a condition
# Syntax
#  X if condition else Y

num=5
print("Positive" if num>0 else "Negative")

num=6

a=5
b=6

print("Even" if num%2==0 else "odd")


max_num=a if a>b else b
min_num=a if a<b else b
print(f"Maximum Number :{max_num}")
print(f"Minimum Number :{min_num}")


age=20
status="Adult" if age>18 else "Not an Adult"
print(f"The status of a person :{status}")
print(status)

temprature=30
weather="Hot" if temprature > 20  else "COLD"

user_role="Admin"

access_level="Full Aceess" if user_role =="Admin" else "Limited Access"

print(access_level)

