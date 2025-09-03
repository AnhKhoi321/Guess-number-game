# if = Do some code only IF some condition is True
#      Else do something else

# Ex1
age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to sign up")
elif age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't born yet")
else:
    print("You must be 18+ to signed up")


#Ex2
response = input("Would you like food? (Y/N): ")


if response == "Y": 
    print("Have some food!")
else:
    print("No food for you")

#Ex3
name = input("Enter your name: ")

if name == "John":
    print("You did not type in your name")
else:
    print("Hello" + name)

#Ex4
online = True

if online:
    print("This user is online")
else:
    print("This user is offline")