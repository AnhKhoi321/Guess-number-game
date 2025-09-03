# function = A block of reusable code
#            place () after the function name to invoke it

# def happy_birthday(x, y):    
#     print(f"Happy birthday to {x}!")
#     print(f"You are {y} years old")
#     print("Happy birthday to you!")
#     print()

# happy_birthday("Bro", 20)
# happy_birthday("Steve", 30)
# happy_birthday("Joe", 40)


def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("JoeSchmo", 100.01, "01/02")
