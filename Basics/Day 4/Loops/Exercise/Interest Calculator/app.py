# principal=0
# rate=0
# time=0
# while principal <=0:
#     principal=float(input("Enter the principle amount: "))
#     if principal <= 0:
#         print("Principle can't be less than or equal to zero")

# while rate <=0:
#     rate=float(input("Enter the interest rate amount: "))
#     if rate <= 0:
#         print("Interest rate can't be less than or equal to zero")

# while time <=0:
#     time=float(input("Enter the time in years: "))
#     if time <= 0:
#         print("Time can't be less than or equal to zero")

# print(principal)
# print(rate)
# print(time)


# total=principal * pow((1+rate/100),time)

# print(f"Balance after {time} years: ${total:.2f}")

principal=0
rate=0
time=0
while True:
    principal=float(input("Enter the principle amount: "))
    if principal < 0:
        print("Principle can't be less than  zero")
    else:
        break

while True:
    rate=float(input("Enter the interest rate amount: "))
    if rate < 0:
        print("Interest rate can't be less than  zero")
    else:
        break

while True:
    time=float(input("Enter the time in years: "))
    if time <= 0:
        print("Time can't be less than zero")
    else:
        break

print(principal)
print(rate)
print(time)


total=principal * pow((1+rate/100),time)

print(f"Balance after {time} years: ${total:.2f}")


# 2:06