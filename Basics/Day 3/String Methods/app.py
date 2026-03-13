name=input("Enter your Full Name: ")
result=len(name)
print(f"Length of String: {result}")

namedResult=name.find(" ")
print(f"we find space on this position index = {namedResult}")


namedResult1=name.rfind("q")
print(namedResult1)

namedResult2=name.capitalize()
print(f"We captialized the first letter : {namedResult2}")

namedResult3=name.upper()
print(f"It upper case the all letters {namedResult3}")

namedResult4=name.lower()
print(f"it lower case the all letters  {namedResult4}")


namedResult5=name.isdigit()
print(f"This checks that it is digit or not {namedResult5}")

namedResult6=name.isalpha()
print(f"To check Alphabets = {namedResult6} ")

phone_number=input("Enter your phone number : ")

num1=phone_number.count("-")
print(f"Count the dashes in phone Number = {num1}")


num2=phone_number.replace("-"," ")
print(f"Replace the dashes with spaces = {num2}")


# to get the documentation of string

print(help(str))





  



