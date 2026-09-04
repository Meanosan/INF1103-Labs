print("======================")
print("Welcome Here!") 
print("My first post!")
print("======================")

username = input("Enter Username: ")
age = int(input("Enter Age: "))
bio = "Fun Blogger"
category = input("Enter Content Category: ")
followers = 100

followers += 50
print("Day 1: ", followers)

followers += 20
print("Day 2: ", followers)

followers += 10
print("Day 3: ", followers)

print("\nInstagram Profile")
print("======================")
print("Username: ", username)
print("Age: ", age)
print("Bio: ", bio)
print("Followers: ", followers)
print("Category: ", category)

if age>40 and category == "fun":
    print("Fun has no boundaries, so enjoy no matter if you're " + str(age) + " or beyond!")


