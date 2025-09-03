# name = input("Enter your full name: ")
# phone_number = input("Enter your phone number: ")



# result = len(name)
# result = name.find("o")
# result = name.rfind("h") # result will be -1 if not found 
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.isdigit()
# result = name.isalpha()
# result = phone_number.count("-")
# result = phone_number.replace("-", " ")

# print(result)


#  validate user input
# 1. username is no more than 12 characters 
# 2. username must not contain spaces 
# 3. username must not contain digits


username = input("Enter your username: ")

if len(username) > 12: 
    print("Your username must not be more than 12 characters long")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {username}")
