import math
radius=float(input("Enter the radius of circle"))
circumference=2*math.pi*radius
print(f"The cicumference is:{round(circumference,2)}cm")


# Area of circle
radius2=float(input("Enter teh radius of the circle: "))
area=math.pi *pow(radius,2)
print(f"The area of the circle is: {area}cm^2")

# Pathagoras theoreom
a=float(input("Enter side A: "))
b=float(input("Enter Side B: "))
c=math.sqrt(pow(a,2) + pow(b,2))
print(f"Sude C = {c}")
