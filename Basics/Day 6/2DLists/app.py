# fruits=["apple","orange","banana","coconut"]
# vegetables=["celery","carrots","potatoes"]
# meats=["chicken","fish","turkey"]
# groceries=[fruits,vegetables,meats]
# # fruits[0]="pineapples"
# print(groceries[0][0])
# print(groceries[0][2])
# print(groceries[0][3])
# print(fruits)

# groceries=[("apple","orange","banana","coconut"),
#            ("celery","carrots","potatoes"),
#            ("chicken","fish","turkey")
#            ]
groceries=({"apple","orange","banana","coconut"},{"celery","carrots","potatoes"},{"chicken","fish","turkey"})
for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()