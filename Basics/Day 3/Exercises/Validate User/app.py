user=input("Enter the username = ")
if len(user) > 12:
    print(f"Your {user} username can't be more than 12 characters")
    user=input("Enter the username = ")
elif not user.find(" ") == -1:
    print(f"Your {user} username can't contains spaces ")
    user=input("Enter the username = ")
elif not user.isalpha():
    print("Your {username} can't contain numbers")
else:
    print("Welcome {username}")
